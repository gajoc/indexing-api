import json
import os
import uuid
from typing import Dict

from model.ientity import MilitaryEntityFamilySearchSchema


class Storage:

    def __init__(self, storage_dir: str):
        self._storage_dir = storage_dir
        self._store = []

    def add(self, entity: Dict) -> None:
        self._store.append(entity)

    def get_previous_copied(self) -> Dict:
        return self._store[-1].copy()

    def dump(self) -> None:
        with open(f'{self._storage_dir}{os.sep}data-{uuid.uuid1()}.json', 'w', encoding='utf-8') as f:
            schema = MilitaryEntityFamilySearchSchema()
            serialized_store = schema.dump(self._store, many=True)
            json.dump(serialized_store, f, ensure_ascii=False, indent=4)
        print(f'Dane zapisano do pliku, zrzucono {len(self)} elementów.')
        self._store = []

    def __len__(self) -> int:
        return len(self._store)
