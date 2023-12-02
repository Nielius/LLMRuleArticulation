from rule_articulation.tasks.capitalization import CapitalizationDataset


def test_capitalization_dataset():
    result = CapitalizationDataset().sample(10)

    print(result)