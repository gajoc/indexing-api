from controllers.fs.action import FamilySearchOnePageOneManAction
from controllers.kbrd_controller import KeyboardController
from controllers.voice_controller import VoiceController


class FamilySearchMilitaryRecordsVoiceCommand(VoiceController, FamilySearchOnePageOneManAction):

    def __init__(self):
        super().__init__()


class FamilySearchMilitaryRecordsKeyboardCommand(KeyboardController, FamilySearchOnePageOneManAction):

    def __init__(self):
        super().__init__()
