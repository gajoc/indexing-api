from typing import Sequence, Type, Dict

from utils.autocomplete import AutocompleteFields


def collect_user_inputs(fields: Sequence, autocomplete: Type[AutocompleteFields] = None) -> Dict:
    entity = {}
    for field in fields:
        user_input = input(f'{field}: ')
        entity[field] = autocomplete.fill_missing(field, value=user_input) \
            if autocomplete else \
            user_input if user_input else None
    return entity


def add_info(entity: Dict, value) -> None:
    entity['info'] = value
