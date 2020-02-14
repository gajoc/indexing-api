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
        elif action == UserAction.NEXT_SCAN:
            self._browser.click_next()
        elif action == UserAction.COPY:
            entity = self._storage.get_previous_copied()
            self._prepare_and_add_to_storage(entity, UserAction.COPY)
            human_view = self.human_readable_schema.dump(entity)
            print(human_view)
        elif action == UserAction.UNREADABLE:
            entity = {}
            self._prepare_and_add_to_storage(entity, UserAction.UNREADABLE)
        elif action == UserAction.PREV_SCAN:
            entity = self._storage.pop_previous()
            human_view = self.human_readable_schema.dump(entity) if entity else {}
            print(f'popped entity {human_view}')
            self._browser.click_previous()
        else:
            print(f'Nieznana akcja, proszę wybrać jedną z dostępnych akcji.')
        return self.next_action(action)

    def next_action(self, action: UserAction) -> Union[UserAction, None]:
        mapper = {
            UserAction.DATA_INPUT: UserAction.NEXT_SCAN,
            UserAction.NEXT_SCAN: None,
            UserAction.COPY: UserAction.NEXT_SCAN,
            UserAction.UNREADABLE: UserAction.NEXT_SCAN,
            UserAction.PREV_SCAN: None
        }
        return mapper.get(action)

    def _prepare_and_add_to_storage(self, entity: Dict, action: UserAction) -> None:
        self._add_browser_link(entity, key='scan_link')
        entity['info'] = action
        entity['created_utc'] = datetime.utcnow()
        self._storage.add(entity)
