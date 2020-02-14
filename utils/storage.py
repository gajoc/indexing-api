import json
import os
import uuid
from contextlib import suppress
from functools import wraps
from typing import Dict

from model.fs_military_entity import MilitaryEntityFamilySearchSchema


def _auto_dump(fn):
    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        entities_count = len(self)
        if self.storage_entities_limit and entities_count >= self.storage_entities_limit:
            self.dump()
        return fn(self, *args, **kwargs)
    return wrapper


class Storage:

    def __init__(self, storage_dir: str, storage_entities_limit: int = 0):
        self.storage_entities_limit = storage_entities_limit
        self._storage_dir = storage_dir
        self._store = []

    @_auto_dump
    def add(self, entity: Dict) -> None:
        self._store.append(entity)

    def get_previous_copied(self) -> Dict:
        previous = {}
        with suppress(IndexError):
            previous = self._store[-1].copy()
        return previous

    def pop_previous(self) -> Dict:
        previous = {}
        with suppress(IndexError):
            previous = self._store.pop()
        return previous

    def dump(self) -> None:
        with open(f'{self._storage_dir}{os.sep}data-{uuid.uuid1()}.json', 'w', encoding='utf-8') as f:
            schema = MilitaryEntityFamilySearchSchema()
            serialized_store = schema.dump(self._store, many=True)
            json.dump(serialized_store, f, ensure_ascii=False, indent=4)
        print(f'Dane zapisano do pliku, zrzucono {len(self)} elementów.')
        self._store = []

    def __len__(self) -> int:
        return len(self._store)
