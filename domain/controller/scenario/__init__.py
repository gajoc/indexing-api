from collections import defaultdict
from typing import DefaultDict, Dict

from domain.controller.icontroller import IController
from domain.controller.scenario.fs_military_records import FamilySearchMilitaryRecordsKeyboardCommand, \
    FamilySearchMilitaryRecordsVoiceCommand
from utils.constants import InteractionMethod, GenealogyDocumentType


class ScenarioControllers:

    mapper: DefaultDict[InteractionMethod, Dict[GenealogyDocumentType, IController]] = defaultdict(dict)

    @classmethod
    def register(cls, method: InteractionMethod, document_type: GenealogyDocumentType, scenario: IController) -> None:
        cls.mapper[method][document_type] = scenario

    @classmethod
    def get(cls, method: InteractionMethod, document_type: GenealogyDocumentType) -> IController:
        return cls.mapper[method][document_type]


ScenarioControllers.register(InteractionMethod.KEYBOARD, GenealogyDocumentType.MILITARY_RECORD,
                             FamilySearchMilitaryRecordsKeyboardCommand)
ScenarioControllers.register(InteractionMethod.VOICE, GenealogyDocumentType.MILITARY_RECORD,
                             FamilySearchMilitaryRecordsVoiceCommand)
