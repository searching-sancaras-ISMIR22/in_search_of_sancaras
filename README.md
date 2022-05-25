

## In Search of Sañcāras - Tradition-Informed Repeated Melodic Pattern Discovery in Carnatic Music

This repository contains the accompanying code for the ISMIR 2022 submission:

`A. Anonymous: In Search of Sañcāras - Tradition-Informed Repeated Melodic Pattern Discovery in Carnatic Music. [In Review for the] Proceedings of the 23rd International Society for Music Information Retrieval Conference, ISMIR 2022, Bangalore, India.`

### 1. Results Explorer
You can explore all results presented in the paper, and more, using the Google Colab notebook  [here](https://colab.research.google.com/drive/115wznvNTr0cdaKN3EBWuCJMz3n-A7P-J?usp=sharing). This includes pitch plots and audio corresponding to the pattern groups returned for a selection of Carnatic performances in the [Saraga Dataset](https://mtg.github.io/saraga/).

The pitch plots corresponding to the paper results are also available in `ouput/for_paper/pitch_plots/`.

### 2. Data
All datasets and models presented in the paper are made available...
| **Data**                     | **Description**                                                     | **Location**                                |
|------------------------------|---------------------------------------------------------------------|---------------------------------------------|
| Annotations                  | Expert annotations of 3 Carnatic performances in SCV                | `data/annotations`                          |
| Saraga Carnatic Melody Synth | SCMS dataset of synthesized predominant pitch ground-truth          | [zenodo](https://zenodo.org/record/5553925) |
| Saraga Carnatic Vocal        | SCV dataset of performances for which we have multitrack recordings |                                             |
| CAE Model                    | Complex Autoencoder (CAE) trained on SCV                            | [link](url)                                 |
| Pitch Tracks                 | Predominant pitch tracks extracted using FTA-NET trained on SCMS    | `data/pitch_tracks`                         |
| Silence/Stability Masks      | Mask annotated silent or stable regions in pitch tracks             | `data/silence_stability_masks`              |
| CAE Features                 | Features for all of Saraga extracted using CAE model trained on SCV | [zenodo](url)                               |
| Source Separated Audio       | SCV dataset after Spleeter source separation                        | [zenodo](url)                               |

**Table 1** - All data relevant to task

### 3. Overview of Process

Include diagram here

### 4. Code Usage

#### 4.1 Install
Requires Python 3.8, to install requirements...

`pip install -r requirements.txt`

#### 4.2 Relevant dependencies
The pipeline requires a model trained using the Complex Autoencoder architecture [[github]](https://github.com/SonyCSLParis/cae-invar) and pitch annotations of the predominant melodic line extracted using FTA-NET trained on the SCMS dataset [[github]](https://github.com/TISMIR22-Carnatic/carnatic-pitch-patterns)  (see **Table 1** in **2. Data** for data and models)

#### 4.3 Configure

To configure the pipeline update the configuration file at `conf/conf.yaml`, in that folder you will find a README detailing each parameters function.

#### 4.4 Run
To extract the silence/stability mask for a pitch track, `<folder>/<pitch_track>.csv`using the parameters specified in `conf/mask.yaml`:

```
python src mask --config conf/mask.yaml
```

To extract the self similarity matrix for a pitch track, `<folder>/<pitch_track>.csv` masked with `<folder>/<mask>.csv` using the parameters specified in `conf/selfsim.yaml`:

```
python src selfsim --config conf/selfsim.yaml
```

To run the melodic pattern extraction pipeline using the parameters specified in `conf/pattern.yaml`:

```
python src pattern --config conf/pattern.yaml
```

There are more detailed explanations of each parameter in the `conf/` directory.

### 5. Reproducibility

`experiments/` contains various one-off scripts related to the development process and paper. The following are relevant to reproduce the paper results...	

Extract silence/stability masks - `python experiments/mask_extraction.py`

Extract CAE features - `python experiments/cae_features.py`

Gridsearch for optimum parameters - `python experiments/gridsearch.py`

Generate results for performances in paper - `python experiments/get_results.py`

Reproduce plots in paper - `python experiments/plots_for_paper.py`

Generate results for various un-annotated tracks - `python experiments/random_results.py`

Evaluate - `python experiments/evaluate.py`



