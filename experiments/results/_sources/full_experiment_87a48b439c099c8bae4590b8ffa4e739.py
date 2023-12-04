from dataclasses import asdict
from pathlib import Path

from sacred import Experiment
from sacred.observers import FileStorageObserver

from rule_articulation.evaluator import TaskEvaluator
from rule_articulation.utils import get_openai_model, get_task, set_default_log_settings

set_default_log_settings()

ex = Experiment("config_demo")

results_path = Path(__file__).parent.parent.parent / "experiments" / "results"
print("Storing results in: ", results_path)
ex.observers.append(FileStorageObserver(results_path))


@ex.config
def experiment_config():
    """This is my demo configuration"""

    task: str = "capitalization"
    gpt4: bool = False
    num_test_examples: int = 10
    num_articulations: int = 1


@ex.automain
def run(task: str, gpt4: bool, num_test_examples: int, num_articulations: int):
    print("Running experiment with config:")
    print(f"{task=}")
    print(f"gpt4: {gpt4} (type: {type(gpt4)})")
    print(f"{num_test_examples=}")
    print(f"{num_articulations=}")

    task = get_task(task)
    evaluator = TaskEvaluator(
        task=task.description, openai_model=get_openai_model(gpt4), num_articulations=num_articulations
    )

    test_data = task.dataset.sample(num_test_examples)
    ex.info["test_data"] = test_data

    # First, evaluate
    report = evaluator.evaluate(test_data)

    ex.info["report"] = report
    ex.info["fraction_correct"] = report.fraction_correct
    ex.info["mislabelled_responses"] = [
        (asdict(input), response) for input, response in report.mislabelled_responses
    ]
    ex.info["evaluation_prompt_example"] = evaluator.evaluation_prompt_messages(
        test_data[0].input
    )

    # Second, ask for articulation
    articulations = evaluator.ask_articulation()
    ex.info["articulation"] = articulations
    ex.info["articulation_prompt_messages"] = evaluator.articulation_prompt_messages()
    # TODO: store the entire articulation chat here

    # {"role": "system", "content": "You are a helpful assistant."},
    # {"role": "user", "content": "Who won the world series in 2020?"},
    # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    # {"role": "user", "content": "Where was it played?"}
