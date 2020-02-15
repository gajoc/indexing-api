from typing import Dict

from app import GeneiAppSelenium
from domain.scenario.fs_military_records import FamilySearchMilitaryRecordsVoiceCommand, \
    FamilySearchMilitaryRecordsKeyboardCommand
from model.fs_military_entity import MilitaryEntityFamilySearchSchema
from utils.browser import Browser
from utils.constants import GenealogyService, BrowserButtons
from utils.storage import Storage


def create_app(service: GenealogyService, config: Dict):
    storage = Storage(storage_dir=config.get("storage_dir", "data"),
                      schema=MilitaryEntityFamilySearchSchema(),
                      storage_entities_limit=config.get("storage_entities_limit", 0))
    buttons = BrowserButtons.get(service)
    browser = Browser(user_browser=config["browser"]["name"],
                      next_button=buttons.NEXT.value,
                      previous_button=buttons.PREV.value,
                      config={"chrome": config["browser"]})
    controller_types = {
        'voice': FamilySearchMilitaryRecordsVoiceCommand,
        'keyboard': FamilySearchMilitaryRecordsKeyboardCommand,

    }
    controller = controller_types.get("keyboard")(browser, storage)
    return GeneiAppSelenium(controller)
