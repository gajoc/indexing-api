from domain.action.one_page_one_man import OnePageOneManAction
from domain.controller.kbrd_controller import KeyboardController
from domain.controller.voice_controller import VoiceController
from utils.autocomplete import AutocompleteFields
from utils.browser import Browser
from utils.constants import AUTOCOMPLETE_FIELDS, INPUT_FIELDS
from utils.storage import Storage


class FamilySearchMilitaryRecordsVoiceCommand(OnePageOneManAction, VoiceController):

    def __init__(self, browser: Browser, storage: Storage):
        super().__init__()
        self._storage = storage
        self._browser = browser
        self._autocomplete = AutocompleteFields(fields=AUTOCOMPLETE_FIELDS)
        self._input_fields = INPUT_FIELDS


class FamilySearchMilitaryRecordsKeyboardCommand(OnePageOneManAction, KeyboardController):

    def __init__(self, browser: Browser, storage: Storage):
        super().__init__()
        self._storage = storage
        self._browser = browser
        self._autocomplete = AutocompleteFields(fields=AUTOCOMPLETE_FIELDS)
        self._input_fields = INPUT_FIELDS
