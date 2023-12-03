import random
from typing import Iterator

from rule_articulation.ra_datasets.gutenberg_sentences import get_gutenberg_sentences
from rule_articulation.task_model import LabelledInput, RuleDataset


class SourceMixerDataset(RuleDataset):
    source_1: Iterator[str]
    source_2: Iterator[str]

    def __init__(self, sources: tuple[list[str], list[str]] | None = None):
        source_1, source_2 = sources or (
            get_gutenberg_sentences("bible"),
            get_gutenberg_sentences("shakespeare"),
        )
        assert source_1
        assert source_2
        random.shuffle(source_1)
        random.shuffle(source_2)
        self.source_1 = iter(source_1)
        self.source_2 = iter(source_2)

    def get_examples_with_label(self, labels: list[bool]) -> list[LabelledInput]:
        def example_iterator() -> Iterator[LabelledInput]:
            for label in labels:
                yield LabelledInput(
                    input=next(self.source_1) if label else next(self.source_2),
                    label=label,
                )

        return list(example_iterator())
