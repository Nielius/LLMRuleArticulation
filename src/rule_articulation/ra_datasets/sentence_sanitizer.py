import re
from typing import Iterator

import nltk

excess_space_re = re.compile(r"\s+")


def sanitized_sentences(
    raw_text: str,
    exclude_headlines: bool = True,
    exclude_short_and_long_sentences: bool = True,
    remove_punctuation: bool = False,
    lower_case: bool = False,
) -> Iterator[str]:
    for sentence in nltk.sent_tokenize(raw_text):
        if exclude_headlines and is_headline(sentence):
            continue

        if exclude_short_and_long_sentences and not (40 < len(sentence) < 180):
            continue

        if remove_punctuation:
            sentence = "".join(
                [char for char in sentence if char.isalnum() or char == " "]
            )

        if lower_case:
            sentence = sentence.lower()

        sentence = excess_space_re.sub(" ", sentence)

        yield sentence


def is_headline(sentence):
    return sentence[:7].isupper()
