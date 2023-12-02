from dataclasses import dataclass


@dataclass
class LabelledInput:
    input: str
    label: bool


@dataclass
class TaskDescription:
    human_articulation: str
    labelled_inputs: list[LabelledInput]
    prompt_preamble: str = """You are a precise classifier, and you need to respond with a JSON object that is either
'{"label": true}' or '{"label": false}'.

Below, you are given a list of sentences, each labelled as true or false.
There is a single, simple rule that determines whether a setence is labelled true or false.
Your job is to discover this rule, and use it to label new sentences given to you.

These are the example sentences:

"""

    def get_system_prompt(self) -> str:
        return (
            self.prompt_preamble
            + "\n\n"
            + "\n\n".join(
                [
                    f'Input: "{labelled_input.input}"\nLabel: {labelled_input.label}'
                    for labelled_input in self.labelled_inputs
                ]
            )
            + "\n\n---\n\nNow do the same for any new sentences provided to you.\n\n"
        )
