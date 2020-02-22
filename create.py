from typing import Dict

from app import GeneiAppSelenium
from domain.controller.scenario import ScenarioControllers
from model.fs_military_entity import MilitaryEntityFamilySearchSchema
from utils.browser import create_browser
from utils.constants import GenealogyService, BrowserButtons, InteractionMethod, GenealogyDocumentType
from utils.logger import GeneiLogger
from utils.storage import Storage


def create_app(service: GenealogyService, config: Dict):
    GeneiLogger.set_logger(config["log_filename"])
    storage = Storage(storage_dir=config.get("storage_dir", "data"),
                      schema=MilitaryEntityFamilySearchSchema(),
                      storage_entities_limit=config.get("storage_entities_limit", 0))
    buttons = BrowserButtons.get(service)
    browser = create_browser(next_button=buttons.NEXT.value,
                             prev_button=buttons.PREV.value,
                             config=config["browser"])
    controller_cls = ScenarioControllers.get(InteractionMethod.KEYBOARD, GenealogyDocumentType.MILITARY_RECORD)
    controller = controller_cls(browser, storage)
    return GeneiAppSelenium(controller)
