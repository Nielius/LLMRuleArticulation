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
        info = json.load(f)

    with open(path / "config.json", "r") as f:
        config = json.load(f)

    print("------------------------------------------")
    for i, articulation in enumerate(info["articulation"]):
        print(f"\n\n------------------ ARTICULATION {i + 1} -----------------------\n\n")
        print(articulation)

    print("------------------------------------------")
    print("Config:")
    print(f"{config['task']=}")
    print(f"{config['gpt4']=}")
    fraction_correct = info["fraction_correct"]
    if fraction_correct < 0.9:
        print("WARNING: RULE HAS NOT BEEN LEARNT PROPERLY")
    print("Fraction correct:", info["fraction_correct"])
