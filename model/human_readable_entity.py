from typing import Dict, Union, Sequence

from marshmallow import post_dump

from model.fs_military_entity import MilitaryEntityFamilySearchSchema
from utils.misc import asterisk_string


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
