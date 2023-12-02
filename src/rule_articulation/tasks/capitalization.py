import random

from rule_articulation.ra_datasets.reuters_sentences import get_reuters_sentences
from rule_articulation.ra_datasets.rule_dataset import RuleDataset
from rule_articulation.using_openai_directly import LabelledInput, TaskDescription

dataset = get_reuters_sentences()


def introduce_random_capitalization(sentence: str) -> str:
    """Introduce random capitalization to a sentence.
    I want to be able to explicitly set the number of capital letters."""

    attempt = 0
    while attempt < 10:
        result = "".join(
            [
                char.upper() if char.isalpha() and random.random() < 0.2 else char
                for char in sentence
            ]
        )
        if any(char.isupper() for char in result):
            return result
        attempt += 1

    # If I have time I might make a better algorithm, but this should basically always work
    raise ValueError(
        f"Could not introduce capitalization in 10 attempts to string {sentence}"
    )


class CapitalizationDataset(RuleDataset):
    sentences: list[str]

    def __init__(self):
        self.sentences = get_reuters_sentences()

    def get_examples_with_label(
        self, n: int, labels: list[bool]
    ) -> list[LabelledInput]:
        return [
            LabelledInput(
                input=introduce_random_capitalization(sentence)
                if label
                else sentence.lower(),
                label=label,
            )
            for sentence, label in zip(random.sample(self.sentences, k=n), labels)
        ]


capitalization_task = TaskDescription(
    labelled_inputs=[
        LabelledInput("the cat sat on the mat", True),
        LabelledInput("THE DOG RAN IN THE PARK", False),
        LabelledInput("THE mat sat on the cat", False),
        LabelledInput("the house is cold", True),
    ] + [
        LabelledInput(
            input="gasoline prices rose 4.2 pct last month after increasing  6.6 pct in january, but were still 18 pct below levels of a  year ago, the department said.",
            label=False,
        ),
        LabelledInput(
            input="Gelco ExprEss LTd was one of  tHE compAniEs schedulEd FoR divestitUre.",
            label=True,
        ),
        LabelledInput(
            input="ExporTs aRe ForEcaSt to increase To 1.0 mlN tonnes froM  800,000 tonnEs ExPorteD lasT Year, The reporT said.",
            label=True,
        ),
        LabelledInput(
            input="The cRiminal caSe settlemEnt disMisses all chargeS  incluDIng BriBery and FalsE staTement, exCept foR cOnspiracy to  wHich ParadYNe pleadEd guilty.",
            label=True,
        ),
        LabelledInput(
            input="THe JuNe inTErim suRplus compAres wIth A 1.76 bilLion DlR  surpLus in thE same MaY periOd.",
            label=True,
        ),
        LabelledInput(
            input='"I thinK (NAkasone\'s) deSPerate," saId a U.S. Bank foreign  EXchange manager.',
            label=True,
        ),
        LabelledInput(
            input='"we consider the interest rate increase that has occurred  here and internationally to be a problem and cause for concern,"  poehl told an investment conference.',
            label=False,
        ),
        LabelledInput(
            input="baker was optimistic about brazil, which has stopped  interest payments on much of its outstanding debt with foreign  commercial banks.",
            label=False,
        ),
        LabelledInput(
            input="harper said the board has previously expressed a strong  determination to remain an independent publishing enterprise.",
            label=False,
        ),
        LabelledInput(
            input="ThE CompAny said parT of tHe agreemEnt Includes payment of  up to an adDitional 6.5 mln dlrs bAsed oN THe PerforMance of  The unit in thE year fOllowINg the CloSiNg.",
            label=True,
        ),
    ]
)
