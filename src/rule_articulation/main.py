import logging
from typing import Annotated

import typer

import rule_articulation.dev_tools.sample_input as sample_input
import rule_articulation.dev_tools.print_report as print_report
from rule_articulation.evaluator import TaskEvaluator
from rule_articulation.utils import get_openai_model, get_task, set_default_log_settings

logger = logging.getLogger(__name__)
set_default_log_settings()


app = typer.Typer()
app.add_typer(sample_input.app, name="sample-input")
app.add_typer(print_report.app, name="report")


@app.command()
def eval(
    task: Annotated[str, typer.Argument()] = "capitalization",
    n: int = 10,
    seed: int = 42, # TODO: I never implemented this
    gpt4: bool = typer.Option(False, "-4", "--gpt4", help="Use GPT-4 instead of GPT-3"),
):
    task = get_task(task)

    evaluation_report = TaskEvaluator(
        task=task.description, openai_model=get_openai_model(gpt4)
    ).evaluate(task.dataset.sample(n))

    evaluation_report.print()


@app.command()
def articulate(
    task: Annotated[str, typer.Argument()] = "capitalization",
    gpt4: bool = typer.Option(False, "-4", "--gpt4", help="Use GPT-4 instead of GPT-3"),
):
    task = get_task(task)

    articulation = TaskEvaluator(
        task=task.description, openai_model=get_openai_model(gpt4)
    ).ask_articulation()
    print("Articulation:", articulation)


if __name__ == "__main__":
    app()
