#!/usr/bin/env python3
"""
DSFSI Datasets Search Utility

A simple command-line tool for searching and filtering the DSFSI datasets registry.

Usage:
    python search_datasets.py --category speech
    python search_datasets.py --language zu
    python search_datasets.py --platform huggingface
    python search_datasets.py --tag nlp
    python search_datasets.py --query "machine translation"
"""

import json
import argparse
from typing import List, Dict, Any


def load_registry(filepath: str = 'datasets_index.json') -> Dict[str, Any]:
    """Load the datasets registry from JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def search_by_category(datasets: List[Dict], category: str) -> List[Dict]:
    """Filter datasets by category."""
    return [d for d in datasets if d.get('category') == category.lower()]


def search_by_language(datasets: List[Dict], language: str) -> List[Dict]:
    """Filter datasets by language code."""
    return [d for d in datasets if language.lower() in [lang.lower() for lang in d.get('languages', [])]]


def search_by_platform(datasets: List[Dict], platform: str) -> List[Dict]:
    """Filter datasets by platform."""
    return [d for d in datasets if d.get('platform', '').lower() == platform.lower()]


def search_by_tag(datasets: List[Dict], tag: str) -> List[Dict]:
    """Filter datasets by tag."""
    return [d for d in datasets if tag.lower() in [t.lower() for t in d.get('tags', [])]]


def search_by_query(datasets: List[Dict], query: str) -> List[Dict]:
    """Search datasets by text query in name or description."""
    query_lower = query.lower()
    results = []
    for d in datasets:
        name_match = query_lower in d.get('name', '').lower()
        desc_match = query_lower in d.get('description', '').lower()
        if name_match or desc_match:
            results.append(d)
    return results


def format_dataset(dataset: Dict, detailed: bool = False) -> str:
    """Format a dataset entry for display."""
    name = dataset.get('name', 'Unknown')
    platform = dataset.get('platform', 'Unknown')
    url = dataset.get('url', 'N/A')

    if detailed:
        category = dataset.get('category', 'N/A')
        languages = ', '.join(dataset.get('languages', ['N/A']))
        tags = ', '.join(dataset.get('tags', ['N/A']))
        downloads = dataset.get('downloads', 'N/A')
        stars = dataset.get('stars', 'N/A')
        description = dataset.get('description', 'N/A')

        return f"""
{'='*80}
Name:        {name}
Category:    {category}
Platform:    {platform}
URL:         {url}
Languages:   {languages}
Tags:        {tags}
Downloads:   {downloads}
Stars:       {stars}
Description: {description}
{'='*80}
"""
    else:
        return f"- {name} ({platform})\n  URL: {url}"


def main():
    parser = argparse.ArgumentParser(
        description='Search DSFSI datasets registry',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python search_datasets.py --category speech
  python search_datasets.py --language zu --detailed
  python search_datasets.py --platform huggingface
  python search_datasets.py --tag nlp
  python search_datasets.py --query "machine translation"
  python search_datasets.py --featured
        """
    )

    parser.add_argument('--category', help='Filter by category (speech, text, terminology, etc.)')
    parser.add_argument('--language', help='Filter by language code (zu, en, tn, etc.)')
    parser.add_argument('--platform', help='Filter by platform (huggingface, github, zenodo, etc.)')
    parser.add_argument('--tag', help='Filter by tag')
    parser.add_argument('--query', help='Search by text query')
    parser.add_argument('--featured', action='store_true', help='Show only featured datasets')
    parser.add_argument('--detailed', action='store_true', help='Show detailed information')
    parser.add_argument('--list-categories', action='store_true', help='List all available categories')
    parser.add_argument('--list-languages', action='store_true', help='List all available languages')
    parser.add_argument('--list-platforms', action='store_true', help='List all available platforms')
    parser.add_argument('--stats', action='store_true', help='Show registry statistics')

    args = parser.parse_args()

    # Load registry
    registry = load_registry()

    # Handle special commands
    if args.list_categories:
        print("\nAvailable Categories:")
        for cat, desc in registry.get('categories', {}).items():
            print(f"  {cat}: {desc}")
        return

    if args.list_languages:
        print("\nAvailable Languages:")
        for code, name in registry.get('languages', {}).items():
            print(f"  {code}: {name}")
        return

    if args.list_platforms:
        print("\nAvailable Platforms:")
        for platform, url in registry.get('platforms', {}).items():
            print(f"  {platform}: {url}")
        return

    if args.stats:
        meta = registry.get('metadata', {})
        print("\nRegistry Statistics:")
        print(f"  Total Datasets: {meta.get('total_datasets', 'N/A')}")
        print(f"  Last Updated: {meta.get('last_updated', 'N/A')}")
        print(f"  Version: {meta.get('version', 'N/A')}")
        print(f"  Organization: {meta.get('organization', 'N/A')}")
        print(f"  Institution: {meta.get('institution', 'N/A')}")
        return

    # Get datasets
    if args.featured:
        datasets = registry.get('featured_datasets', [])
        print(f"\nFeatured Datasets ({len(datasets)}):")
    else:
        datasets = registry.get('datasets', [])

        # Apply filters
        if args.category:
            datasets = search_by_category(datasets, args.category)
            print(f"\nDatasets in category '{args.category}' ({len(datasets)}):")

        if args.language:
            datasets = search_by_language(datasets, args.language)
            print(f"\nDatasets with language '{args.language}' ({len(datasets)}):")

        if args.platform:
            datasets = search_by_platform(datasets, args.platform)
            print(f"\nDatasets on platform '{args.platform}' ({len(datasets)}):")

        if args.tag:
            datasets = search_by_tag(datasets, args.tag)
            print(f"\nDatasets with tag '{args.tag}' ({len(datasets)}):")

        if args.query:
            datasets = search_by_query(datasets, args.query)
            print(f"\nSearch results for '{args.query}' ({len(datasets)}):")

    # Display results
    if not datasets:
        print("No datasets found matching your criteria.")
        return

    for dataset in datasets:
        print(format_dataset(dataset, args.detailed))

    if not args.detailed:
        print(f"\nTotal: {len(datasets)} dataset(s)")
        print("\nUse --detailed flag for more information")


if __name__ == '__main__':
    main()
