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
def capitalization(n: int = 10, seed: int = 42):
    dataset = CapitalizationDataset()

    evaluation_report = TaskEvaluator().evaluate(capitalization_task, dataset.sample(n))
    evaluation_report.print()


if __name__ == "__main__":
    app()
