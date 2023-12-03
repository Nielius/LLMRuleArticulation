import re
from rule_articulation.ra_datasets.arithmetic import ArithmeticDataset
from rule_articulation.ra_datasets.gutenberg_sentences import get_gutenberg_sentences
from rule_articulation.ra_datasets.same_letter_wordlist import (
    StartEndLetterDataset,
    ends_in_same_letter,
)
from rule_articulation.ra_datasets.short_sentence_wordlist import ShortSentenceDataset
from rule_articulation.ra_datasets.source_mixer import SourceMixerDataset
from rule_articulation.ra_datasets.wordnet_wordlist import (
    PalindromeWordDataset,
    is_palindrome,
)
from rule_articulation.tasks.capitalization import CapitalizationDataset


def test_capitalization_dataset():
    labelled_inputs = CapitalizationDataset().sample(100)

    for labelled_input in labelled_inputs:
        assert labelled_input.label == any(
            char.isupper() for char in labelled_input.input
        )


def test_palindrome_dataset():
    labelled_inputs = PalindromeWordDataset().sample(100)

    for labelled_input in labelled_inputs:
        # we allow e.g. hyphens and capitals
        assert is_palindrome(labelled_input.input) == labelled_input.label
        assert len(labelled_input.input) > 1


def test_ends_in_same_letter_dataset():
    labelled_inputs = StartEndLetterDataset().sample(100)

    for labelled_input in labelled_inputs:
        assert ends_in_same_letter(labelled_input.input) == labelled_input.label


def test_short_sentence_dataset():
    dataset = ShortSentenceDataset()
    labelled_inputs = dataset.sample(100)

    for labelled_input in labelled_inputs:
        if labelled_input.label:
            assert len(labelled_input.input) < dataset.short_threshold
        else:
            assert len(labelled_input.input) > dataset.long_threshold


def test_source_mixer_dataset():
    source_1 = get_gutenberg_sentences("bible")[:200]
    source_2 = get_gutenberg_sentences("shakespeare")[:200]

    dataset = SourceMixerDataset(sources=(source_1, source_2))
    labelled_inputs = dataset.sample(100)

    source_1_set = set(source_1)
    source_2_set = set(source_2)
    for labelled_input in labelled_inputs:
        if labelled_input.label:
            assert labelled_input.input in source_1_set
        else:
            assert labelled_input.input in source_2_set


def test_arithmetic_dataset():
    dataset = ArithmeticDataset()
    labelled_inputs = dataset.sample(100)

    sum_re = re.compile(r"(\d+) \+ (\d+) = (\d+)")

    for labelled_input in labelled_inputs:
        match = sum_re.match(labelled_input.input)
        x, y, z = [int(s) for s in match.groups()]

        if labelled_input.label:
            assert x + y == z
        else:
            assert x + y != z
