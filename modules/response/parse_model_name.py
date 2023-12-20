# for type hints
from ..typing import Model

# this function takes the model and removes the unneccessary 'gpt' at the end
def parse_model_name(model: Model | str, suffix: str = ' (ignore this: gpt)') -> Model | str:

    return str(model).removesuffix(suffix)