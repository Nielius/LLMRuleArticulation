import logging

import typer

from rule_articulation.evaluator import TaskEvaluator
from rule_articulation.tasks.capitalization import (
    CapitalizationDataset,
    capitalization_task_description,
)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


app = typer.Typer()


def get_openai_model(gpt4: bool):
    return "gpt-4-1106-preview" if gpt4 else "gpt-3.5-turbo-1106"


@app.command()
def eval(
    n: int = 10,
    seed: int = 42,
    gpt4: bool = typer.Option(False, "-4", "--gpt4", help="Use GPT-4 instead of GPT-3"),
):
    dataset = CapitalizationDataset()

    evaluation_report = TaskEvaluator(
        task=capitalization_task_description, openai_model=get_openai_model(gpt4)
    ).evaluate(dataset.sample(n))
    evaluation_report.print()


@app.command()
def articulate(
    gpt4: bool = typer.Option(False, "-4", "--gpt4", help="Use GPT-4 instead of GPT-3"),
):
    articulation = TaskEvaluator(
        task=capitalization_task_description, openai_model=get_openai_model(gpt4)
    ).ask_articulation()
    print("Articulation:", articulation)


if __name__ == "__main__":
    app()
