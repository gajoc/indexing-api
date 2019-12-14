from controllers.common_controller import CommonController
from utils.constants import UserAction, KEYBOARD_BUTTON_2_ACTION


class KeyboardController(CommonController):

    def __init__(self):
        super().__init__()
        self._to_command = KEYBOARD_BUTTON_2_ACTION

    def wait_for_user_action(self) -> UserAction:
        user_choice = input('Co robimy? 1.dane 2.kopia 3.nastepny 4.--- 5.nieczytelny 6.koniec\n')
        return self._to_command.get(user_choice)
