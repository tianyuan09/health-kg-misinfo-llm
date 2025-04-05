import subprocess
import json
import time
import math
import os

# Define input and output folder paths
input_folder = "/Users/yujie/Documents/advanceddeeplearning828/project/TweetsMisinformationDetection/data/hpv/annotations/"         # Folder containing JSONL files with Tweet IDs
output_folder = "/Users/yujie/Documents/advanceddeeplearning828/health-kg-misinfo-llm/YujieCourseProject/hpv/tweet_ids/"       # Folder to save temporary TXT files and outputs

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

print("Running twarc2 configure...")
subprocess.run(["twarc2", "configure"], check=True)

# Loop over all JSONL files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".jsonl"):
        tweet_ids_file = os.path.join(input_folder, filename)
        output_ids_txt = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_ids.txt")
        output_jsonl = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_tweets.jsonl")
        output_texts = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_texts.txt")
        # Read Tweet IDs from JSONL file and save them into a temporary TXT file
        tweet_ids = []
        with open(tweet_ids_file, "r", encoding="utf-8") as infile:
            for line in infile:
                tweet_data = json.loads(line)
                if "id" in tweet_data:  # Ensure the key matches your JSONL format
                    tweet_ids.append({"id": tweet_data["id"]})  # Save in the desired format

        # Write Tweet IDs to the temporary TXT file
        with open(output_ids_txt, "w", encoding="utf-8") as outfile:
            for tweet_id in tweet_ids:
                outfile.write(json.dumps(tweet_id) + "\n")
