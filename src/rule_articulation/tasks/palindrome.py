from rule_articulation.ra_datasets.wordnet_wordlist import PalindromeWordDataset
from rule_articulation.task_model import (
    RuleArticulationTask,
    TaskDescription,
    LabelledInput,
)

palindrome_task = RuleArticulationTask(
    description=TaskDescription(
        human_articulation="Return true if the word is a palindrome",
        example_labelled_inputs=[
            LabelledInput(input="sexes", label=True),
            LabelledInput(input="sexy", label=False),
            LabelledInput(input="racecar", label=True),
            LabelledInput(input="racecat", label=False),
            LabelledInput(input="egarage", label=True),
            LabelledInput(input="garage", label=False),
            LabelledInput(input="qaanaaq", label=True),
            LabelledInput(input="downplay", label=False),
        ],
    ),
    get_dataset=lambda: PalindromeWordDataset(),
)
