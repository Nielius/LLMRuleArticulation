from pathlib import Path

from sacred import Experiment
from sacred.observers import FileStorageObserver

from rule_articulation.evaluator import TaskEvaluator
from rule_articulation.utils import get_openai_model
from rule_articulation.tasks.capitalization import capitalization_task_description, CapitalizationDataset

ex = Experiment("config_demo")

results_path = Path(__file__).parent.parent.parent / "experiments" / "results"
print("Storing results in: ", results_path)
ex.observers.append(FileStorageObserver(results_path))


@ex.config
def experiment_config():
    """This is my demo configuration"""

    task: str = "capitalization"
    gpt4: bool = False


@ex.automain
def run(task: str, gpt4: bool):
    print("Running experiment with config:")
    print(f"task: {task}")
    print(f"gpt4: {gpt4} (type: {type(gpt4)})")

    evaluator = TaskEvaluator(openai_model=get_openai_model(gpt4))

    test_data = CapitalizationDataset().sample(10)

    ex.info["test_data"] = test_data

    report = evaluator.evaluate(test_data)

    ex.info["report"] = report

