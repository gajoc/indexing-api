from enum import Enum


class VoiceCommand(Enum):
    DATA = 0
    COPY = 1
    NEXT = 2
    UNREADABLE = 3


class Language(Enum):
    EN = 'en'
    PL = 'pl'


config = {
    'selenium': {
        'chrome': {
            'driverPath': 'bin/chromedriver',
            'experimentalOptions': {
                'debuggerAddress': '127.0.0.1:9222',
            }
        }
    },
    'common': {
        'storage_dir': 'data',
    },
    'voice_command_translator': {
        Language.EN: {
            'data': VoiceCommand.DATA,
            'copy': VoiceCommand.COPY,
            'next': VoiceCommand.NEXT,
            'not clear': VoiceCommand.UNREADABLE
        },
        Language.PL: {
            'dane': VoiceCommand.DATA,
            'kopia': VoiceCommand.COPY,
            'następny': VoiceCommand.NEXT,
            'następne': VoiceCommand.NEXT,
            'nieczytelny': VoiceCommand.UNREADABLE,
            'nieczytelne': VoiceCommand.UNREADABLE,
        },
    }
}

user_config = {
    'fields': ('nazwisko', 'data_ur', 'scan_link', 'save'),
    'autocomplete_fields': ('data_ur',),
    'click_button': "span[class='next pager-icon fs-civ-circle-chevron-right enabled']",
    'voice_language': Language.PL,
}
