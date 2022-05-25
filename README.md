
## In Search of Sañcāras - Tradition Informed Repeated Melodic Pattern Discovery in Carnatic Music

This repository contains the accompanying code for the ISMIR 2022 submission:

`A. Anonymous: In Search of Sañcāras - Tradition Informed Repeated Melodic Pattern Discovery in Carnatic Music. [In Review for] Proceedings of the 23rd International Society for Music Information Retrieval Conference, ISMIR 2022, Bangalore, India.`

### 1. Results Explorer
You can explore all results presented in the paper, and more, using the Google Colab notebook  [here](https://colab.research.google.com/drive/115wznvNTr0cdaKN3EBWuCJMz3n-A7P-J?usp=sharing). This includes pitch plots and audio corresponding to the pattern groups returned for a selection of Carnatic performances in the [Saraga Dataset](https://mtg.github.io/saraga/).

### 2. Data
Pitch Tracks
Features
Silence/stability masks
Model
Source separated audio
Annotations
SCV
Carnatic Melody Synth
### 3. Code Usage

#### 3.1 Install
Requires Python 3.8, to install requirements...
`pip install -r requirements.txt`

#### 3.2 Relevant dependencies
The pipeline requires a model trained using the Complex Autoencoder architecture [github](https://github.com/SonyCSLParis/cae-invar) and pitch annotations of the predominant melodic line extracted using FTA-NET trained on the SCMS dataset [github](https://github.com/TISMIR22-Carnatic/carnatic-pitch-patterns)  (see **2. Data** for data and models)

#### 3.3 Configure

#### 3.4 Run

### 4. Reproducibility