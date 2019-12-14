from typing import Sequence, Type, Union, Dict

import speech_recognition as sr

from utils.autocomplete import AutocompleteFields


def await_for_voice_command() -> Union[str, None]:
    r = sr.Recognizer()
    r.energy_threshold = 500
    r.dynamic_energy_threshold = False
    with sr.Microphone() as source:
        print('Powiedz co robimy? dane | kopia | następny | nieczytelny | koniec')
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


def get_voice_command() -> str:
    command = await_for_voice_command()
    while not command:
        print('Powtórz proszę jeszcze raz!')
        command = await_for_voice_command()
    return command


def collect_user_inputs(fields: Sequence, autocomplete: Type[AutocompleteFields] = None) -> Dict:
    entity = {}
    for field in fields:
        user_input = input(f'{field}: ')
        entity[field] = autocomplete.fill_missing(field, value=user_input) \
            if autocomplete else \
            user_input if user_input else None
    return entity


def add_info(entity: Dict, value) -> None:
    entity['info'] = value
