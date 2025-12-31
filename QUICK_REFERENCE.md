# DSFSI Datasets Quick Reference

## Top 5 Datasets (Start Here)

1. **[African Next Voices](https://huggingface.co/datasets/dsfsi-anv/za-african-next-voices)** - 3,000 hrs multilingual speech
2. **[za-mafoko](https://huggingface.co/collections/dsfsi/za-mafoko)** - Multilingual terminologies (9+ glossaries)
3. **[COVID-19 ZA](https://github.com/dsfsi/covid19za)** - SA pandemic data (256 ⭐)
4. **[PuoData](https://huggingface.co/datasets/dsfsi/PuoData)** - Setswana corpus + PuoBERTa models
5. **[Vuk'uzenzele](https://github.com/dsfsi/vukuzenzele-nlp)** - 11-language parallel corpus (7 ⭐)

## Quick Access by Need

### I need...
- **Speech data** → African Next Voices
- **Text in SA language** → Vuk'uzenzele or PuoData
- **Terminology** → za-mafoko collection
- **COVID data** → COVID-19 ZA
- **Translation data** → Vuk'uzenzele (11 langs)
- **Pre-trained model** → PuoBERTa or Whisper models

## Language Coverage

| Language | Speech | Text | Terminology |
|----------|--------|------|-------------|
| isiZulu | ✓ ANV | ✓ Vuk, News | ✓ Mafoko |
| Setswana | ✓ ANV | ✓ PuoData | ✓ Mafoko |
| isiXhosa | ✓ ANV, ViXSD | ✓ Vuk | ✓ Mafoko |
| Sesotho | ✓ ANV | ✓ Vuk | ✓ Mafoko |
| Sepedi | ✓ ANV | ✓ Vuk | ✓ Mafoko |
| Tshivenda | ✓ ANV | ✓ Vuk | ✓ Mafoko |
| Xitsonga | ✓ ANV | ✓ Vuk | ✓ Mafoko |
| Siswati | - | ✓ News | ✓ Mafoko |
| isiNdebele | - | ✓ Vuk | ✓ Mafoko |
| English | - | ✓ Multiple | ✓ Multiple |
| Afrikaans | - | ✓ Vuk | ✓ Mafoko |

## Accessing Datasets

### HuggingFace
```python
from datasets import load_dataset
dataset = load_dataset("dsfsi/PuoData")
```

### GitHub
```bash
git clone https://github.com/dsfsi/covid19za.git
```

### Local (this repo)
```python
import pandas as pd
df = pd.read_csv("data/stocks/top40_jse_2024_performance.csv")
```

### Search Tool
```bash
python search_datasets.py --language zu
python search_datasets.py --category speech
python search_datasets.py --query "translation"
```

## Repository Structure

```
dsfsi_datasets/
├── README.md              # Main catalog (detailed)
├── DATASETS_GUIDE.md      # How to find datasets
├── CONTRIBUTING.md        # How to add datasets
├── QUICK_REFERENCE.md     # This file
├── datasets_index.json    # Structured data
├── search_datasets.py     # Search tool
├── data/                  # Local datasets
│   ├── stocks/           # JSE Top 40 (2019-2024)
│   ├── cos781/           # Course datasets
│   ├── cos802/           # Course datasets
│   └── whats-cooking/    # Kaggle data
└── notebooks/            # Data prep notebooks
```

## By Platform

- **HuggingFace** (22 datasets): [huggingface.co/dsfsi](https://huggingface.co/dsfsi)
- **GitHub** (10+ repos): [github.com/dsfsi](https://github.com/dsfsi)
- **Zenodo** (archived): DOIs for citation
- **Local** (this repo): Small datasets

## By Category

| Category | Count | Example |
|----------|-------|---------|
| Speech | 4+ | African Next Voices |
| Text/NLP | 15+ | Vuk'uzenzele |
| Terminology | 10+ | za-mafoko |
| Legal | 2 | ZASCA-Sum |
| Health | 1 | COVID-19 ZA |
| Financial | 1 | JSE stocks |
| Educational | 6 | Course datasets |

## Pre-trained Models

### Speech Recognition (ASR)
- **Multilingual Whisper v3 Turbo** (7 languages)
- **Language-specific Whisper** (ZU, VE, TS, TN, ST)
- **MMS-1B** (NCHLT, Lwazi)

### NLP Models
- **PuoBERTa** (Setswana)
  - PuoBERTa-News (classification)
  - PuoBERTa-NER (named entities)
  - PuoBERTa-POS (part-of-speech)

## Usage Examples

### Load Speech Dataset
```python
from datasets import load_dataset
anv = load_dataset("dsfsi-anv/za-african-next-voices")
```

### Load ASR Model
```python
from transformers import pipeline
asr = pipeline("automatic-speech-recognition",
               model="dsfsi-anv/multilingual-whisper-v3-turbo")
result = asr("audio.wav")
```

### Load Language Model
```python
from transformers import pipeline
model = pipeline("fill-mask", model="dsfsi/PuoBERTa")
```

### Search Registry
```python
import json
with open('datasets_index.json') as f:
    registry = json.load(f)

# Get all Setswana datasets
tn_datasets = [d for d in registry['datasets']
               if 'tn' in d.get('languages', [])]
```

## Common Tasks

| Task | Recommended Dataset |
|------|---------------------|
| ASR (SA languages) | African Next Voices |
| Machine Translation | Vuk'uzenzele |
| Text Classification | PuoBERTa-News, AG News |
| NER | PuoBERTa-NER |
| POS Tagging | PuoBERTa-POS |
| Terminology Lookup | za-mafoko |
| Low-resource NLP | PuoData, ANV |
| Public Health | COVID-19 ZA |
| Legal Analysis | ZASCA-Sum |

## License Quick Check

- **Most permissive**: MIT, CC BY 4.0
- **Data**: Often CC BY-SA 4.0
- **Always check**: Individual dataset license

## Citation

```bibtex
@misc{dsfsi-datasets-2025,
  title={DSFSI Public Datasets Registry},
  author={{Data Science for Social Impact Research Group}},
  year={2025},
  publisher={University of Pretoria},
  url={https://github.com/dsfsi/dsfsi-datasets}
}
```

## Help & Contact

- **Website**: [dsfsi.co.za](https://www.dsfsi.co.za)
- **Email**: dsfsi.info@up.ac.za
- **Lead**: Prof Vukosi Marivate
- **GitHub**: [@dsfsi](https://github.com/dsfsi)
- **HuggingFace**: [@dsfsi](https://huggingface.co/dsfsi)
- **Social**: [Twitter/X](https://twitter.com/dsfsi_research) | [LinkedIn](https://linkedin.com/company/dsfsi) | [Bluesky](https://bsky.app/profile/dsfsi.bsky.social)

## More Information

- **Detailed catalog**: [README.md](README.md)
- **Discovery guide**: [DATASETS_GUIDE.md](DATASETS_GUIDE.md)
- **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **For Claude Code**: [CLAUDE.md](CLAUDE.md)

---

**Last Updated**: December 31, 2025

**Note**: GitHub stars (⭐) shown where available. HuggingFace download counts excluded to avoid frequent updates.
