from typing import Union

from controllers.common_controller import CommonController
from utils.constants import UserAction, KEYBOARD_BUTTON_2_ACTION
from utils.mic import collect_user_inputs, add_info


class KeyboardController(CommonController):

    def __init__(self):
        super().__init__()
        self._to_command = KEYBOARD_BUTTON_2_ACTION

    def wait_for_user_action(self) -> UserAction:
        user_choice = input('Co robimy? 1.dane 2.kopia 3.nastepny 4.--- 5.nieczytelny 6.koniec\n')
        return self._to_command.get(user_choice)

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
