# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository (`dsfsi_datasets`) serves as the **official public datasets registry** for the Data Science for Social Impact (DSFSI) Research Group at the University of Pretoria. It functions as:

1. **Primary Dataset Catalog**: Comprehensive index of 50+ DSFSI datasets across multiple platforms
2. **Local Dataset Host**: Small-scale datasets for teaching and specific use cases (JSE stocks, course data)
3. **Dataset Discovery Portal**: Organized access to DSFSI's ecosystem spanning HuggingFace, GitHub, Zenodo, and institutional repositories

### DSFSI Dataset Ecosystem

DSFSI maintains datasets across multiple platforms:

- **HuggingFace** ([dsfsi](https://huggingface.co/dsfsi), [dsfsi-anv](https://huggingface.co/dsfsi-anv)): 22+ datasets, 30+ models
  - Featured: African Next Voices (451k downloads), za-mafoko terminology collection (100k+ downloads), PuoData (126k downloads)
- **GitHub** ([github.com/dsfsi](https://github.com/dsfsi)): 10+ dataset repositories
  - Featured: COVID-19 ZA (256 stars), Vuk'uzenzele NLP, Gov-ZA multilingual
- **Zenodo**: Archived datasets with DOIs for academic citation
- **This Repository**: Small datasets, JSE stock data, course materials

**Research Focus**: South African and African languages, low-resource NLP, speech recognition, public health, legal documents, financial data

## Repository Structure

### Data Organization

The repository follows a hierarchical data organization pattern:

- **`data/stocks/`**: JSE (Johannesburg Stock Exchange) Top 40 stock performance data
  - Annual stock ticker lists: `top40_jse_YYYY.csv` (simple list of JSE codes)
  - Performance data: `top40_jse_YYYY_performance.csv` (daily closing prices)
  - Pickle format: `top40_jse_YYYY_performance.df` (pandas DataFrame pickles)
  - Years covered: 2019, 2021, 2022, 2023, 2024

- **`data/cos781/`**: Course datasets for COS781
  - `customer_segment_data.csv`: Customer segmentation data with demographics and behavior
  - `hypermarket_dataset.csv`: Retail transaction data
  - `market_basket_optimisation.csv`: Market basket analysis data
  - `online_retail_II.csv.zip`: E-commerce transaction data (compressed)

- **`data/cos802/`**: Course datasets for COS802
  - `ag_news_csv/`: AG News dataset for text classification
    - `train.csv`, `test.csv`: Training and test splits
    - `classes.txt`, `readme.txt`: Dataset documentation

- **`data/whats-cooking/`**: Kaggle "What's Cooking" dataset
  - `whats-cooking-kernels-only.zip`: Competition kernels archive

- **`notebooks/`**: Jupyter notebooks for data preparation
  - Pattern: `YYYY-MM-DD-prep-jse.ipynb` (dated notebooks for JSE data preparation)
  - Years: 2020, 2021, 2022, 2023, 2024, 2025

### Key Files

- **`README.md`**: Comprehensive dataset catalog organized by category, language, and platform (primary documentation)
- **`datasets_index.json`**: Structured JSON index for programmatic dataset discovery and querying
- **`CONTRIBUTING.md`**: Guidelines for submitting new datasets and updating the registry
- **`.gitignore`**: Standard Python gitignore that excludes `data/` directory from version control (though data is currently tracked)

## Discovering and Accessing Datasets

### Using the README Catalog

The README is organized for multiple discovery paths:
1. **By Category**: Speech, Text/NLP, Terminology, Legal, Health, Financial, Educational
2. **By Language**: isiZulu, Setswana, isiXhosa, Tshivenda, Xitsonga, etc.
3. **By Platform**: HuggingFace, GitHub, Zenodo, UP Repository
4. **Featured**: Top 5 most impactful datasets

### Using the JSON Index

The `datasets_index.json` provides programmatic access:

```python
import json

# Load dataset index
with open('datasets_index.json') as f:
    registry = json.load(f)

# Get all speech datasets
speech_datasets = [d for d in registry['datasets'] if d.get('category') == 'speech']

# Find datasets by language (isiZulu)
zulu_datasets = [d for d in registry['datasets'] if 'zu' in d.get('languages', [])]

# Get featured datasets
featured = registry['featured_datasets']
```

### Platform-Specific Access

**HuggingFace Datasets**:
```python
from datasets import load_dataset
dataset = load_dataset("dsfsi/PuoData")
```

**GitHub Repositories**:
```bash
git clone https://github.com/dsfsi/covid19za.git
```

**Local Datasets** (in this repo):
```python
import pandas as pd
df = pd.read_csv("data/stocks/top40_jse_2024_performance.csv")
```

## Working with JSE Stock Data

### Data Preparation Workflow

The JSE stock data follows a consistent annual preparation pattern:

1. **Source file**: Read the year's Top 40 ticker list from `data/stocks/top40_jse_YYYY.csv`
2. **Ticker transformation**: Append `.JO` suffix to each JSE code for Yahoo Finance compatibility
3. **Data fetching**: Use `yfinance` and `pandas_datareader` to fetch daily closing prices
4. **Date range**: Typically fetch first 4 months (Jan 1 - Apr 30) of each year
5. **Output formats**:
   - CSV: `data/stocks/top40_jse_YYYY_performance.csv`
   - Pickle: `data/stocks/top40_jse_YYYY_performance.df`

### Required Dependencies

Based on the notebooks, you'll need:

```python
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()  # Override pandas_datareader with yfinance backend
```

### Common Data Operations

1. **Reading ticker lists**:
   ```python
   df = pd.read_csv("../data/stocks/top40_jse_YYYY.csv")
   tickers = df['JSE Code'].apply(lambda x: x + '.JO').values.tolist()
   ```

2. **Fetching stock data**:
   ```python
   stock_data = {}
   for company in tickers:
       panel_data = pdr.get_data_yahoo(company, start_date, end_date)
       stock_data[company.split('.')[0]] = panel_data
   ```

3. **Creating performance DataFrame**:
   - Extract closing prices for all companies
   - Create DataFrame with companies as columns, dates as index
   - Remove problematic tickers (e.g., CFR has been dropped in past years)

## Git Workflow

- **Main branch**: `master`
- **Current state**: Repository has many uncommitted changes in `data/` and `notebooks/`
- **Note**: `.gitignore` excludes `data/` but data files are currently tracked (likely added before gitignore rule)

## Dataset Characteristics

### Stock Data Format

- **Ticker lists**: Single column CSV with header "JSE Code"
- **Performance data**:
  - Index: Date (YYYY-MM-DD format)
  - Columns: JSE ticker codes (without `.JO` suffix)
  - Values: Closing prices in cents (South African currency)
  - Typical row count: ~80-82 trading days (4 months of data)

### Course Data Formats

- **COS781**: Customer analytics and retail datasets (CSV format)
- **COS802**: Text classification datasets (AG News in CSV format)

## Important Conventions

1. **Notebook naming**: Use ISO date format prefix `YYYY-MM-DD-prep-jse.ipynb`
2. **Stock ticker transformation**: Always append `.JO` for Yahoo Finance API
3. **Data exclusions**: CFR ticker has been dropped in recent years (see cell-7 in notebooks)
4. **Dual output**: Always save both CSV and pickle formats for stock performance data

## Updating the Registry

When adding or updating datasets in the catalog:

### Adding a New Dataset

1. **Update `README.md`**:
   - Add to appropriate category section
   - Add to language section if applicable
   - Update Featured section if high-impact
   - Include: name, platform, URL, description, languages, downloads/stars, license, tags

2. **Update `datasets_index.json`**:
   - Add entry to `datasets` array (or `featured_datasets` if applicable)
   - Required fields: `id`, `name`, `category`, `platform`, `url`, `tags`
   - Optional but recommended: `languages`, `downloads`, `stars`, `license`, `description`

3. **Update metadata**:
   - Increment `total_datasets` count in `datasets_index.json`
   - Update `last_updated` date

### Adding Local Datasets

For datasets stored in `data/`:

1. Place data in appropriate subdirectory (`data/stocks/`, `data/cos781/`, etc.)
2. Create or update notebook in `notebooks/` if data preparation is needed
3. Document in both README and JSON index with `platform: "local"` and `location` field
4. Add to .gitattributes if needed for LFS

### Updating Dataset Metrics

Periodically update download counts, stars, and other metrics:
- HuggingFace: Check dataset pages for current downloads/likes
- GitHub: Update stars and forks from repository page
- Update `last_updated` date in JSON metadata

## Key Dataset Collections

### Featured Collections

1. **African Next Voices (ZA-ANV)**: 3,000 hours multilingual speech (7 SA languages)
2. **za-mafoko**: Multilingual terminology across 9+ specialized glossaries
3. **COVID-19 ZA**: Comprehensive pandemic data with live dashboard
4. **Vuk'uzenzele**: Government magazine in 11 languages with parallel alignments
5. **PuoBERTa/PuoData**: Setswana language model and curated corpus

### By Domain

- **Speech Recognition**: ANV, ViXSD, NCHLT, Lwazi + 8 Whisper ASR models
- **Multilingual NLP**: Vuk'uzenzele, Gov-ZA, Masakhane MT
- **Low-Resource Languages**: PuoBERTa (Setswana), various African language datasets
- **Public Health**: COVID-19 ZA with 256 stars, 64+ contributors
- **Legal**: ZASCA-Sum, State Capture transcripts
- **Terminology**: za-mafoko collection (100k+ combined downloads)

## External Datasets

The registry catalogs datasets hosted across multiple platforms:
- **Zenodo**: NLP corpora, embeddings, news data (with DOIs for citation)
- **GitHub**: State Capture transcripts, COVID-19 data, multilingual corpora
- **UP Repository**: Sentiment word lists, legal document summaries
- **HuggingFace**: 22 datasets, 30+ models (largest collection)
- **SADiLaR & NWU**: Speech corpora (Lwazi, NCHLT)

These external datasets are NOT stored in this repository but are comprehensively documented for discovery and access.

## Contact and Resources

- **Research Group**: [dsfsi.co.za](https://www.dsfsi.co.za)
- **Publications**: [dsfsi.co.za/publications](https://www.dsfsi.co.za/publications/)
- **GitHub Organization**: [github.com/dsfsi](https://github.com/dsfsi)
- **HuggingFace**: [huggingface.co/dsfsi](https://huggingface.co/dsfsi)
- **Email**: dsfsi.info@up.ac.za
- **Lead**: Prof Vukosi Marivate (vukosi.marivate@cs.up.ac.za)
- **Social Media**: [@dsfsi_research](https://twitter.com/dsfsi_research) (Twitter/X), [LinkedIn](https://www.linkedin.com/company/dsfsi), [Bluesky](https://bsky.app/profile/dsfsi.bsky.social)
