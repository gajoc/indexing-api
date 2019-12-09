from abc import abstractmethod, ABC
from itertools import cycle
from pprint import pprint

from config import VoiceCommand
from utils.autocomplete import AutocompleteFields
from utils.browser import Browser
from utils.mic import get_voice_command
from utils.storage import Storage


class IGeneiApp(ABC):
    @abstractmethod
    def run(self, **config):
        pass


class GeneiAppSelenium(IGeneiApp):

    def __init__(self, **config):
        self._storage = Storage(config['common']['storage_dir'])
        self._to_command = config['voice_command_translator'][config['voice_language']]
        self._autocomplete = AutocompleteFields(fields=config.get('autocomplete_fields', ()))
        self._browser = Browser(user_browser=config['user_browser'],
                                next_button=config['click_next_button'],
                                previous_button=None,
                                config=config['selenium'])
        self._fields = cycle(config['fields'])

    def _save(self, data):
        print('zapisywanie...')
        pprint(data, indent=4)
        self._storage.add(data)
        print("zapisano!\n")

    @staticmethod
    def _prompt(text):
        line = input(f'{text}: ')
        return None if line == '' else line

    def run(self):
        self._welcome()
        person = {}

        while True:
            field = next(self._fields)

            if field == 'save':
                self._save(person)
                person = {}
                self._browser.click_next()
                speech = get_voice_command()
                command = self._to_command.get(speech)

                # click next scan until copy, next or mark as unreadable is needed
                while command in (VoiceCommand.COPY, VoiceCommand.NEXT, VoiceCommand.UNREADABLE):
                    person = {}
                    if command == VoiceCommand.COPY:
                        person = self._storage.get_previous_copied()
                        person['info'] = speech
                    elif command == VoiceCommand.UNREADABLE:
                        person['info'] = speech
                    elif command == VoiceCommand.NEXT:
                        person['info'] = speech

                    person['scan_link'] = self._browser.current_url()

                    self._save(person)
                    person = {}

                    self._browser.click_next()
                    speech = get_voice_command()
                    command = self._to_command.get(speech)

                if command == VoiceCommand.DATA:
                    person['info'] = speech
                    continue
                else:
                    self._storage.dump()
                    print(f'Powiedziałeś {speech}, kończymy, zapisano {len(self._storage)} elementów, bye bye!')
                    print(f'Genei, 2019, Paweł Maciejski.')
                    break

            if field == 'scan_link':
                person[field] = self._browser.current_url()
                continue

            user_input = self._prompt(field)
            if user_input:
                user_input = user_input.capitalize()
            person[field] = self._autocomplete.fill_missing(field, value=user_input)

    @staticmethod
    def _welcome():
        print('\nWitaj w Genei, przygotowałeś skany z FS? Zaczynamy! ')
        print('Wprowadź dane pierwszej osoby.\n')
