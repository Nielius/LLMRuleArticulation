# Rule articulation -- research exercise

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
```
