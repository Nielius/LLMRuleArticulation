"""
Tool to create the sample inputs in the TaskDescription
"""
import json
from dataclasses import asdict

import typer

from rule_articulation.task_model import LabelledInput
from rule_articulation.utils import get_task

app = typer.Typer()


@app.command(name="dump")
def dump_true_false_samples_in_json_file(task: str) -> None:
    dataset = get_task(task).dataset  # REPLACE ME with the dataset you want to use

    sample = dataset.sample(100)
    falses = [s for s in sample if not s.label]
    trueses = [s for s in sample if s.label]

    with open("sample_dump.json", "w") as f:
        json.dump([asdict(s) for s in trueses + falses], f, indent=2)

    print("Dumped to sample_dump.json")


@app.command(name="load")
def load_true_false_samples_from_json_file() -> list[LabelledInput]:
    with open("sample_dump.json", "r") as f:
        d = json.load(f)

    loaded_inputs = [LabelledInput(**s) for s in d]
    print(loaded_inputs)
    return loaded_inputs
