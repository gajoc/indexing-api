from typing import Union, Dict

from controllers.icontroller import IController
from utils.autocomplete import AutocompleteFields
from utils.browser import Browser
from utils.constants import UserAction, COMMAND_2_ACTION, SPEECH_2_COMMAND, AUTOCOMPLETE_FIELDS, INPUT_FIELDS, \
    USER_BROWSER, NEXT_BUTTON_FAMILY_SEARCH, SELENIUM_CONFIG, STORAGE_DIR
from utils.mic import get_voice_command, collect_user_inputs
from utils.storage import Storage


class VoiceController(IController):

    def __init__(self):
        self._to_command = SPEECH_2_COMMAND
        self._autocomplete = AutocompleteFields(fields=AUTOCOMPLETE_FIELDS)
        self._browser = Browser(user_browser=USER_BROWSER,
                                next_button=NEXT_BUTTON_FAMILY_SEARCH,
                                previous_button=None,
                                config=SELENIUM_CONFIG)
        self._input_fields = INPUT_FIELDS
        self._storage = Storage(STORAGE_DIR)

    def wait_for_user_action(self) -> UserAction:
        speech_recognized = get_voice_command()
        command = self._to_command.get(speech_recognized)
        return COMMAND_2_ACTION.get(command)

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
