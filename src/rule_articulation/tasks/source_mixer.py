from rule_articulation.ra_datasets.gutenberg_sentences import get_gutenberg_sentences
from rule_articulation.ra_datasets.source_mixer import SourceMixerDataset
from rule_articulation.task_model import (
    LabelledInput,
    TaskDescription,
    RuleArticulationTask,
)

bible_vs_shakespeare_task = RuleArticulationTask(
    description=(
        TaskDescription(
            human_articulation="Return true if the sentence is from the Bible, false if it is from Shakespeare.",
            example_labelled_inputs=[
                LabelledInput(
                    input="And God said, Let there be light: and there was light.",
                    label=True,
                ),
                LabelledInput(
                    input="To be, or not to be, that is the question.", label=False
                ),
                LabelledInput(
                    input="After this manner therefore pray ye: Our Father which art in heaven, Hallowed be thy name.",
                    label=True,
                ),
                LabelledInput(
                    input="If music be the food of love, play on, Give me excess of it; that, surfeiting, The appetite may sicken and so die.",
                    label=False,
                ),
                LabelledInput(
                    input="But seek ye first the kingdom of God, and his righteousness; and all these things shall be added unto you.",
                    label=True,
                ),
                LabelledInput(
                    input="Parting is such sweet sorrow That I shall say good night till it be morrow.",
                    label=False,
                ),
                LabelledInput(
                    input="And Jesus saith unto him, I will come and heal him.",
                    label=True,
                ),
                LabelledInput(
                    input="We are such stuff As dreams are made on, and our little life Is rounded with a sleep.",
                    label=False,
                ),
            ],
        )
    ),
    get_dataset=lambda: SourceMixerDataset(
        sources=(
            get_gutenberg_sentences("bible"),
            get_gutenberg_sentences("shakespeare"),
        )
    ),
)
