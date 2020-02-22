from collections import defaultdict
from typing import DefaultDict, Dict

from model.fs_military_entity import MilitaryEntityFamilySearchSchema
from model.ientity import IEntitySchema
from utils.constants import GenealogyService, GenealogyDocumentType


class ModelSchemas:

    mapper: DefaultDict[GenealogyService, Dict[GenealogyDocumentType, IEntitySchema]] = defaultdict(dict)

    @classmethod
    def register(cls, service: GenealogyService, document_type: GenealogyDocumentType, schema: IEntitySchema) -> None:
        cls.mapper[service][document_type] = schema

    @classmethod
    def get(cls, service: GenealogyService, document_type: GenealogyDocumentType) -> IEntitySchema:
        return cls.mapper[service][document_type]


ModelSchemas.register(GenealogyService.FAMILY_SEARCH, GenealogyDocumentType.MILITARY_RECORD,
                      MilitaryEntityFamilySearchSchema)
