from rule_articulation.task_model import RuleArticulationTask
from rule_articulation.tasks import TASKS


def get_openai_model(gpt4: bool):
    return "gpt-4-1106-preview" if gpt4 else "gpt-3.5-turbo-1106"


def get_task(task: str) -> RuleArticulationTask:
    try:
        return TASKS[task]
    except KeyError:
        raise ValueError(f"Unknown task {task}")
