from rule_articulation.task_model import RuleArticulationTask
from rule_articulation.tasks.capitalization import capitalization_task
from rule_articulation.tasks.source_mixer import bible_vs_shakespeare_task

TASKS: dict[str, RuleArticulationTask] = {
    "bibleshakespeare": bible_vs_shakespeare_task,
    "capitalization": capitalization_task,
}