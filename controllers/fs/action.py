from datetime import datetime
from typing import Union, Dict

from controllers.iaction import IAction
from model.ientity import HumanReadableSchema
from utils.constants import UserAction
from utils.misc import collect_user_inputs


class FamilySearchOnePageOneManAction(IAction):

    def __init__(self):
        super().__init__()
        self.human_readable_schema = HumanReadableSchema()

    def execute(self, action: UserAction) -> Union[UserAction, None]:
        if action == UserAction.DATA_INPUT:
            entity = collect_user_inputs(self._input_fields, autocomplete=self._autocomplete)
            self._prepare_and_add_to_storage(entity, UserAction.DATA_INPUT)
            human_view = self.human_readable_schema.dump(entity)
            print(human_view)
            return UserAction.NEXT_SCAN
        elif action == UserAction.NEXT_SCAN:
            self._browser.click_next()
        elif action == UserAction.COPY:
            entity = self._storage.get_previous_copied()
            self._prepare_and_add_to_storage(entity, UserAction.COPY)
            human_view = self.human_readable_schema.dump(entity)
            print(human_view)
            return UserAction.NEXT_SCAN
        elif action == UserAction.UNREADABLE:
            entity = {}
            self._prepare_and_add_to_storage(entity, UserAction.UNREADABLE)
            return UserAction.NEXT_SCAN
        else:
            print(f'Nieznana akcja, proszę wybrać jedną z dostępnych akcji.')

    def _prepare_and_add_to_storage(self, entity: Dict, action: UserAction) -> None:
        self._add_browser_link(entity, key='scan_link')
        entity['info'] = action
        entity['created_utc'] = datetime.utcnow()
        self._storage.add(entity)
