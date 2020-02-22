from domain.controller.icontroller import IController
from domain.controller.scenario.fs_military_records import FamilySearchMilitaryRecordsKeyboardCommand, \
    FamilySearchMilitaryRecordsVoiceCommand
from utils.constants import InteractionMethod, GenealogyDocumentType


class ScenarioControllers:
    @staticmethod
    def get(method: InteractionMethod, document_type: GenealogyDocumentType) -> IController:
        mapper = {
            InteractionMethod.KEYBOARD: {
                GenealogyDocumentType.MILITARY_RECORD: FamilySearchMilitaryRecordsKeyboardCommand
            },
            InteractionMethod.VOICE: {
                GenealogyDocumentType.MILITARY_RECORD: FamilySearchMilitaryRecordsVoiceCommand
            },
        }
        return mapper[method][document_type]
