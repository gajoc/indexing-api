from typing import Union, Dict, Sequence, Mapping

from marshmallow import fields, post_dump

from model.ientity import IEntitySchema


class MilitaryEntityFamilySearchSchema(IEntitySchema):
    surname = fields.Str(data_key='nazwisko')
    born_year = fields.Str(data_key='data_ur')

    @post_dump
    def make_surname_proper(self, data: Union[Dict, Sequence], **kwargs) -> Dict:
        if isinstance(data, Mapping) and 'nazwisko' in data:
            data['nazwisko'] = data['nazwisko'].title()
        return data
