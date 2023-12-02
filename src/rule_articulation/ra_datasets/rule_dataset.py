from abc import ABC, abstractmethod
import random

from rule_articulation.task_model import LabelledInput


class RuleDataset(ABC):
    @abstractmethod
    def get_examples_with_label(
        self, n: int, labels: list[bool]
    ) -> list[LabelledInput]:
        raise NotImplementedError()

    def sample(self, n: int, p_true: float = 0.5) -> list[LabelledInput]:
        return self.get_examples_with_label(
            n, [random.random() < p_true for _ in range(n)]
        )


