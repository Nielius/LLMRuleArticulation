# Rule articulation -- research exercise

A short 2-day project to investigate whether LLMs can formulate rules
they have learnt in-context.

Some pointers to get started with this repo:

- the results to experiments are stored in `experiments/results`
- see the examples below for how to run experiments
- it's very easy to add new rules; see `src/rule_articulation/tasks/arithmetic.py` for an example

## Usage

- Install dependencies with `poetry install`.
- Create a file `src/rule_articulation/secrets/.openai-key.json` containing your openai key. It should look like this:

```json
{
  "organization": "org-XXXXX",
  "api_key": "sk-XXXXX"
}
```

Examples:

```
# First activate a subshell with the right environment
poetry shell

python src/rule_articulation/full_experiment.py with gpt4=True task=capitalization

python src/rule_articulation/main.py eval bibleshakespeare
python src/rule_articulation/main.py eval -4 bibleshakespeare
python src/rule_articulation/main.py articulate -4 bibleshakespeare


# When you run a full experiment, the results are stored in `experiments/results/<experiment_number>`
# You can print a small report using

python src/rule_articulation/main.py report print <experiment_number>

# see ./run-all-experiments.sh to see which experiments ended up in the TeX report
```
