# Praktikum ISE 2023 Patrick Zierahn

This repository contains the code and materials for the practical course "Ingenieursmäßige Software-Entwicklung"
conducted at the Karlsruher Institute for Technology (KIT).

## Project Aim

The primary objective of this practical course was to research, explore, and develop Natural Language Processing (NLP)
tools to automatically classifying research papers.

## Datasets

### Open Research Knowledge Graph (ORKG)

The [Open Research Knowledge Graph (ORKG)](https://orkg.org/) is a collaborative platform for scientific knowledge
graphs. The ORKG project currently lags a classification for the Software Architecture domain.

The ORKG dataset contains 26745 research papers. Each paper contains two interesting fields for labeling the `subfields`
and `research field`. The subfields contain a list with labels from the ORKG taxonomy. The research field contains a
single label that describes the research field. The 'subfields' contain 692 distinct labels, while the 'research field'
contains 307 labels. Each paper in the dataset has on average 119 subfields and 1 research field.

The dataset: [orkg_data.csv](data%2Forkg%2Forkg_data.csv)

### "Software Architecture" by Konersmann

The paper "Evaluation Methods and Replicability of Software Architecture Research Objects" by Konersmann et al. proposes
a taxonomy for research papers in the Software Architecture domain.

This dataset contains 150 research papers from the Software Architecture domain. The taxonomy contains many fields,
like 'Paper class', 'Threats To Validity' and 'Research Object'. A detailed description of the taxonomy can be found
in
the [SoftwareArchitectureResearch/StateOfPractice](https://gitlab.com/SoftwareArchitectureResearch/StateOfPractice/-/wikis/Data-Extraction/Taxonomy)
repository.

This project focuses on the `Research Object` field, because it can be derived from the paper's abstract. Each paper in
the dataset can contain multiple 'Research Objects':

* Architecture Analysis Method
* Architecture Design Method
* Architecture Optimization Method
* Architecture Evolution
* Architecture Description Language
* Architecture Decision Making
* Architecture Pattern
* Architecture Description
* Architecture Extraction
* Architectural Aspects
* Architectural Assumptions
* Reference Architecture
* Technical Debt

The dataset: [bib-text.csv](data%2Fsoftware_architecture%2Fbib-text.csv)

### European Conference on Software Architecture (ECSA)

The European Conference on Software Architecture (ECSA) is a collaborative network and organization dedicated to
promoting and advancing citizen science initiatives across Europe.

This dataset contains 100 research papers, with a focus on the computer science domain. The datasets contain the
following columns: `title`, `abstract`, `keywords`.

The dataset: [export_SpringerLink_ecsa.csv](data%2Fecsa%2Fexport_SpringerLink_ecsa.csv)

## Supervised-classification Experiments

The goal of this project is to develop a classifier that can automatically classify research papers given in the three
datasets.

| Notebook                                                                                                                       | Dataset                                  | NLP Tool           | Description                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [scincl_single_label_classifier.ipynb](notebooks%2Fsupervised-classification%2Fscincl_single_label_classifier.ipynb)           | ORKG: 'research field'                   | SciNCL             | Fine-tune SciNCL to predict ORKG 'research field'                                                                                             |
| [scincl_multi_label_classifier.ipynb.ipynb](notebooks%2Fsupervised-classification%2Fscincl_multi_label_classifier.ipynb.ipynb) | ORKG: 'subfields'                        | SciNCL             | Fine-tune SciNCL to predict multiple ORKG 'subfields'                                                                                         |
| [scincl_clustering.ipynb](notebooks%2Fsupervised-classification%2Fscincl_clustering.ipynb)                                     | ORKG: 'research field'                   | SciNCL             | Using SciNCL embeddings to cluster 'research field' with Random-Forest, KMeans and Agglomerative-Clustering                                   |
| [openai_chatgpt_classification.ipynb](notebooks%2Fsupervised-classification%2Fopenai_chatgpt_classification.ipynb)             | Software Architecture: 'Research Object' | OpenAI's ChatGPT   | Zero-knowledge classification of 'Research Object'                                                                                            |
| [openai_embedding_classification.ipynb](notebooks%2Fsupervised-classification%2Fopenai_embedding_classification.ipynb)         | Software Architecture: 'Research Object' | OpenAI Embeddings  | Cluster 'Research Object' with Agglomerative-Clustering                                                                                       |
| [openai_fine_tune.ipynb](notebooks%2Fsupervised-classification%2Fopenai_fine_tune.ipynb)                                       | Software Architecture: 'Research Object' | OpenAI Fine-Tuning | Fine-tune OpenAI model to classify 'Research Objects'                                                                                         |
| [openai_fine_tune_explaination.ipynb](notebooks%2Fsupervised-classification%2Fopenai_fine_tune_explaination.ipynb)             | Software Architecture: 'Research Object' | OpenAI Fine-Tuning | Fine-tune OpenAI model to classify 'Research Objects', this also add taxonomy explainations to the completions to give the model more context |
| [llama2_fine_tune.ipynb](notebooks%2Fsupervised-classification%2Fllama2_fine_tune.ipynb) (Incomplete)                          | Software Architecture: 'Research Object' | Llama 2            | The aim was to fine-tune a classifier for 'Research Objects'                                                                                  |

### Evaluation results

The following table shows the evaluation results of the different classifiers can be found:

| Notebook                                  | Predictions                                                   | Evaluation Scores                                            |
|-------------------------------------------|---------------------------------------------------------------|--------------------------------------------------------------|
| scincl_single_label_classifier.ipynb      | reports/scincl_classifier/single_label_predictions.csv        | reports/scincl_classifier/single_label_evaluation.json       |
| scincl_multi_label_classifier.ipynb.ipynb | reports/scincl_classifier/multi_label_predictions.csv         | reports/scincl_classifier/multi_label_evaluation.json        |
| scincl_clustering.ipynb                   | -                                                             | reports/scincl_clustering/evaluation.csv                     |
| openai_chatgpt_classification.ipynb       | reports/openai_chatgpt/chatgpt_classification.csv             | reports/openai_chatgpt/chatgpt_evaluation.json               |
| openai_embedding_classification.ipynb     | reports/openai_clustering/predictions.csv                     | reports/openai_clustering/evaluation.json                    |
| openai_fine_tune.ipynb                    | reports/openai_fine_tune/awesome_elion_predictions.csv        | reports/openai_fine_tune/awesome_elion_evaluation.csv        |
| openai_fine_tune_explaination.ipynb       | reports/openai_fine_tune/nostalgic_montalcini_predictions.csv | reports/openai_fine_tune/nostalgic_montalcini_evaluation.csv |

> Note: Still missing is time tracking and emission tracking for the notebooks.

## Unsupervised-classification Experiments

This project also explores unsupervised-classification methods to classify research papers. The goal is to automatically
name the clusters.

* **[auto_classify.ipynb](notebooks%2Funsupervised-classification%2Fauto_classify.ipynb)**: This notebook explores
  different unsupervised-classification methods to cluster research papers. The notebook uses the ECSA dataset. The
  notebook uses OpenAI's embedding for clustering and TD-IDF for the extraction of relevant terms. The terms are used to
  name the clusters.
* **[custom_classes.ipynb](notebooks%2Funsupervised-classification%2Fcustom_classes.ipynb)**: This notebook
  clusters papers to given classes. The notebook uses the ECSA dataset and OpenAI's embedding for clustering.

## Project Structure

The project is structured as follows:

* `data/`: Contains the datasets used in this project
* `notebooks/`: Contains the Jupyter notebooks used in this project
* `src/`: Contains the source code used in this project
* `models/`: Contains the trained models in this project
* `references/`: Contains some references
* `reports/`: Contains evaluation reports and predictions
* `requirements.txt`: Contains the Python dependencies used in this project

## Installation

To install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the notebooks, run the following command:

```bash
jupyter notebook
```
