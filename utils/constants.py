from enum import IntEnum, Enum


class UserAction(IntEnum):
    EXIT = 0
    DATA_INPUT = 1
    NEXT_SCAN = 2
    PREV_SCAN = 3
    MEM_LINK = 4
    DUMP_DATA = 5


class VoiceCommand(Enum):
    DATA = 0
    COPY = 1
    NEXT = 2
    UNREADABLE = 3
    EXIT = 4


COMMAND_2_ACTION = {
    VoiceCommand.DATA: UserAction.DATA_INPUT,
    VoiceCommand.NEXT: UserAction.NEXT_SCAN,
    VoiceCommand.EXIT: UserAction.EXIT,
}


class Language(Enum):
    EN = 'en'
    PL = 'pl'


SPEECH_2_COMMAND = {
    'dane': VoiceCommand.DATA,
    'kopia': VoiceCommand.COPY,
    'następny': VoiceCommand.NEXT,
    'następne': VoiceCommand.NEXT,
    'nieczytelny': VoiceCommand.UNREADABLE,
    'nieczytelne': VoiceCommand.UNREADABLE,
    'koniec': VoiceCommand.EXIT,
}


KEYBOARD_BUTTON_2_ACTION = {
    '1': UserAction.DATA_INPUT,
    '2': None,
    '3': UserAction.NEXT_SCAN,
    '4': None,
    '5': UserAction.EXIT,
}


INPUT_FIELDS = ('nazwisko', 'data_ur',)
AUTOCOMPLETE_FIELDS = ('data_ur',)
NEXT_BUTTON_FAMILY_SEARCH = "span[class='next pager-icon fs-civ-circle-chevron-right enabled']"
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
