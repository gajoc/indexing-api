from typing import Union, Dict

from controllers.iaction import IAction
from utils.constants import UserAction
from utils.misc import collect_user_inputs, add_info, short_print


class FamilySearchOnePageOneManAction(IAction):

    def __init__(self):
        super().__init__()

    def execute(self, action: UserAction) -> Union[UserAction, None]:
        if action == UserAction.DATA_INPUT:
            entity = collect_user_inputs(self._input_fields, autocomplete=self._autocomplete)
            self._prepare_and_add_to_storage(entity, UserAction.DATA_INPUT.name)
            short_print(entity)
            return UserAction.NEXT_SCAN
        elif action == UserAction.NEXT_SCAN:
            self._browser.click_next()
        elif action == UserAction.COPY:
            entity = self._storage.get_previous_copied()
            self._prepare_and_add_to_storage(entity, UserAction.COPY.name)
            short_print(entity)
            return UserAction.NEXT_SCAN
        elif action == UserAction.UNREADABLE:
            entity = {}
            self._prepare_and_add_to_storage(entity, UserAction.UNREADABLE.name)
            return UserAction.NEXT_SCAN
        else:
            print(f'Nieznana akcja, proszę wybrać jedną z dostępnych akcji.')

    def _prepare_and_add_to_storage(self, entity: Dict, action_name: str) -> None:
        self._add_browser_link(entity)
        add_info(entity, value=action_name)
        self._storage.add(entity)
