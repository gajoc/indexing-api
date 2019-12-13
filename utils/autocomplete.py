from typing import Sequence, Any


class AutocompleteFields:

    _user_input_cache = {}

    def __init__(self, fields: Sequence):
        self._autocomplete = fields

    def fill_missing(self, field: str, value: Any):
        if field not in self._autocomplete:
            return value
        if value:
            self._user_input_cache[field] = value
            return value
        return self._user_input_cache.get(field, value)
