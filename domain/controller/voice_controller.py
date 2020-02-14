from typing import Union

import speech_recognition as sr

from domain.controller.common_controller import CommonController
from utils.constants import UserAction, COMMAND_2_ACTION, SPEECH_2_COMMAND


class VoiceController(CommonController):

    def __init__(self):
        super().__init__()
        self._to_command = SPEECH_2_COMMAND

    @property
    def user_prompt_info(self):
        return 'Powiedz co robimy? dane | kopia | następny | poprzedni | nieczytelny | koniec'

    def wait_for_user_action(self) -> UserAction:
        speech_recognized = self.get_voice_command()
        command = self._to_command.get(speech_recognized)
        return COMMAND_2_ACTION.get(command)

    def await_for_voice_command(self) -> Union[str, None]:
        r = sr.Recognizer()
        r.energy_threshold = 500
        r.dynamic_energy_threshold = False
        with sr.Microphone() as source:
            print(self.user_prompt_info)
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source)
        try:
            voice_command = r.recognize_google(audio, language='pl')
            if voice_command:
                voice_command = voice_command.lower()
            print(f'Google twiedzi, że powiedziałeś {voice_command}.')
            return voice_command
        except sr.UnknownValueError:
            print("Google nie zrozumiało tego co powiedziałeś.")
            return
        except sr.RequestError as e:
            print("Mamy problem, nie można odebrać wyników z Google Speech Recognition service; {0}".format(e))
            return

    def get_voice_command(self) -> str:
        command = self.await_for_voice_command()
        while not command:
            print('Powtórz proszę jeszcze raz!')
            command = self.await_for_voice_command()
        return command
