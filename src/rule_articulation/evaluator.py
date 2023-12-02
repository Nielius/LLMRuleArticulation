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


def get_true_or_false_response(
    system_prompt: str, prompt: str, json_key: str = "label"
) -> bool | None:
    global total_tokens_used
    logger.debug("System prompt: %s", system_prompt)
    logger.debug("Prompt: %s", prompt)
    response = client.chat.completions.create(
        # model="gpt-4-1106-preview",
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": system_prompt,
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

    def print(self):
        print(f"Fraction correct: {self.fraction_correct}")
        print(f"Total tokens used: {total_tokens_used}")
        print("Mislabelled responses:")
        for labelled_input, response in self.mislabelled_responses:
            print(f"Input: {labelled_input.input}")
            print(f"Label: {labelled_input.label}")
            print(f"Response: {response}")
            print()


class TaskEvaluator:
    def evaluate(
        self, task: TaskDescription, test_data: list[LabelledInput]
    ) -> EvaluationReport:
        input_strings = [labelled_input.input for labelled_input in test_data]

        output = [
            get_true_or_false_response(task.get_system_prompt(), f'Input: "{input}".\nLabel: ???')
            for input in input_strings
        ]

        return EvaluationReport(task, test_data, output)
