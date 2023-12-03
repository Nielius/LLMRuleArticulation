import random
from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property
from typing import Callable


@dataclass
class LabelledInput:
    input: str
    label: bool


def format_labelled_input(input: str, label: bool | str) -> str:
    return f'Input: "{input}"\nLabel: {label}'


class RuleDataset(ABC):
    @abstractmethod
    def get_examples_with_label(self, labels: list[bool]) -> list[LabelledInput]:
        raise NotImplementedError()

    def sample(self, n: int, p_true: float = 0.5) -> list[LabelledInput]:
        return self.get_examples_with_label(
            [random.random() < p_true for _ in range(n)]
        )


@dataclass
class TaskDescription:
    human_articulation: str
    example_labelled_inputs: list[LabelledInput]
    prompt_preamble: str = """You are a precise classifier, and you need to respond with a JSON object that is either
'{"label": true}' or '{"label": false}'.

Below, you are given a list of sentences, each labelled as true or false.
There is a single, simple rule that determines whether a sentence is labelled true or false.
Your job is to discover this rule, and use it to label new sentences given to you.

These are the example sentences:

"""

    def get_system_prompt(self) -> str:
        return (
            self.prompt_preamble
            + "\n\n".join(
                [
                    format_labelled_input(labelled_input.input, labelled_input.label)
                    for labelled_input in self.example_labelled_inputs
                ]
            )
            + "\n\n---\n\nNow do the same for any new sentences provided to you.\n\n"
        )


@dataclass
class RuleArticulationTask:
    description: TaskDescription
    get_dataset: Callable[[], RuleDataset]

    @cached_property
    def dataset(self) -> RuleDataset:
        return self.get_dataset()
