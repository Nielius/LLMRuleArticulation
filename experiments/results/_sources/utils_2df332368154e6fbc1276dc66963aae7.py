import logging
from pathlib import Path

from rule_articulation.task_model import RuleArticulationTask
from rule_articulation.tasks import TASKS


def set_default_log_settings():
    logging.basicConfig(level=logging.DEBUG)


def get_openai_model(gpt4: bool):
    return "gpt-4-1106-preview" if gpt4 else "gpt-3.5-turbo-1106"


def get_task(task: str) -> RuleArticulationTask:
    try:
        return TASKS[task]
    except KeyError:
        raise ValueError(f"Unknown task {task}")


def get_experiment_results_path(experiment_number: int) -> Path:
    return (
        Path(__file__).parent.parent.parent
        / "experiments"
        / "results"
        / str(experiment_number)
    )
