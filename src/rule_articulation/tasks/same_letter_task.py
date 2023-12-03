from rule_articulation.ra_datasets.same_letter_wordlist import StartEndLetterDataset
from rule_articulation.task_model import (
    RuleArticulationTask,
    TaskDescription,
    LabelledInput,
)

same_letter_task = RuleArticulationTask(
    description=TaskDescription(
        human_articulation="Return true if the sentence starts and ends with the same letter",
        example_labelled_inputs=[
            LabelledInput(
                input="xenophobic patissiers make tasteless gateaux", label=True
            ),
            LabelledInput(
                input="xenophobic patissiers make tasteless cakes", label=False
            ),
            LabelledInput(
                input="quite a lot of people know the french word for five is cinq",
                label=True,
            ),
            LabelledInput(
                input="quite a lot of people know the french word for four is quatre",
                label=False,
            ),
            LabelledInput(
                input="this compares with the previous januarys 139 pct", label=True
            ),
            LabelledInput(
                input="this compares with the previous januarys 139 payroll cost tranfer",
                label=False,
            ),
            LabelledInput(
                input="no other details were disclosed about the amount of millipores investment in protein",
                label=True,
            ),
            LabelledInput(
                input="no interest will accrue or will be payable on the debentures starting may 18 the computer and communications company said",
                label=False,
            ),
        ],
    ),
    get_dataset=lambda: StartEndLetterDataset(),
)
