# health-misinfo-llm
A repository for a research project on health-related misinformation, LLM, poison attack on social media data

## 1. Introduction


## 2. Literature Review

<https://github.com/penghui-yang/awesome-data-poisoning-and-backdoor-attacks>

[Paperpile](https://paperpile.com/shared/LLM-data-poisoning-fyVnJRP5pR~6g31bFg~fBQg) 

## 3. Methods

### 3.1 Data Source

#### 3.1.1 [COVIDLies](https://github.com/ucinlp/covid19-data) -- Annotated
   * Hossain, T.; Logan, R.L., IV; Ugarte, A.; Matsubara, Y.; Young, S.; Singh, S. COVIDLies: Detecting COVID-19 Misinformation on Social Media. In Proceedings of the Workshop on NLP for COVID-19 (Part 2) at EMNLP 2020; September 4 2020. [[Paper](https://openreview.net/forum?id=FCna-s-ZaIE)] [[Data](https://github.com/ucinlp/covid19-data)]
   * Rizvi, S. Misinformation Retrieval. Master Thesis. University of Waterloo, ON, Canada 2021. [[Paper](https://uwspace.uwaterloo.ca/items/868363d0-ab6a-480e-a8dd-4ce810a63597)] -- This study used COVIDLies

### 3.2 Tools

* Chroma -- storage solution for knowledge graph used in [Alber et al.](https://www.nature.com/articles/s41591-024-03445-1):
    * <https://github.com/chroma-core/chroma> 

### 3.3 Pre-trained Twitter Bert Models
* [twhin-bert-base](https://huggingface.co/Twitter/twhin-bert-base)
* [twhin-bert-large](https://huggingface.co/Twitter/twhin-bert-large)

### 3.4 Precision Medicine Knowledge Graph (PrimeKG)

PrimeKG is an **Off-the-shelf Medical KG** maintained by Harvard University. 
  * Chandak, P.; Huang, K.; Zitnik, M. Building a Knowledge Graph to Enable Precision Medicine. Sci. Data 2023, 10, 67, doi:10.1038/s41597-023-01960-3. [[Paper](https://www.nature.com/articles/s41597-023-01960-3)] [[Github](https://github.com/mims-harvard/PrimeKG)] [[Dataset](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM)]
  *   * Chandak, P.; Huang, K.; Zitnik, M. Building a Knowledge Graph to Enable Precision Medicine. Sci. Data 2023, 10, 67, doi:10.1038/s41597-023-01960-3. [[Paper](https://www.nature.com/articles/s41597-023-01960-3)] [[Github](https://github.com/mims-harvard/PrimeKG)] [[Dataset](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM)]  -- ***Used PrimeKG for data poisoning attack***
  

## 4. Results



## 5. Discussion


## Reference

[Paperpile](https://paperpile.com/shared/LLM-data-poisoning-fyVnJRP5pR~6g31bFg~fBQg) 

* Chandak, P.; Huang, K.; Zitnik, M. Building a Knowledge Graph to Enable Precision Medicine. Sci. Data 2023, 10, 67, doi:10.1038/s41597-023-01960-3. [[Paper](https://www.nature.com/articles/s41597-023-01960-3)] [[Github](https://github.com/mims-harvard/PrimeKG)] [[Dataset](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM)]

* Yang, P. Awesome-Data-Poisoning-and-Backdoor-Attacks: A Curated List of Papers & Resources Linked to Data Poisoning, Backdoor Attacks and Defenses against Them (No Longer Maintained); Github;

* Alber, D.A.; Yang, Z.; Alyakin, A.; Yang, E.; Rai, S.; Valliani, A.A.; Zhang, J.; Rosenbaum, G.R.; Amend-Thomas, A.K.; Kurland, D.B.; et al. Medical Large Language Models Are Vulnerable to Data-Poisoning Attacks. Nat. Med. 2025, 1–9, doi:10.1038/s41591-024-03445-1.

* Mozaffari-Kermani, M.; Sur-Kolay, S.; Raghunathan, A.; Jha, N.K. Systematic Poisoning Attacks on and Defenses for Machine Learning in Healthcare. IEEE J. Biomed. Health Inform. 2015, 19, 1893–1905, doi:10.1109/JBHI.2014.2344095.

* Kurita, K.; Michel, P.; Neubig, G. Weight Poisoning Attacks on Pre-Trained Models. arXiv [cs.LG] 2020.
  
## Out-of-date Stuff




