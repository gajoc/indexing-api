from typing import Union, Dict

from controllers.icontroller import IController
from utils.autocomplete import AutocompleteFields
from utils.browser import Browser
from utils.constants import UserAction, USER_BROWSER, NEXT_BUTTON_FAMILY_SEARCH, SELENIUM_CONFIG, AUTOCOMPLETE_FIELDS, \
    INPUT_FIELDS, STORAGE_DIR, KEYBOARD_BUTTON_2_ACTION
from utils.mic import collect_user_inputs
from utils.storage import Storage


class KeyboardController(IController):

    def __init__(self):
        self._to_command = KEYBOARD_BUTTON_2_ACTION
        self._autocomplete = AutocompleteFields(fields=AUTOCOMPLETE_FIELDS)
        self._browser = Browser(user_browser=USER_BROWSER,
                                next_button=NEXT_BUTTON_FAMILY_SEARCH,
                                previous_button=None,
                                config=SELENIUM_CONFIG)
        self._input_fields = INPUT_FIELDS
        self._storage = Storage(STORAGE_DIR)

    def wait_for_user_action(self) -> UserAction:
        user_choice = input('Co robimy? 1.dane 2.--- 3.nastepny 4.--- 5.wyjscie\n')
        return self._to_command.get(user_choice)

    def before_exit(self) -> None:
        self._storage.dump()

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

    def _add_browser_link(self, entity: Dict) -> None:
        entity['scan_link'] = self._browser.current_url()
