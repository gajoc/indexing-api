from typing import Sequence

from domain.action_handler.iaction_handler import IActionHandler
from utils.autocomplete import AutocompleteFields
from utils.misc import collect_user_inputs
from utils.storage import Storage


class CollectUserInputHandler(IActionHandler):

    def handle(self, fields: Sequence, autocomplete: AutocompleteFields, storage: Storage, **kwargs):
        entity = collect_user_inputs(fields, autocomplete)
        entity.update(**kwargs)
        storage.add(entity)
        human_view = self.human_readable_schema.dump(entity)
        print(human_view)
