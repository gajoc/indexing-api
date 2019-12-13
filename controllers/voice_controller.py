from typing import Union

from controllers.common_controller import CommonController
from utils.constants import UserAction, COMMAND_2_ACTION, SPEECH_2_COMMAND
from utils.mic import get_voice_command, collect_user_inputs


class VoiceController(CommonController):

    def __init__(self):
        super().__init__()
        self._to_command = SPEECH_2_COMMAND

    def wait_for_user_action(self) -> UserAction:
        speech_recognized = get_voice_command()
        command = self._to_command.get(speech_recognized)
        return COMMAND_2_ACTION.get(command)

    def execute(self, action: UserAction) -> Union[UserAction, None]:
        if action == UserAction.DATA_INPUT:
            entity = collect_user_inputs(self._input_fields, autocomplete=self._autocomplete)
            self._add_browser_link(entity)
            self._storage.add(entity)
            print(entity)

        elif action == UserAction.NEXT_SCAN:
            self._browser.click_next()
        else:
            print(f'Nierozpoznano akcji {action}')
