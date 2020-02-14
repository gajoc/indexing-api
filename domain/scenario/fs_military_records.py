from domain.action.one_page_one_man import OnePageOneManAction
from domain.controller.kbrd_controller import KeyboardController
from domain.controller.voice_controller import VoiceController


class FamilySearchMilitaryRecordsVoiceCommand(OnePageOneManAction, VoiceController):

    def __init__(self):
        super().__init__()


class FamilySearchMilitaryRecordsKeyboardCommand(OnePageOneManAction, KeyboardController):

    def __init__(self):
        super().__init__()