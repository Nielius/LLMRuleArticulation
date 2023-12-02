import json
from dataclasses import dataclass
from functools import cached_property

import instructor
from openai import OpenAI
from pydantic import BaseModel

from rule_articulation.secrets import get_openai_key

import logging

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)

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
class LabelledInput:
    input: str
    label: bool


@dataclass
class TaskDescription:
    labelled_inputs: list[LabelledInput]
    prompt: str = "Please carefully consider the following statements that are labelled as true or false."

    def get_prompt(self) -> str:
        return (
            self.prompt
            + "\n\n"
            + "\n\n".join(
                [
                    f'Input: "{labelled_input.input}"\nLabel: {labelled_input.label}'
                    for labelled_input in self.labelled_inputs
                ]
            )
        )


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
        tasks = [labelled_input.input for labelled_input in test_data]
        output = self.execute_task(task, tasks)

        return EvaluationReport(task, test_data, output)

    def execute_task(
        self, description: TaskDescription, tasks: list[str]
    ) -> list[bool | None]:
        return [
            get_true_or_false_response(
                description.get_prompt()
                + "\n\n---\n\nNow provide the label for the following input in JSON format:\n\n"
                f'Input: "{task}"'
            )
            for task in tasks
        ]
#
#
#
# output = execute_task(
#     capitalization_task,
#     [
#         "wHaT is going ON?",
#         "is this correct?",
#         "not a question but still FALSE",
#         "what bout this",
#     ],
# )
# output
#
#
# get_true_or_false_response("Is 1 + 1 = 2 true?")
# get_true_or_false_response("Is 1 + 1 = 3 true?")
#
#
# get_true_or_false_response(
#     """
# Please carefully consider the following statements that are labelled as true or false.
#
# Input: "the cat sat on the mat"
# Label: True
#
# Input: "THE DOG RAN IN THE PARK"
# Label: False
#
# Input: "THE mat sat on the cat"
# Label: False
#
# Input: "the house is cold"
# Label: True
#
# ---
#
# Now provide the label for the following input in JSON format:
#
# Input: "wHaT is going ON?"
# """
# )
