from abc import abstractmethod, ABC
from itertools import cycle
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.mic import await_for_voice_command
from utils.storage import Storage


class IGeneiApp(ABC):
    @abstractmethod
    def run(self, **config):
        pass


class GeneiAppSelenium(IGeneiApp):
    '''
    chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"
    '''

    def __init__(self, **config):
        self._config = config
        self._driver = self._init_browser_driver()
        self._user_input_cache = {}
        self._storage = Storage(config['common']['storage_dir'])

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

    def _autocomplete_missing(self, field, value, use_fields):
        if field not in use_fields:
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
                speech_command = await_for_voice_command()

                # click next scan until copy, skip or mark as unreadable is needed
                while speech_command in ('copy', 'skip', 'unreadable'):
                    person = {}
                    if speech_command == 'copy':
                        person = self._storage.get_previous_copied()
                    elif speech_command == 'unreadable':
                        person['warning'] = 'unreadable'
                    elif speech_command == 'skip':
                        person['warning'] = 'skipped'

                    person['scan_link'] = self._driver.current_url
                    self._save(person)
                    person = {}

                    self._click_next_page()
                    speech_command = await_for_voice_command()

                if speech_command == 'next':
                    continue
                else:
                    self._storage.dump()
                    print(f'you said {speech_command}, dumped {len(self._storage)} items, bye bye!')
                    break

            if field == 'scan_link':
                person[field] = self._driver.current_url
                continue

            user_input = self._prompt(field)
            if user_input:
                user_input = user_input.capitalize()
            person[field] = self._autocomplete_missing(
                field, value=user_input, use_fields=('birth_date',))

    def _click_next_page(self):
        e = self._driver.find_element_by_css_selector(self._config['click_button'])
        e.click()
        print(f'next page was auto clicked')