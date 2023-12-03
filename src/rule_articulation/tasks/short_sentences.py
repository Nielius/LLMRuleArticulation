from rule_articulation.ra_datasets.short_sentence_wordlist import ShortSentenceDataset
from rule_articulation.task_model import LabelledInput, RuleArticulationTask, TaskDescription

short_sentence_task = RuleArticulationTask(
    description=TaskDescription(
        human_articulation="Return true if the sentence is short, false otherwise.",
        example_labelled_inputs=[
            LabelledInput(input="The agreement calls for drilling.", label=True),
            LabelledInput(
                input="The agreement calls for drilling of 10 to 12 offshore wells  per year, primarily in the Gulf of Mexico area off the Texas  and Louisiana coasts and 30 to 40 onshore Texas and Louisiana  Gulf Coast wells.",
                label=False,
            ),
            LabelledInput(
                input="It quoted a spokesman for the China National Offshore Oil  Corp (CNOOC) as saying China signed eight contracts with 15  foreign firms for blocks in the Pearl River mouth and south  Yellow Sea covering a total area of 44,913 sq km.",
                label=False,
            ),
            LabelledInput(input="China signed eight contracts", label=True),
            LabelledInput(
                input='For the week as a whole, he said that float related as of  adjustments were "small," adding that they fell to a negative  750 mln dlrs on Tuesday due to a number of corrections for  unrelated cash letter errors in six districts around the  country.',
                label=False,
            ),
            LabelledInput(input="Employers groups also want change.", label=True),
            LabelledInput(input="Polaroid rose 1-1/8 to 74-1/2.", label=True),
        ]
    ),
    get_dataset=lambda: ShortSentenceDataset(),
)

