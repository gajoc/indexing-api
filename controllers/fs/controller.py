from domain.action.one_page_one_man import OnePageOneManAction
from controllers.kbrd_controller import KeyboardController
from controllers.voice_controller import VoiceController


class FamilySearchMilitaryRecordsVoiceCommand(OnePageOneManAction, VoiceController):

    def __init__(self):
        super().__init__()


class FamilySearchMilitaryRecordsKeyboardCommand(OnePageOneManAction, KeyboardController):

    def __init__(self):
        super().__init__()
