from controllers.common_controller import CommonController
from utils.constants import UserAction, COMMAND_2_ACTION, SPEECH_2_COMMAND
from utils.mic import get_voice_command


class VoiceController(CommonController):

    def __init__(self):
        super().__init__()
        self._to_command = SPEECH_2_COMMAND

    def wait_for_user_action(self) -> UserAction:
        speech_recognized = get_voice_command()
        command = self._to_command.get(speech_recognized)
        return COMMAND_2_ACTION.get(command)
