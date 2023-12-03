from rule_articulation.task_model import RuleArticulationTask
from rule_articulation.tasks.arithmetic import arithmetic_task
from rule_articulation.tasks.capitalization import capitalization_task
from rule_articulation.tasks.same_letter_task import same_letter_task
from rule_articulation.tasks.palindrome import palindrome_task
from rule_articulation.tasks.short_sentences import short_sentence_task
from rule_articulation.tasks.source_mixer import bible_vs_shakespeare_task

TASKS: dict[str, RuleArticulationTask] = {
    "arithmetic": arithmetic_task,
    "bibleshakespeare": bible_vs_shakespeare_task,
    "capitalization": capitalization_task,
    "palindrome": palindrome_task,
    "sameletter": same_letter_task,
    "shortsentence": short_sentence_task,
}