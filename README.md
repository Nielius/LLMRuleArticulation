# Rule articulation -- research exercise


## Usage

- `.openai-key.json` should look something like

```json
{
  "organization": "org-XXXXX",
  "api_key": "sk-XXXXX"
}
```


Examples:


```
python src/rule_articulation/full_experiment.py with gpt4=True task=capitalization

python src/rule_articulation/main.py eval bibleshakespeare
python src/rule_articulation/main.py eval -4 bibleshakespeare
python src/rule_articulation/main.py articulate -4 bibleshakespeare

```
