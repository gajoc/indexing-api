from abc import abstractmethod, ABC
from itertools import cycle
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.mic import await_for_voice_command


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

    def _init_browser_driver(self):
        chrome_options = Options()
        config = self._config['selenium']['chrome']
        for key, value in config['experimentalOptions'].items():
            chrome_options.add_experimental_option(key, value)
        driver = webdriver.Chrome(config['driverPath'], chrome_options=chrome_options)
        return driver

    @staticmethod
    def _save(data):
        print('saving...')
        pprint(data, indent=4)
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
                speech_command = await_for_voice_command()
                if speech_command == 'Next':
                    self._click_next_page()
                    continue
                else:
                    print(f'you said {speech_command}, bye bye!')
                    break

            if field == 'scan_link':
                person[field] = self._driver.current_url
                continue

            user_input = self._prompt(field)
            person[field] = self._autocomplete_missing(
                field, value=user_input, use_fields=('birth_date',))

    def _click_next_page(self):
        e = self._driver.find_element_by_css_selector(self._config['click_button'])
        e.click()
