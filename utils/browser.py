from typing import Dict

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Browser:

    def __init__(self, user_browser: str, next_button: str, previous_button: str, config: Dict):
        self._config = config[user_browser]
        chrome_options = Options()
        for key, value in self._config['experimentalOptions'].items():
            chrome_options.add_experimental_option(key, value)
        driver = webdriver.Chrome(self._config['driverPath'], chrome_options=chrome_options)
        self._driver = driver
        self._next_button = next_button
        self._previous_button = previous_button

    def current_url(self) -> str:
        return self._driver.current_url

    def click_next(self) -> None:
        e = self._driver.find_element_by_css_selector(self._next_button)
        e.click()
        print(f'Kliknąłem automatycznie następną stronę')

    def click_previous(self) -> None:
        e = self._driver.find_element_by_css_selector(self._previous_button)
        e.click()
        print(f'Kliknąłem automatycznie poprzednią stronę')
