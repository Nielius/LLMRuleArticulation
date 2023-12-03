from rule_articulation.ra_datasets.arithmetic import ArithmeticDataset
from rule_articulation.task_model import (
    RuleArticulationTask,
    TaskDescription,
    LabelledInput,
)

arithmetic_task = RuleArticulationTask(
    description=TaskDescription(
        human_articulation="Return true if the word is a palindrome",
        example_labelled_inputs=[
            LabelledInput(input="19 + 15 = 34", label=True),
            LabelledInput(input="19 + 10 = 26", label=False),
            LabelledInput(input="1 + 6 = 27", label=False),
            LabelledInput(input="17 + 8 = 25", label=True),
            LabelledInput(input="11 + 18 = 29", label=True),
            LabelledInput(input="17 + 14 = 1", label=False),
            LabelledInput(input="1 + 7 = 14", label=False),
            LabelledInput(input="20 + 16 = 36", label=True),
            LabelledInput(input="19 + 10 = 29", label=True),
        ],
    ),
    get_dataset=lambda: ArithmeticDataset(),
)
