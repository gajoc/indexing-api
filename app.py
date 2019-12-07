from abc import abstractmethod, ABC
from itertools import cycle
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import VoiceCommand
from utils.mic import await_for_voice_command, get_voice_command
from utils.storage import Storage


class IGeneiApp(ABC):
    @abstractmethod
    def run(self, **config):
        pass


class GeneiAppSelenium(IGeneiApp):

    def __init__(self, **config):
        self._config = config
        self._driver = self._init_browser_driver()
        self._user_input_cache = {}
        self._storage = Storage(config['common']['storage_dir'])
        self._to_command = config['voice_command_translator'][config['voice_language']]

    def _init_browser_driver(self):
        chrome_options = Options()
        config = self._config['selenium']['chrome']
        for key, value in config['experimentalOptions'].items():
            chrome_options.add_experimental_option(key, value)
        driver = webdriver.Chrome(config['driverPath'], chrome_options=chrome_options)
        return driver

    def _save(self, data):
        print('saving...')
        pprint(data, indent=4)
        self._storage.add(data)
        print('saved!')
        print('')

    @staticmethod
    def _prompt(text):
        line = input(f'{text}: ')
        return None if line == '' else line

    def _get_fields_generator(self):
        fields = self._config['fields']
        return cycle(fields)

    def _autocomplete_missing(self, field, value, autocomplete):
        if field not in autocomplete:
            return value
        if value:
            self._user_input_cache[field] = value
            return value
        return self._user_input_cache.get(field, value)

    def run(self):
        fields = self._get_fields_generator()
        person = {}

        while True:
            field = next(fields)

            if field == 'save':
                self._save(person)
                person = {}
                self._click_next_page()
                speech = get_voice_command()
                command = self._to_command.get(speech)

                # click next scan until copy, next or mark as unreadable is needed
                while command in (VoiceCommand.COPY, VoiceCommand.NEXT, VoiceCommand.UNREADABLE):
                    person = {}
                    if command == VoiceCommand.COPY:
                        person = self._storage.get_previous_copied()
                        person['warning'] = speech
                    elif command == VoiceCommand.UNREADABLE:
                        person['warning'] = speech
                    elif command == VoiceCommand.NEXT:
                        person['warning'] = speech

                    person['scan_link'] = self._driver.current_url
                    self._save(person)
                    person = {}

                    self._click_next_page()
                    speech = get_voice_command()
                    command = self._to_command.get(speech)

                if command == VoiceCommand.DATA:
                    continue
                else:
                    self._storage.dump()
                    print(f'you said {speech}, dumped {len(self._storage)} items, bye bye!')
                    break

            if field == 'scan_link':
                person[field] = self._driver.current_url
                continue

            user_input = self._prompt(field)
            if user_input:
                user_input = user_input.capitalize()
            person[field] = self._autocomplete_missing(
                field, value=user_input, autocomplete=self._config.get('autocomplete_fields', ()))

    def _click_next_page(self):
        e = self._driver.find_element_by_css_selector(self._config['click_button'])
        e.click()
        print(f'next page was auto clicked')
