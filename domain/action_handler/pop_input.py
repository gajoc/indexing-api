from domain.action_handler.iaction_handler import IActionHandler
from utils.browser import Browser
from utils.constants import BrowserAction
from utils.storage import Storage


class PopPreviousEntity(IActionHandler):

    def handle(self, storage: Storage, browser: Browser, action: BrowserAction):
        entity = storage.pop_previous()
        human_view = self.human_readable_schema.dump(entity) if entity else {}
        getattr(browser, action.value)()
        print(human_view)
