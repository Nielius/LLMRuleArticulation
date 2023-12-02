from rule_articulation.ra_datasets.same_letter_wordlist import (
    StartEndLetterDataset,
    ends_in_same_letter,
)
from rule_articulation.ra_datasets.short_sentence_wordlist import ShortSentenceDataset
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
