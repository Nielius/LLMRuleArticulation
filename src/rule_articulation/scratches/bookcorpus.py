from datasets import load_dataset_builder, get_dataset_split_names, load_dataset, get_dataset_config_names

# worth considerign: https://huggingface.co/datasets/wikitext

ds_builder = load_dataset_builder("rotten_tomatoes")

ds_loaded = load_dataset("bookcorpus")

get_dataset_config_names("wikimedia/wikipedia")

get_dataset_split_names("bookcorpus")

ds_loaded = load_dataset("bookcorpus", split="train")

ds_loaded["text"]

ds_loaded[100]

ds_loaded[3000000]

get_dataset_split_names("rotten_tomatoes")

get_dataset_config_names("bookcorpus")

ds_builder.info.features

# Inspect dataset description
ds_builder.info.description
Movie Review Dataset. This is a dataset of containing 5,331 positive and 5,331 negative processed sentences from Rotten Tomatoes movie reviews. This data was first used in Bo Pang and Lillian Lee, ``Seeing stars: Exploiting class relationships for sentiment categorization with respect to rating scales.'', Proceedings of the ACL, 2005.

# Inspect dataset features
ds_builder.info.features
{'label': ClassLabel(num_classes=2, names=['neg', 'pos'], id=None),
 'text': Value(dtype='string', id=None)}
