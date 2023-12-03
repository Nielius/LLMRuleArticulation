import random
from functools import cache
from itertools import islice
from typing import Iterator

import nltk

from nltk.corpus import wordnet

from rule_articulation.ra_datasets.reuters_sentences import get_reuters_sentences
from rule_articulation.task_model import LabelledInput, RuleDataset


def ends_in_same_letter(sentence: str) -> bool:
    return sentence[0] == sentence[-1]


class StartEndLetterDataset(RuleDataset):
    """Label is True if the sentence ends in the same letter as it starts"""

    sentences_iterator: Iterator[str]

    def __init__(self):
        sentences = get_reuters_sentences(remove_punctuation=True, lower_case=True)
        random.shuffle(sentences)
        self.sentences = iter(sentences)

    def get_examples_with_label(self, labels: list[bool]) -> list[LabelledInput]:
        def next_sentence_iterator() -> Iterator[LabelledInput]:
            for label in labels:
                while True:
                    candidate = next(self.sentences)
                    if ends_in_same_letter(candidate) == label:
                        yield LabelledInput(
                            input=candidate,
                            label=label,
                        )
                        break

        return list(next_sentence_iterator())
