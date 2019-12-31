from collections import Mapping
from typing import Dict, Union, Sequence

from marshmallow import Schema, fields, post_dump
from marshmallow_enum import EnumField

from utils.constants import UserAction, DATETIME_FORMAT
from utils.misc import asterisk_string


class IEntitySchema(Schema):
    created_utc = fields.DateTime(required=True)
    info = EnumField(UserAction, required=True)
    scan_link = fields.URL(required=True)

    class Meta:
        dateformat = DATETIME_FORMAT


class MilitaryEntityFamilySearchSchema(IEntitySchema):
    surname = fields.Str(data_key='nazwisko')
    born_year = fields.Str(data_key='data_ur')

    @post_dump
    def make_surname_proper(self, data: Union[Dict, Sequence], **kwargs) -> Dict:
        if isinstance(data, Mapping):
            data['nazwisko'] = data['nazwisko'].title()
        return data


class HumanReadableSchema(MilitaryEntityFamilySearchSchema):

    @staticmethod
    def human_readable_entity(entity: Dict, values_only: bool = True, link_parts: int = 5) -> Union[Dict, Sequence]:
        short_entity = entity.copy()
        short_entity.pop('created_utc')
        short_entity['scan_link'] = asterisk_string(short_entity['scan_link'], parts=link_parts)
        return tuple(short_entity.values()) if values_only else short_entity

    @post_dump
    def make_human_readable(self, data: Dict, **kwargs) -> Union[Dict, Sequence]:
        return self.human_readable_entity(entity=data)
