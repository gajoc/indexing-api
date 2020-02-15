from typing import Dict

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Browser:

    def __init__(self, driver, next_button: str, previous_button: str):
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


def create_browser(next_button: str, prev_button: str, config: Dict) -> Browser:
    driver = None
    if config["name"] == "chrome":
        chrome_options = Options()
        for param in config['experimentalOptions'].items():
            chrome_options.add_experimental_option(*param)
        driver = webdriver.Chrome(config['driverPath'], chrome_options=chrome_options)
    else:
        raise RuntimeError("browser from config not supported")
    return Browser(driver, next_button, prev_button)
