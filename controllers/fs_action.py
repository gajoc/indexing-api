from typing import Union

from controllers.iaction import IAction
from utils.constants import UserAction
from utils.misc import collect_user_inputs, add_info


class FamilySearchOnePageOneManAction(IAction):

    def __init__(self):
        super().__init__()

    def execute(self, action: UserAction) -> Union[UserAction, None]:
        if action == UserAction.DATA_INPUT:
            entity = collect_user_inputs(self._input_fields, autocomplete=self._autocomplete)
            self._add_browser_link(entity)
            add_info(entity, value=UserAction.DATA_INPUT.name)
            self._storage.add(entity)
            print(entity)
            return UserAction.NEXT_SCAN
        elif action == UserAction.NEXT_SCAN:
            self._browser.click_next()
        elif action == UserAction.COPY:
            entity = self._storage.get_previous_copied()
            self._add_browser_link(entity)
            add_info(entity, value=UserAction.COPY.name)
            self._storage.add(entity)
            return UserAction.NEXT_SCAN
        elif action == UserAction.UNREADABLE:
            entity = {}
            self._add_browser_link(entity)
            add_info(entity, value=UserAction.UNREADABLE.name)
            self._storage.add(entity)
            print(entity)
            return UserAction.NEXT_SCAN
        else:
            print(f'Nieznana akcja, proszę wybrać jedną z dostępnych akcji.')
