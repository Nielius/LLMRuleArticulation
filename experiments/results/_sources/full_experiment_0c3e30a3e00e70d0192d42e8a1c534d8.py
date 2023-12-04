from pathlib import Path

from sacred import Experiment
from sacred.observers import FileStorageObserver

ex = Experiment("config_demo")

results_path = Path(__file__).parent.parent.parent / "experiments" / "results"
print("Storing results in: ", results_path)
ex.observers.append(
    FileStorageObserver(
        results_path
    )
)


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
