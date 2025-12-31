# DSFSI Datasets Discovery Guide

A practical guide to finding and using the right dataset from the DSFSI collection.

## Quick Start

**Looking for something specific?**

- [I need a speech/audio dataset](#finding-speech-datasets)
- [I need text data in a South African language](#finding-text-datasets-by-language)
- [I need terminology or translations](#finding-terminology-resources)
- [I need data for teaching](#educational-datasets)
- [I want the most popular datasets](#featured--popular-datasets)
- [I'm doing research on low-resource languages](#low-resource-language-datasets)

## Finding Speech Datasets

### For Automatic Speech Recognition (ASR)

**Start here:** [African Next Voices (ZA-ANV)](https://huggingface.co/datasets/dsfsi-anv/za-african-next-voices)
- **Why**: Largest SA multilingual speech dataset (3,000 hours)
- **Languages**: isiZulu, Setswana, Sesotho sa Leboa, Tshivenda, Xitsonga, isiXhosa, Sesotho
- **Includes**: 8 pre-trained Whisper ASR models
- **Downloads**: 451k+

**Other options:**
- **isiXhosa only**: [Vuk'uzenzele isiXhosa Speech (ViXSD)](https://huggingface.co/datasets/lelapa/Vukuzenzele_isiXhosa_Speech_Dataset_ViXSD)
- **11 SA languages**: [NCHLT Speech Corpus](https://rma.nwu.ac.za/index.php/resource-catalogue/nchlt-speech-corpus.html)
- **Multi-language**: [Lwazi Speech Corpus](https://repo.sadilar.org/handle/20.500.12185/7)

### Pre-trained ASR Models

Available models (all on HuggingFace under `dsfsi-anv`):
- Multilingual Whisper v3 Turbo (0.8B params, 7 languages)
- Language-specific models: `whisper-large-v3-turbo-anv-[zul|ven|tso|tsn|sot]`
- MMS-1B models (NCHLT & Lwazi variants)

## Finding Text Datasets by Language

### isiZulu (Zulu)

| Dataset | Type | Size | Platform |
|---------|------|------|----------|
| [African Next Voices](https://huggingface.co/datasets/dsfsi-anv/za-african-next-voices) | Speech | 3000 hrs | HuggingFace |
| [Vuk'uzenzele Corpus](https://github.com/dsfsi/vukuzenzele-nlp) | Parallel text | 2200+ pairs | GitHub |
| [IsiZulu News 2022](https://github.com/dsfsi/za-isizulu-siswati-news-2022) | News text | - | GitHub |
| [Umsuka Parallel Corpus](https://zenodo.org/record/5035171) | EN-ZU parallel | - | Zenodo |
| za-mafoko collections | Terminology | Multiple | HuggingFace |

### Setswana (Tswana)

**Best starting point:** [PuoData](https://huggingface.co/datasets/dsfsi/PuoData)
- **Downloads**: 126k+
- **Includes**: Pre-trained [PuoBERTa](https://huggingface.co/dsfsi/PuoBERTa) model
- **Variants**: PuoBERTa-News, PuoBERTa-NER, PuoBERTa-POS

**Also available:**
- African Next Voices (speech)
- Vuk'uzenzele Corpus (text)
- za-mafoko terminology

### isiXhosa (Xhosa)

- [African Next Voices](https://huggingface.co/datasets/dsfsi-anv/za-african-next-voices) (speech)
- [ViXSD](https://huggingface.co/datasets/lelapa/Vukuzenzele_isiXhosa_Speech_Dataset_ViXSD) (speech, dedicated)
- [Vuk'uzenzele Corpus](https://github.com/dsfsi/vukuzenzele-nlp) (text)
- za-mafoko terminology

### Multiple SA Languages (11 languages)

**Best option:** [Vuk'uzenzele Corpus](https://github.com/dsfsi/vukuzenzele-nlp)
- **Languages**: English, Afrikaans, isiZulu, isiXhosa, Sesotho, Sepedi, Setswana, isiNdebele, Siswati, Tshivenda, Xitsonga
- **Type**: Parallel corpus from government magazine
- **Size**: 2,200+ aligned sentence pairs
- **Use case**: Machine translation, multilingual NLP

**Government data:** [Gov-ZA Multilingual](https://github.com/dsfsi/gov-za-multilingual)
- Cabinet statements in multiple languages

### For All Language Options

See the [Datasets by Language](README.md#datasets-by-language) section in the main README.

## Finding Terminology Resources

### za-mafoko Collection

The most comprehensive multilingual terminology resource for SA languages:

| Dataset | Focus | Downloads | Best For |
|---------|-------|-----------|----------|
| [DSAC Terminology](https://huggingface.co/datasets/dsfsi/za-mafoko-dsac) | Arts & Culture | 15.6k | Cultural terms |
| [StatsSA Terminology](https://huggingface.co/datasets/dsfsi/za-mafoko-statssa) | Statistics | 1.16k | Statistical terms |
| [UP Glossary](https://huggingface.co/datasets/dsfsi/za-mafoko-up-glossary) | Academic | 1.77k | Academic terms |
| [AI Glossary](https://huggingface.co/datasets/dsfsi/za-mafoko-ai-glossary) | AI/ML | 85 | Tech terms |
| [OERTB Terminology](https://huggingface.co/datasets/dsfsi/za-mafoko-oertb) | Education | 5.74k | Educational terms |

**Portal**: [za-mafoko.dsfsi.co.za](https://www.dsfsi.co.za/za-mafoko/)

### Other Lexicon Resources

- [WordNets for SA Languages](https://zenodo.org/record/4299515)
- [Loughran McDonald-SA-2020](https://researchdata.up.ac.za/articles/dataset/Loughran_McDonald-SA-2020_Sentiment_Word_List/14401178) (financial sentiment)

## Featured & Popular Datasets

Our top 5 most impactful datasets:

1. **[African Next Voices (ZA-ANV)](https://huggingface.co/datasets/dsfsi-anv/za-african-next-voices)** - 451k downloads
   - Speech recognition in 7 SA languages

2. **[za-mafoko Collection](https://huggingface.co/collections/dsfsi/za-mafoko)** - 100k+ downloads
   - Multilingual terminologies and glossaries

3. **[COVID-19 ZA](https://github.com/dsfsi/covid19za)** - 256 stars
   - Comprehensive pandemic data with dashboard

4. **[PuoData](https://huggingface.co/datasets/dsfsi/PuoData)** - 126k downloads
   - Setswana corpus with BERT model

5. **[Vuk'uzenzele](https://github.com/dsfsi/vukuzenzele-nlp)** - 7 stars
   - 11-language parallel corpus

## Low-Resource Language Datasets

### African Languages Beyond SA

- **Kinyarwanda & Kirundi**: [Cross-lingual models](https://github.com/rulezcasa/Cross-lingual-Kinyarwanda_Kirundi)
- **40+ African languages**: [Masakhane MT](https://github.com/masakhane-io/masakhane-mt)
- **Multiple African languages**: [Pre-trained Embeddings](https://zenodo.org/record/3668481)
- **Code-switching**: [AfroCS-xs](https://aclanthology.org/2025.acl-long.1601/)

### Language-Specific Resources

Each of the 11 SA official languages has resources in:
- Vuk'uzenzele parallel corpus
- za-mafoko terminology
- NCHLT speech corpus (where applicable)

## Domain-Specific Datasets

### Public Health

**[COVID-19 ZA](https://github.com/dsfsi/covid19za)**
- Provincial and district-level data (2020-present)
- Cases, deaths, testing, vaccination, mobility
- [Live dashboard](https://dsfsi.github.io/covid19za-dash/)
- 64+ contributors, 256 stars

### Legal Documents

- **[ZASCA-Sum](https://researchdata.up.ac.za/articles/journal_contribution/ZASCA-Sum)**: Supreme Court judgments and summaries
- **[State Capture Transcripts](https://github.com/dsfsi/project-state-capture)**: Zondo Commission transcripts

### Financial Data

**[JSE Top 40 Stock Data](data/stocks/)** (Local)
- Years: 2019, 2021, 2022, 2023, 2024
- Daily closing prices (Jan-Apr each year)
- Format: CSV and pickle
- Access: Included in this repository

### News & Media

- [IsiZulu & Siswati News 2022](https://github.com/dsfsi/za-isizulu-siswati-news-2022)
- [South African News Data 2020](https://zenodo.org/record/3668495)
- [ZA Fake News 2020](https://zenodo.org/record/4682843) (disinformation)

## Educational Datasets

Datasets curated for teaching and coursework:

### COS781 (Customer Analytics)
- Customer Segmentation Data
- Hypermarket Dataset
- Market Basket Optimisation
- Online Retail II

### COS802 (Text Analytics)
- AG News Dataset

**Location**: `data/cos781/` and `data/cos802/` in this repository

## Datasets for Specific Tasks

### Machine Translation

**Start here**: [Vuk'uzenzele Corpus](https://github.com/dsfsi/vukuzenzele-nlp)
- 11 languages, 2,200+ aligned pairs

**Also**:
- [Umsuka EN-IsiZulu Parallel Corpus](https://zenodo.org/record/5035171)
- [Masakhane MT](https://github.com/masakhane-io/masakhane-mt)
- [Gov-ZA Cabinet Statements](https://huggingface.co/datasets/dsfsi/govza-sa-cabinet-statements-sentence-aligned)

### Text Classification

- [PuoBERTa-News](https://huggingface.co/dsfsi/PuoBERTa-News) (Setswana)
- [IsiZulu & Siswati News](https://github.com/dsfsi/za-isizulu-siswati-news-2022)
- [AG News Dataset](data/cos802/ag_news_csv/) (local)

### Named Entity Recognition (NER)

- [PuoBERTa-NER](https://huggingface.co/dsfsi/PuoBERTa-NER) (Setswana)

### Part-of-Speech Tagging

- [PuoBERTa-POS](https://huggingface.co/dsfsi/PuoBERTa-POS) (Setswana)

### Embeddings & Pre-training

- [PuoData](https://huggingface.co/datasets/dsfsi/PuoData) (Setswana)
- [African Pre-Trained Embeddings](https://zenodo.org/record/3668481)

## How to Access Datasets

### From HuggingFace

```python
from datasets import load_dataset

# Load a dataset
dataset = load_dataset("dsfsi/PuoData")

# Load with specific split
train_data = load_dataset("dsfsi-anv/za-african-next-voices", split="train")
```

### From GitHub

```bash
# Clone repository
git clone https://github.com/dsfsi/covid19za.git

# Or download specific files
wget https://raw.githubusercontent.com/dsfsi/vukuzenzele-nlp/main/data/file.csv
```

### From Zenodo

- Click "Download" on the Zenodo page
- Use DOI for citation in papers
- Some datasets have APIs (check Zenodo docs)

### Local Datasets (This Repo)

```python
import pandas as pd

# JSE stock data
stocks = pd.read_csv("data/stocks/top40_jse_2024_performance.csv")

# Or pickle format
stocks_df = pd.read_pickle("data/stocks/top40_jse_2024_performance.df")

# Course data
customers = pd.read_csv("data/cos781/customer_segment_data.csv")
```

## Programmatic Search

Use `datasets_index.json` for programmatic discovery:

```python
import json

# Load registry
with open('datasets_index.json') as f:
    registry = json.load(f)

# Find all speech datasets
speech = [d for d in registry['datasets']
          if d.get('category') == 'speech']

# Find datasets by language
zulu = [d for d in registry['datasets']
        if 'zu' in d.get('languages', [])]

# Find datasets on HuggingFace
hf_datasets = [d for d in registry['datasets']
               if d.get('platform') == 'huggingface']

# Find by tag
nlp_datasets = [d for d in registry['datasets']
                if 'nlp' in d.get('tags', [])]
```

## Dataset Selection Checklist

When choosing a dataset, consider:

- [ ] **Language coverage**: Does it include your target language(s)?
- [ ] **Size**: Is it large enough for your task?
- [ ] **License**: Can you use it for your purpose (research, commercial, etc.)?
- [ ] **Quality**: Is it curated/validated? What's the error rate?
- [ ] **Documentation**: Is there a paper or detailed documentation?
- [ ] **Format**: Is it in a format you can work with?
- [ ] **Pre-trained models**: Are there models already available?
- [ ] **Community**: Is it actively maintained? Are others using it?
- [ ] **Citation**: Is there proper citation information?

## Need Help?

Can't find what you're looking for?

1. **Check the main README**: [Complete catalog](README.md)
2. **Browse by category**: See [Datasets by Category](README.md#datasets-by-category)
3. **Browse by language**: See [Datasets by Language](README.md#datasets-by-language)
4. **Check publications**: [DSFSI Publications](https://www.dsfsi.co.za/publications/)
5. **Contact us**: dsfsi.info@up.ac.za
6. **Follow us**: [Twitter/X](https://twitter.com/dsfsi_research) | [LinkedIn](https://www.linkedin.com/company/dsfsi) | [Bluesky](https://bsky.app/profile/dsfsi.bsky.social)

## Citing Datasets

When using DSFSI datasets in research:

1. **Cite the specific dataset**: Use DOI or URL from dataset page
2. **Cite the registry**: For general dataset discovery
3. **Cite the paper**: If there's an associated publication

Example citation for the registry:
```bibtex
@misc{dsfsi-datasets-2025,
  title={DSFSI Public Datasets Registry},
  author={{Data Science for Social Impact Research Group}},
  year={2025},
  publisher={University of Pretoria},
  url={https://github.com/dsfsi/dsfsi-datasets}
}
```

## Contributing

Found a dataset we should include? See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on submitting new datasets.

---

**DSFSI Research Group**
University of Pretoria
[www.dsfsi.co.za](https://www.dsfsi.co.za)
