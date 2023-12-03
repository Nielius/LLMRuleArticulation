import random

from rule_articulation.task_model import LabelledInput, RuleDataset

random.randint(1, 20)


class ArithmeticDataset(RuleDataset):
    """Simple addition. True if the sum is correct."""

    max_num: int = 20

    def get_examples_with_label(self, labels: list[bool]) -> list[LabelledInput]:
        def get_incorrect_sum() -> tuple[int, int, int]:
            a = random.randint(0, self.max_num)
            b = random.randint(0, self.max_num)
            c = random.randint(0, 2 * self.max_num)

            while c == a + b:
                c = random.randint(0, 10)

            return a, b, c

        def get_correct_sum() -> tuple[int, int, int]:
            a = random.randint(0, self.max_num)
            b = random.randint(0, self.max_num)
            c = a + b

            return a, b, c

        def format_sum(a: int, b: int, c: int) -> str:
            return f"{a} + {b} = {c}"

        return [
            LabelledInput(
                input=format_sum(*get_correct_sum())
                if label
                else format_sum(*get_incorrect_sum()),
                label=label,
            )
            for label in labels
        ]
