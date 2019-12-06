import json
import os
import uuid
from datetime import datetime


class Storage:

    _store = []

    def __init__(self, storage_dir):
        self._storage_dir = storage_dir

    def add(self, entity):
        entity['created_utc'] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        self._store.append(entity)

    def get_previous(self):
        return self._store[-1].copy()

    def dump(self):
        with open(f'{self._storage_dir}{os.sep}data-{uuid.uuid1()}.json', 'w', encoding='utf-8') as f:
            json.dump(self._store, f, ensure_ascii=False, indent=4)

    def __len__(self):
        return len(self._store)
