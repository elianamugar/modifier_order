"""
Find consecutive adjective sequences in NLTK corpus texts.

This script searches a selected NLTK corpus text for strings of two or more
consecutive adjectives, then exports each sequence with surrounding context.
"""

from pathlib import Path

import nltk
from nltk.corpus import brown, gutenberg, inaugural, reuters, webtext


CORPORA = {
    "brown": brown,
    "gutenberg": gutenberg,
    "inaugural": inaugural,
    "reuters": reuters,
    "webtext": webtext,
}

ADJECTIVE_TAGS = {"JJ", "JJR", "JJS"}
EXCLUDED_WORDS = {"such"}


def choose_corpus():
    """Prompt the user to choose an available corpus."""
    print("Available corpora:")
    for name in CORPORA:
        print(f"- {name}")

    while True:
        choice = input("\nChoose a corpus: ").strip().lower()
        if choice in CORPORA:
            return choice, CORPORA[choice]

        print("Invalid corpus. Please choose one from the list.")


def choose_file(corpus):
    """Prompt the user to choose a file from the selected corpus."""
    file_ids = corpus.fileids()

    print("\nAvailable files:")
    for file_id in file_ids[:25]:
        print(f"- {file_id}")

    if len(file_ids) > 25:
        print(f"...and {len(file_ids) - 25} more")

    while True:
        choice = input("\nChoose a file ID: ").strip()
        if choice in file_ids:
            return choice

        print("Invalid file ID. Please copy one exactly from the list.")


def is_adjective(token_tag_pair):
    """Return True if a tagged token is an adjective."""
    word, tag = token_tag_pair
    return tag in ADJECTIVE_TAGS and word.lower() not in EXCLUDED_WORDS


def find_adjective_sequences(tagged_tokens, context_size=6):
    """Find consecutive adjective sequences with surrounding context."""
    sequences = []
    index = 0

    while index < len(tagged_tokens):
        if not is_adjective(tagged_tokens[index]):
            index += 1
            continue

        start = index
        adjectives = []

        while index < len(tagged_tokens) and is_adjective(tagged_tokens[index]):
            adjectives.append(tagged_tokens[index][0])
            index += 1

        end = index - 1

        if len(adjectives) >= 2:
            before = tagged_tokens[max(0, start - context_size):start]
            after = tagged_tokens[end + 1:end + 1 + context_size]

            sequences.append(
                {
                    "adjectives": adjectives,
                    "before": [word for word, _ in before],
                    "after": [word for word, _ in after],
                }
            )

    return sequences


def format_sequence(sequence):
    """Format one adjective sequence with context."""
    before = " ".join(sequence["before"])
    adjectives = " ".join(sequence["adjectives"])
    after = " ".join(sequence["after"])

    return f"{before} [{adjectives}] {after}".strip()


def format_results(corpus_name, file_id, sequences):
    """Format all modifier-order results."""
    lines = [
        "Modifier Order Analysis",
        "=======================",
        f"Corpus: {corpus_name}",
        f"File: {file_id}",
        f"Consecutive adjective sequences found: {len(sequences)}",
        "",
    ]

    for sequence in sequences:
        lines.append(format_sequence(sequence))
        lines.append("")

    return "\n".join(lines)


def main():
    """Run the modifier order finder."""
    corpus_name, corpus = choose_corpus()
    file_id = choose_file(corpus)

    text = corpus.raw(file_id)
    tokens = nltk.word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)

    sequences = find_adjective_sequences(tagged_tokens)

    output_path = Path(
        input("\nEnter output filename, e.g. modifier_order_results.txt: ").strip()
    )

    results = format_results(corpus_name, file_id, sequences)
    output_path.write_text(results, encoding="utf-8")

    print(f"\nFound {len(sequences)} adjective sequences.")
    print(f"Saved results to {output_path}")


if __name__ == "__main__":
    main()
