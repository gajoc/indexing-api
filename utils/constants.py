from enum import IntEnum, Enum


class UserAction(IntEnum):
    EXIT = 0
    DATA_INPUT = 1
    NEXT_SCAN = 2
    PREV_SCAN = 3
    COPY = 4
    UNREADABLE = 5


class VoiceCommand(Enum):
    DATA = 0
    COPY = 1
    NEXT = 2
    UNREADABLE = 3
    EXIT = 4
    PREV = 5


COMMAND_2_ACTION = {
    VoiceCommand.DATA: UserAction.DATA_INPUT,
    VoiceCommand.NEXT: UserAction.NEXT_SCAN,
    VoiceCommand.EXIT: UserAction.EXIT,
    VoiceCommand.PREV: UserAction.PREV_SCAN,
    VoiceCommand.COPY: UserAction.COPY,
    VoiceCommand.UNREADABLE: UserAction.UNREADABLE,
}


class Language(Enum):
    EN = 'en'
    PL = 'pl'


SPEECH_2_COMMAND = {
    'dane': VoiceCommand.DATA,
    'kopia': VoiceCommand.COPY,
    'następny': VoiceCommand.NEXT,
    'następne': VoiceCommand.NEXT,
    'wróć': VoiceCommand.PREV,
    'poprzedni': VoiceCommand.PREV,
    'nieczytelny': VoiceCommand.UNREADABLE,
    'nieczytelne': VoiceCommand.UNREADABLE,
    'koniec': VoiceCommand.EXIT,
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
NEXT_BUTTON_FAMILY_SEARCH = "span[class='next pager-icon fs-civ-circle-chevron-right enabled']"
PREVIOUS_BUTTON_FAMILY_SEARCH = "span[class='previous pager-icon fs-civ-circle-chevron-left enabled']"
VOICE_LANGUAGE = Language.PL

USER_BROWSER = 'chrome'
SELENIUM_CONFIG = {
    'chrome': {
        'driverPath': 'bin/chromedriver',
        'experimentalOptions': {
            'debuggerAddress': '127.0.0.1:9222',
        }
    }
}
STORAGE_DIR = 'data'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
STORAGE_ENTITIES_LIMIT = 100


class BrowserAction(Enum):
    NEXT = 'click_next'
    PREVIOUS = 'click_previous'
    GET_LINK = 'current_url'
