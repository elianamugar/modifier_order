# Modifier Order Finder

A Python NLP tool for finding consecutive adjective sequences in NLTK corpus texts.

## Overview

This project searches corpus texts for sequences of two or more consecutive adjectives. It was designed as an exploratory linguistics/NLP project for studying modifier order: how multiple adjectives appear before a noun or within descriptive phrases.

For example, a phrase like "long dark road" contains a sequence of consecutive modifiers that may reflect patterns in adjective ordering.

## Features

- Lets the user choose an NLTK corpus
- Lets the user choose a file from that corpus
- Tokenizes and POS-tags the selected text
- Finds sequences of two or more consecutive adjectives
- Exports each sequence with surrounding context

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```
Download required NLTK data:
```python
import nltk

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("brown")
nltk.download("gutenberg")
nltk.download("inaugural")
nltk.download("reuters")
nltk.download("webtext")
```
## How to Run
```bash
python modifier_order_finder.py
```
### Example Output
```
Modifier Order Analysis
=======================
Corpus: gutenberg
File: austen-emma.txt
Consecutive adjective sequences found: 12

she saw a [long narrow] path leading toward
```
## Skills Demonstrated
* Python scripting
* Natural language processing
* Corpus linguistics
* Part-of-speech tagging
* Pattern extraction
* Modifier/order analysis

## Limitations
This project depends on NLTK POS tagging, so adjective sequences may not always be identified perfectly. Some modifier sequences may be missed if a word is tagged incorrectly or if punctuation interrupts the phrase.

## Future Improvements
* Export results as CSV
* Include the following noun after each adjective sequence
* Count most common adjective bigrams
* Compare modifier order patterns across authors
* Add command-line arguments
* Add visualization of adjective sequence frequency
