import random
from typing import Iterator

from rule_articulation.ra_datasets.reuters_sentences import get_reuters_sentences
from rule_articulation.task_model import LabelledInput, RuleDataset


class ShortSentenceDataset(RuleDataset):
    """Returns sentences that are either very long (> 200 chars) (for False) or very short (< 40 chars) (for True)."""

    sentences_iterator: Iterator[str]
    short_threshold: int = 40
    long_threshold: int = 200

    def __init__(self):
        sentences = get_reuters_sentences(exclude_short_and_long_sentences=False)
        random.shuffle(sentences)
        self.sentences = iter(sentences)

    def get_examples_with_label(self, labels: list[bool]) -> list[LabelledInput]:
        def next_sentence_iterator() -> Iterator[LabelledInput]:
            for label in labels:
                if label:
                    # need short
                    while True:
                        candidate = next(self.sentences)
                        if len(candidate) < self.short_threshold:
                            yield LabelledInput(
                                input=candidate,
                                label=label,
                            )
                            break
                else:
                    # need long
                    while True:
                        candidate = next(self.sentences)
                        if len(candidate) > self.long_threshold:
                            yield LabelledInput(
                                input=candidate,
                                label=label,
                            )
                            break

        return list(next_sentence_iterator())
