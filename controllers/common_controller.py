from abc import abstractmethod
from typing import Dict

from controllers.icontroller import IController
from utils.autocomplete import AutocompleteFields
from utils.browser import Browser
from utils.constants import INPUT_FIELDS, STORAGE_DIR, SELENIUM_CONFIG, NEXT_BUTTON_FAMILY_SEARCH, USER_BROWSER, \
    AUTOCOMPLETE_FIELDS, UserAction, PREVIOUS_BUTTON_FAMILY_SEARCH, STORAGE_ENTITIES_LIMIT
from utils.storage import Storage


class CommonController(IController):

    def __init__(self):
        self._autocomplete = AutocompleteFields(fields=AUTOCOMPLETE_FIELDS)
        self._browser = Browser(user_browser=USER_BROWSER,
                                next_button=NEXT_BUTTON_FAMILY_SEARCH,
                                previous_button=PREVIOUS_BUTTON_FAMILY_SEARCH,
                                config=SELENIUM_CONFIG)
        self._input_fields = INPUT_FIELDS
        self._storage = Storage(STORAGE_DIR, STORAGE_ENTITIES_LIMIT)

    @property
    @abstractmethod
    def user_prompt_info(self):
        pass

    @abstractmethod
    def wait_for_user_action(self) -> UserAction:
        pass

    def before_exit(self) -> None:
        self._storage.dump()

    def _add_browser_link(self, entity: Dict, key: str) -> None:
        entity[key] = self._browser.current_url()
