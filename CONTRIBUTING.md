# Contributing to DSFSI Public Datasets Registry

Thank you for your interest in contributing to the DSFSI Public Datasets Registry! This document provides guidelines for submitting new datasets, updating existing dataset information, and improving the registry.

## Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Submitting a New Dataset](#submitting-a-new-dataset)
- [Updating Dataset Information](#updating-dataset-information)
- [Adding Local Datasets](#adding-local-datasets)
- [Reporting Issues](#reporting-issues)
- [Style Guidelines](#style-guidelines)
- [Review Process](#review-process)

## Ways to Contribute

You can contribute to the registry in several ways:

1. **Submit a new DSFSI dataset** for inclusion in the registry
2. **Update information** about existing datasets (downloads, stars, links, descriptions)
3. **Add local datasets** to the `data/` directory for teaching or research
4. **Report broken links** or outdated information
5. **Improve documentation** and categorization
6. **Suggest new features** for the registry

## Submitting a New Dataset

### Eligibility Criteria

To be included in the DSFSI registry, datasets should:

- Be produced or co-produced by DSFSI researchers
- Be publicly available (open access or with clear access instructions)
- Have clear licensing information
- Focus on South African or African contexts, languages, or social impact
- Include proper documentation

### Submission Process

1. **Gather Dataset Information**

   Collect the following details about your dataset:
   - Full name and acronym (if applicable)
   - Description (2-3 sentences)
   - Platform (HuggingFace, GitHub, Zenodo, etc.)
   - URL(s) to access the dataset
   - Languages covered (use ISO 639-1 codes: zu, xh, en, etc.)
   - Category (speech, text, terminology, legal, health, financial, educational)
   - Size (e.g., "3000 hours", "10k sentences", "1.2M tokens")
   - License
   - Tags (3-6 relevant keywords)
   - Associated paper/publication (if available)
   - Download counts and stars (if available)

2. **Create a Pull Request**

   Fork this repository and create a new branch:
   ```bash
   git checkout -b add-dataset-[dataset-name]
   ```

3. **Update Files**

   You need to update both `README.md` and `datasets_index.json`:

   **A. Update README.md**

   Add your dataset to the appropriate sections:

   - **Datasets by Category**: Add to the relevant category table
   - **Datasets by Language**: Add to relevant language sections
   - **Featured Datasets**: If your dataset is high-impact (>10k downloads or significant research impact), propose adding it to the Featured section

   Example entry for a category table:
   ```markdown
   | [My Dataset Name](https://example.com/dataset) | Platform | Language | Description | License |
   ```

   **B. Update datasets_index.json**

   Add an entry to the `datasets` array:
   ```json
   {
     "id": "unique-dataset-id",
     "name": "Full Dataset Name",
     "category": "speech|text|terminology|legal|health|financial|educational",
     "platform": "huggingface|github|zenodo|local|other",
     "url": "https://full-url-to-dataset",
     "description": "Brief description of the dataset",
     "languages": ["zu", "en"],
     "downloads": 1000,
     "stars": 50,
     "license": "CC BY 4.0",
     "tags": ["tag1", "tag2", "tag3"]
   }
   ```

   **C. Update Metadata**

   In `datasets_index.json`, increment the `total_datasets` count and update `last_updated`:
   ```json
   "metadata": {
     "total_datasets": 51,  // increment by 1
     "last_updated": "2025-12-31"  // current date
   }
   ```

4. **Submit Pull Request**

   - Provide a clear PR title: `Add [Dataset Name] to registry`
   - In the PR description, include:
     - Link to the dataset
     - Brief explanation of what the dataset contains
     - Why it should be included in the registry
     - Citation information (if applicable)

## Updating Dataset Information

If you notice outdated information (download counts, broken links, etc.):

1. **Create an Issue** or **Pull Request** with the updates
2. **Specify what changed**:
   - Old value → New value
   - Link to source of updated information
3. **Update both README.md and datasets_index.json** to keep them in sync

### Updating Metrics

Periodically, dataset metrics should be refreshed:

- **HuggingFace**: Check dataset page for current downloads/likes
- **GitHub**: Update stars, forks, contributors from repo page
- **Update date**: Change `last_updated` in JSON metadata

## Adding Local Datasets

For datasets stored directly in this repository (in the `data/` directory):

### Process

1. **Determine Appropriate Location**
   - Course datasets: `data/cos###/` (where ### is course number)
   - Financial data: `data/stocks/`
   - Other: Create new subdirectory with descriptive name

2. **Prepare Dataset**
   - Ensure data is clean and documented
   - Include README in dataset directory if needed
   - Use standard formats (CSV, JSON, Parquet)
   - Compress large files (ZIP, GZ)

3. **Create Processing Notebook** (if applicable)
   - Place in `notebooks/` directory
   - Use naming convention: `YYYY-MM-DD-prep-[dataset-name].ipynb`
   - Document all data processing steps
   - Include data source information

4. **Update Documentation**
   - Add to "Local Datasets" section in README.md
   - Add to datasets_index.json with `"platform": "local"`
   - Include `"location": "data/path/to/dataset"`

5. **Consider Git LFS**
   - For files >50MB, use Git Large File Storage
   - Add to `.gitattributes`: `*.csv filter=lfs diff=lfs merge=lfs -text`

### Local Dataset Example

```json
{
  "id": "my-local-dataset",
  "name": "My Local Dataset",
  "category": "educational",
  "platform": "local",
  "location": "data/cos900/",
  "description": "Dataset for COS900 coursework",
  "format": ["csv", "pickle"],
  "course": "COS900",
  "tags": ["education", "classification"]
}
```

## Reporting Issues

### Found a Problem?

Open an issue with:
- **Issue type**: Broken link, outdated info, missing dataset, etc.
- **Dataset name**: Which dataset is affected
- **Description**: What's wrong and what it should be
- **Evidence**: Links or screenshots supporting the issue

### Types of Issues to Report

- Broken or outdated URLs
- Incorrect download counts or stars
- Missing datasets that should be in the registry
- Categorization errors
- License information errors
- Spelling or formatting issues

## Style Guidelines

### Dataset Naming

- Use official dataset names
- Include acronyms in parentheses: `Full Name (ACRONYM)`
- Be consistent with capitalization

### Descriptions

- Write clear, concise descriptions (2-3 sentences max)
- Focus on what the dataset contains and its use cases
- Avoid marketing language
- Use present tense

### Language Codes

Use ISO 639-1 codes:
- `en` - English
- `af` - Afrikaans
- `zu` - isiZulu
- `xh` - isiXhosa
- `st` - Sesotho
- `nso` - Sepedi (Northern Sotho)
- `tn` - Setswana
- `nr` - isiNdebele
- `ss` - Siswati
- `ve` - Tshivenda
- `ts` - Xitsonga

### Tags

- Use lowercase
- Use hyphens for multi-word tags: `machine-translation`, `low-resource`
- Be specific but not overly granular
- Typical tags: `speech`, `nlp`, `multilingual`, `classification`, `asr`, `parallel-corpus`, etc.

### Categories

Use one of these predefined categories:
- `speech` - Speech and audio datasets
- `text` - Text corpora and NLP datasets
- `terminology` - Lexicons, glossaries, terminologies
- `legal` - Legal documents
- `health` - Public health data
- `financial` - Financial and economic data
- `educational` - Teaching and coursework datasets

## Review Process

1. **Submission**: You submit a PR or issue
2. **Initial Review**: DSFSI team reviews for completeness
3. **Technical Review**: Verification of:
   - Dataset accessibility
   - Correct categorization
   - Accurate information
   - Proper documentation
4. **Feedback**: Reviewers may request changes
5. **Approval**: Once approved, PR is merged
6. **Publication**: Registry is updated

### Review Timeline

- Initial review: Within 1 week
- Full review: Within 2-3 weeks
- Urgent updates (broken links): Within 2-3 days

## Questions?

If you have questions about contributing:

- **Email**: dsfsi.info@up.ac.za
- **Open an issue**: For general questions about the registry
- **GitHub Discussions**: For broader conversations (if enabled)
- **Social Media**: Reach out via [Twitter/X](https://twitter.com/dsfsi_research), [LinkedIn](https://www.linkedin.com/company/dsfsi), or [Bluesky](https://bsky.app/profile/dsfsi.bsky.social)

## Code of Conduct

By contributing, you agree to:
- Provide accurate information
- Respect intellectual property and licensing
- Be constructive in discussions
- Follow DSFSI's values of social impact and ethical data use

## Attribution

Contributors will be acknowledged in:
- Git commit history
- Annual DSFSI reports (for significant contributions)
- Dataset documentation (if you create/curate a dataset)

## License

By contributing to this registry:
- Registry content (README, JSON): CC BY 4.0
- Code and scripts: MIT License
- Individual datasets: Retain their original licenses

---

Thank you for helping make DSFSI datasets more discoverable and accessible!

**DSFSI Research Group**
University of Pretoria
[www.dsfsi.co.za](https://www.dsfsi.co.za)
