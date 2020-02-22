from enum import IntEnum, Enum


DEFAULT_STORAGE_DIR = "data"
DEFAULT_STORAGE_ENTITIES_LIMIT = 0
DEFAULT_ENCODING = "utf-8"
DEFAULT_CONFIG_FILE = "config.json"


class UserAction(IntEnum):
    EXIT = 0
    DATA_INPUT = 1
    NEXT_SCAN = 2
    PREV_SCAN = 3
    COPY = 4
    UNREADABLE = 5


class InteractionMethod(Enum):
    VOICE = 'voice'
    KEYBOARD = 'keyboard'


class GenealogyDocumentType(Enum):
    MILITARY_RECORD = 'military_record'


SPEECH_2_ACTION = {
    'dane': UserAction.DATA_INPUT,
    'kopia': UserAction.COPY,
    'następny': UserAction.NEXT_SCAN,
    'następne': UserAction.NEXT_SCAN,
    'wróć': UserAction.PREV_SCAN,
    'poprzedni': UserAction.PREV_SCAN,
    'nieczytelny': UserAction.UNREADABLE,
    'nieczytelne': UserAction.UNREADABLE,
    'koniec': UserAction.EXIT,
}


KEYBOARD_BUTTON_2_ACTION = {
    '1': UserAction.DATA_INPUT,
    '2': UserAction.COPY,
    '3': UserAction.NEXT_SCAN,
    '4': UserAction.PREV_SCAN,
    '5': UserAction.UNREADABLE,
    '6': UserAction.EXIT,
}


INPUT_FIELDS = ('surname', 'born_year',)
AUTOCOMPLETE_FIELDS = ('born_year',)

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


class BrowserAction(Enum):
    NEXT = 'click_next'
    PREVIOUS = 'click_previous'
    GET_LINK = 'current_url'


class FamilySearchButton(Enum):
    NEXT = "span[class='next pager-icon fs-civ-circle-chevron-right enabled']"
    PREV = "span[class='previous pager-icon fs-civ-circle-chevron-left enabled']"


class GenealogyService(Enum):
    FAMILY_SEARCH = 'fs'


class BrowserButtons:
    @staticmethod
    def get(service: GenealogyService) -> Enum:
        mapper = {
            GenealogyService.FAMILY_SEARCH: FamilySearchButton
        }
        return mapper[service]
