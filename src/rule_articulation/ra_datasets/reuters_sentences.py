from functools import cache
from typing import Iterator

import nltk

from nltk.corpus import reuters


@cache
def get_reuters_sentences(
    exclude_headlines: bool = True,
    remove_punctuation: bool = False,
    lower_case: bool = False,
) -> list[str]:
    # returning a list is better for caching
    return list(
        _get_reuters_iterator(
            exclude_headlines=exclude_headlines,
            remove_punctuation=remove_punctuation,
            lower_case=lower_case,
        )
    )


def _get_reuters_iterator(
    exclude_headlines: bool = True,
    remove_punctuation: bool = False,
    lower_case: bool = False,
) -> Iterator[str]:
    nltk.download("reuters")

    def is_headline(sentence):
        return sentence[:7].isupper()

    for sentence in nltk.sent_tokenize(reuters.raw()):
        if exclude_headlines and is_headline(sentence):
            continue

        if not(40 < len(sentence) < 180):
            continue

        if remove_punctuation:
            sentence = "".join(
                [char for char in sentence if char.isalnum() or char == " "]
            )

        if lower_case:
            sentence = sentence.lower()

        yield sentence.replace("\n", "")
