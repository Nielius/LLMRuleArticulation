# CAREFUL!
# Running all of these takes a lot of time and not an insignificant amount of dollars

python src/rule_articulation/full_experiment.py with task=arithmetic       num_test_examples=30 num_articulations=10
python src/rule_articulation/full_experiment.py with task=bibleshakespeare num_test_examples=30 num_articulations=10
python src/rule_articulation/full_experiment.py with task=capitalization   num_test_examples=30 num_articulations=10
python src/rule_articulation/full_experiment.py with task=palindrome       num_test_examples=30 num_articulations=10
python src/rule_articulation/full_experiment.py with task=sameletter       num_test_examples=30 num_articulations=10
python src/rule_articulation/full_experiment.py with task=shortsentence    num_test_examples=30 num_articulations=10


python src/rule_articulation/full_experiment.py with gpt4=true task=arithmetic        num_test_examples=30 num_articulations=10
python src/rule_articulation/full_experiment.py with gpt4=true task=bibleshakespeare  num_test_examples=30 num_articulations=10
python src/rule_articulation/full_experiment.py with gpt4=true task=capitalization    num_test_examples=30 num_articulations=10
python src/rule_articulation/full_experiment.py with gpt4=true task=palindrome        num_test_examples=30 num_articulations=10
python src/rule_articulation/full_experiment.py with gpt4=true task=sameletter        num_test_examples=30 num_articulations=10
python src/rule_articulation/full_experiment.py with gpt4=true task=shortsentence     num_test_examples=30 num_articulations=10
