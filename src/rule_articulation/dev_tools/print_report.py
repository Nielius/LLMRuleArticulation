"""
Tool to create the sample inputs in the TaskDescription
"""
import json
from dataclasses import asdict

import typer

from rule_articulation.task_model import LabelledInput
from rule_articulation.utils import get_task, get_experiment_results_path

app = typer.Typer()


@app.command(name="print")
def print_report(experiment_number: int) -> None:
    path = get_experiment_results_path(experiment_number)
    print(path)

    with open(path / "info.json", "r") as f:
        d = json.load(f)

    fraction_correct = d["fraction_correct"]
    if fraction_correct < 0.9:
        print("WARNING: RULE HAS NOT BEEN LEARNT PROPERLY")

    print("Fraction correct:", d["fraction_correct"])
    print("------------------------------------------")
    for i, articulation in enumerate(d["articulation"]):
        print(f"\n\n------------------ ARTICULATION {i + 1} -----------------------\n\n")
        print(articulation)
