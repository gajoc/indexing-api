import math
from datetime import datetime
from typing import Sequence, Type, Dict

from utils.autocomplete import AutocompleteFields
from utils.constants import UserAction


def collect_user_inputs(fields: Sequence, autocomplete: Type[AutocompleteFields] = None) -> Dict:
    entity = {}
    for field in fields:
        user_input = input(f'{field}: ')
        entity[field] = autocomplete.fill_missing(field, value=user_input) \
            if autocomplete else \
            user_input if user_input else None
    return entity


def asterisk_string(value: str, parts: int) -> str:
    x = math.ceil(len(value)/parts)
    return f'{value[:x]}***{value[-x:]}'


def entity_base_data(scan_link: str, info: UserAction, **kwargs) -> Dict:
    entity = {
        'scan_link': scan_link,
        'info': info,
        'created_utc': datetime.utcnow()
    }
    entity.update(**kwargs)
    return entity
