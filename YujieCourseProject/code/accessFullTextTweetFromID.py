import subprocess
import json
import time
import math
import os
from tqdm import tqdm

# Define input and output file paths
input_folder = "/Users/yujie/Documents/advanceddeeplearning828/health-kg-misinfo-llm/YujieCourseProject/hpv/tweet_ids/"  # Folder containing TXT files with Tweet IDs
output_folder = "/Users/yujie/Documents/advanceddeeplearning828/health-kg-misinfo-llm/YujieCourseProject/hpv/full_texts/"  # Folder to save full text files

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get all TXT files from the input folder
txt_files = [f for f in os.listdir(input_folder) if f.endswith(".txt")]

processed_files = set()
log_file = "processed_files.log"

# Load processed files from log
if os.path.exists(log_file):
    with open(log_file, "r") as f:
        processed_files = set(f.read().splitlines())

# Process only unprocessed files
for txt_file in txt_files:
    if txt_file in processed_files:
        print(f"Skipping already processed file: {txt_file}")
        continue

    tweet_ids_file = os.path.join(input_folder, txt_file)
    output_ids_txt = "tweet_ids_temp.txt"  # Temporary file for Twarc2 input
    output_jsonl = os.path.join(output_folder, f"{os.path.splitext(txt_file)[0]}_fulltext.jsonl")  # Output hydrated tweets in JSONL format

    # Read Tweet IDs from the TXT file
    tweet_ids = []
    with open(tweet_ids_file, "r", encoding="utf-8") as infile:
        for line in tqdm(infile, desc=f"Processing {txt_file}"):
            try:
                # Parse the line as JSON if it contains a JSON object
                tweet_data = json.loads(line.strip())
                tweet_id = str(tweet_data["id"])  # Extract the "id" field
            except (json.JSONDecodeError, KeyError):
                # If it's not JSON, treat it as a plain tweet ID
                tweet_id = line.strip()

            # Ensure the tweet ID is valid (convertible to an integer)
            if tweet_id.isdigit():
                tweet_ids.append(tweet_id)
                print("Tweet ID found and added:", tweet_id)
            else:
                print(f"Invalid tweet ID found and skipped: {line.strip()}")

    # Debug: Check if Tweet IDs are being read
    print(f"Total Tweet IDs found in {txt_file}: {len(tweet_ids)}")

    # Calculate the number of batches (each batch contains 100 Tweet IDs)
    batch_size = 99  # Twarc2 allows 100 IDs per request, so we use 99 to leave room for the command itself

    num_batches = math.ceil(len(tweet_ids) / batch_size)

    # Hydrate Tweet IDs in batches, respecting rate limits
    for batch_num in range(num_batches):
        start_index = batch_num * batch_size
        end_index = min((batch_num + 1) * batch_size, len(tweet_ids))
        batch_ids = tweet_ids[start_index:end_index]

        # Save current batch to the temporary tweet_ids_temp.txt
        with open(output_ids_txt, "w", encoding="utf-8") as outfile:
            for tweet_id in batch_ids:
                outfile.write(tweet_id + "\n")

        # Debug: Check if Twarc2 is running successfully
        print(f"Running twarc2 hydrate for batch {batch_num + 1}/{num_batches}...")
        subprocess.run(["twarc2", "hydrate", output_ids_txt, "temp_hydrated.jsonl"], check=True)
        print(f"Finished running twarc2 hydrate for batch {batch_num + 1}/{num_batches}.")

        # Debug: Check if temp_hydrated.jsonl is created
        if os.path.exists("temp_hydrated.jsonl"):
            print("temp_hydrated.jsonl created successfully.")
            with open("temp_hydrated.jsonl", "r", encoding="utf-8") as infile, open(output_jsonl, "a", encoding="utf-8") as outfile:
                for line in infile:
                    tweet = json.loads(line)
                    if "id" in tweet and "text" in tweet:
                        # Write tweet ID and full text as a JSON object
                        json.dump({"id": tweet["id"], "text": tweet["text"]}, outfile)
                        outfile.write("\n")
        else:
            print("temp_hydrated.jsonl not found. Skipping this batch.")

        # Sleep to respect rate limits (15 requests per 15 minutes, so 15 minutes = 900 seconds)
        if (batch_num + 1) % 15 == 0:

            # Sleep dynamically based on remaining time
            remaining_time = 900  # Replace with actual time from API response if available
            print(f"Rate limit exceeded: sleeping {remaining_time} seconds...")
            time.sleep(remaining_time)

        print(f"Batch {batch_num + 1}/{num_batches} processed for file {txt_file}.")

    # Log the processed file
    with open(log_file, "a") as f:
        f.write(txt_file + "\n")

print(f"Full tweet texts saved to folder: {output_folder}")
