import math
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


def asterisk_string(value: str, parts: int) -> str:
    x = math.ceil(len(value)/parts)
    return f'{value[:x]}***{value[-x:]}'


def short_print(entity: Dict, values_only: bool = True, link_parts: int = 5) -> None:
    short_entity = entity.copy()
    short_entity.pop('created_utc')
    short_entity['scan_link'] = asterisk_string(short_entity['scan_link'], parts=link_parts)
    print(tuple(short_entity.values()) if values_only else short_entity)
