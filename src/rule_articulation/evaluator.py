import json
import logging
from dataclasses import dataclass
from functools import cached_property

from openai import OpenAI

from rule_articulation.secrets import get_openai_key
from rule_articulation.task_model import TaskDescription, LabelledInput

logger = logging.getLogger(__name__)
client = OpenAI(**get_openai_key())
total_tokens_used = 0


def get_true_or_false_response(prompt: str, json_key: str = "label") -> bool | None:
    global total_tokens_used
    logger.debug("Prompt: %s", prompt)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": "You are a helpful classifier, and you need to respond with a JSON object that is either"
                f"'{{\"{json_key}\": true}}' or '{{\"{json_key}\": false}}'.",
            },
            {"role": "user", "content": prompt},
        ],
    )
    total_tokens_used += response.usage.total_tokens

    content = json.loads(response.choices[0].message.content)
    logger.debug("Response: %s", content)

    match content.get(json_key):
        case True:
            return True
        case False:
            return False
        case _:
            print(f"Invalid response from GPT-3: {content}")
            return None


@dataclass
class EvaluationReport:
    task: TaskDescription
    test_data: list[LabelledInput]
    responses: list[bool | None]

    @cached_property
    def fraction_correct(self) -> float:
        return sum(
            [
                1
                for labelled_input, response in zip(self.test_data, self.responses)
                if response == labelled_input.label
            ]
        ) / len(self.test_data)

    @cached_property
    def mislabelled_responses(self) -> list[tuple[LabelledInput, bool | None]]:
        return [
            (labelled_input, response)
            for labelled_input, response in zip(self.test_data, self.responses)
            if response != labelled_input.label
        ]


class TaskEvaluator:
    def evaluate(
        self, task: TaskDescription, test_data: list[LabelledInput]
    ) -> EvaluationReport:
        input_strings = [labelled_input.input for labelled_input in test_data]

        output = [
            get_true_or_false_response(
                task.get_prompt()
                + "\n\n---\n\nNow provide the label for the following input in JSON format:\n\n"
                f'Input: "{input}"'
            )
            for input in input_strings
        ]

        return EvaluationReport(task, test_data, output)
