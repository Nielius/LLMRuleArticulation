from importlib.resources import files
import json

def get_openai_key() -> dict:
    """Get the OpenAI key from the secrets.json file.

    Returns:
        dict: The OpenAI key.
    """
    with files("rule_articulation.secrets").joinpath(".openai-key.json").open() as f:
        return json.load(f)
