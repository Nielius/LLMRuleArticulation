from dataclasses import dataclass


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
