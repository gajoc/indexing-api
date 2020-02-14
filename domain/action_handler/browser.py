from domain.action_handler.iaction_handler import IActionHandler
from utils.browser import Browser
from utils.constants import BrowserAction


class BrowserHandler(IActionHandler):

    def handle(self, browser: Browser, action: BrowserAction):
        getattr(browser, action.value)()
