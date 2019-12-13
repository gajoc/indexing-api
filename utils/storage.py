import json
import os
import uuid
from datetime import datetime
from typing import Dict


class Storage:

    def __init__(self, storage_dir: str):
        self._storage_dir = storage_dir
        self._store = []

    def add(self, entity: Dict) -> None:
        entity['created_utc'] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        self._store.append(entity)

    def get_previous_copied(self) -> Dict:
        return self._store[-1].copy()

    def dump(self) -> None:
        with open(f'{self._storage_dir}{os.sep}data-{uuid.uuid1()}.json', 'w', encoding='utf-8') as f:
            json.dump(self._store, f, ensure_ascii=False, indent=4)
        print(f'Dane zapisano do pliku, zrzucono {len(self)} elementów.')
        self._store = []

    def __len__(self) -> int:
        return len(self._store)
