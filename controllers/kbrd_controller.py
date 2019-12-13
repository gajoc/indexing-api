from typing import Union

from controllers.common_controller import CommonController
from utils.constants import UserAction, KEYBOARD_BUTTON_2_ACTION
from utils.mic import collect_user_inputs


class KeyboardController(CommonController):

    def __init__(self):
        super().__init__()
        self._to_command = KEYBOARD_BUTTON_2_ACTION

    def wait_for_user_action(self) -> UserAction:
        user_choice = input('Co robimy? 1.dane 2.--- 3.nastepny 4.--- 5.wyjscie\n')
        return self._to_command.get(user_choice)

    def execute(self, action: UserAction) -> Union[UserAction, None]:
        if action == UserAction.DATA_INPUT:
            entity = collect_user_inputs(self._input_fields, autocomplete=self._autocomplete)
            self._add_browser_link(entity)
            self._storage.add(entity)
            print(entity)

        elif action == UserAction.NEXT_SCAN:
            self._browser.click_next()
        else:
            print(f'Nierozpoznano akcji {action}')
