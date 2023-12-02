import logging

import typer

from rule_articulation.evaluator import TaskEvaluator
from rule_articulation.tasks.capitalization import (
    CapitalizationDataset,
    capitalization_task,
)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


app = typer.Typer()


@app.command()
def eval(n: int = 10, seed: int = 42):
    dataset = CapitalizationDataset()

    evaluation_report = TaskEvaluator().evaluate(capitalization_task, dataset.sample(n))
    evaluation_report.print()


@app.command()
def articulate():
    articulation = TaskEvaluator().ask_articulation(capitalization_task)
    print("Articulation:", articulation)


@app.command()
def something_else(name: str, formal: bool = False):
    raise NotImplementedError


if __name__ == "__main__":
    app()
