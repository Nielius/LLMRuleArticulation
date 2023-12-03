from functools import cache
from typing import Iterator

import nltk

from nltk.corpus import reuters

from rule_articulation.ra_datasets.sentence_sanitizer import sanitized_sentences


@cache
def get_reuters_sentences(
    exclude_headlines: bool = True,
    exclude_short_and_long_sentences: bool = True,
    remove_punctuation: bool = False,
    lower_case: bool = False,
) -> list[str]:
    # returning a list is better for caching
    return list(
        _get_reuters_iterator(
            exclude_headlines=exclude_headlines,
            exclude_short_and_long_sentences=exclude_short_and_long_sentences,
            remove_punctuation=remove_punctuation,
            lower_case=lower_case,
        )
    )


def _get_reuters_iterator(
    exclude_headlines: bool = True,
    exclude_short_and_long_sentences: bool = True,
    remove_punctuation: bool = False,
    lower_case: bool = False,
) -> Iterator[str]:
    nltk.download("reuters")

    yield from sanitized_sentences(
        raw_text=reuters.raw(),
        exclude_headlines=exclude_headlines,
        exclude_short_and_long_sentences=exclude_short_and_long_sentences,
        remove_punctuation=remove_punctuation,
        lower_case=lower_case,
    )
