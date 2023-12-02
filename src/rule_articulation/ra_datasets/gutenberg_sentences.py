import re
import urllib.request
from functools import cache
from importlib.resources import files
from pathlib import Path
from typing import Iterator


import rule_articulation
from rule_articulation.ra_datasets.sentence_sanitizer import sanitized_sentences

sources = {
    "bible": "https://www.gutenberg.org/ebooks/10.txt.utf-8",
    "shakespeare": "https://www.gutenberg.org/ebooks/100.txt.utf-8",
}


@cache
def get_gutenberg_sentences(
    source: str,
    exclude_headlines: bool = True,
    exclude_short_and_long_sentences: bool = True,
    remove_punctuation: bool = False,
    lower_case: bool = False,
) -> list[str]:
    if source not in sources:
        raise ValueError(f"source must be one of {sources.keys()}")

    # returning a list is better for caching
    return list(
        _get_gutenberg_iterator(
            source=source,
            exclude_headlines=exclude_headlines,
            exclude_short_and_long_sentences=exclude_short_and_long_sentences,
            remove_punctuation=remove_punctuation,
            lower_case=lower_case,
        )
    )


def load_source(source: str) -> str:
    path = download_if_necessary(source)
    return path.read_text()


def download_if_necessary(source: str) -> Path:
    download_path = (
        Path(files(rule_articulation)).parent.parent / "downloads" / "datasets"
    )
    download_path.mkdir(parents=True, exist_ok=True)

    target_path = download_path / f"{source}.txt"
    print(target_path)

    if not target_path.exists() or target_path.stat().st_size == 0:
        print(f"Downloading {source}...")
        urllib.request.urlretrieve(sources[source], target_path)

    return target_path


bible_verse_regex = re.compile(r"^\d+:\d+ ")
shakespeare_line_no_regex = re.compile(r"^\d+ ")


def _get_gutenberg_iterator(
    source: str,
    exclude_headlines: bool = True,
    exclude_short_and_long_sentences: bool = True,
    remove_punctuation: bool = False,
    lower_case: bool = False,
) -> Iterator[str]:
    if source == "bible":
        # want to do some post-processing, to remove the verse numbers
        for sentence in sanitized_sentences(
            load_source(source),
            exclude_headlines=exclude_headlines,
            exclude_short_and_long_sentences=exclude_short_and_long_sentences,
            remove_punctuation=remove_punctuation,
            lower_case=lower_case,
        ):
            yield bible_verse_regex.sub("", sentence)
    elif source == "shakespeare":
        for sentence in sanitized_sentences(
            load_source(source),
            exclude_headlines=exclude_headlines,
            exclude_short_and_long_sentences=exclude_short_and_long_sentences,
            remove_punctuation=remove_punctuation,
            lower_case=lower_case,
        ):
            yield shakespeare_line_no_regex.sub("", sentence)
    else:
        yield from sanitized_sentences(
            load_source(source),
            exclude_headlines=exclude_headlines,
            exclude_short_and_long_sentences=exclude_short_and_long_sentences,
            remove_punctuation=remove_punctuation,
            lower_case=lower_case,
        )
