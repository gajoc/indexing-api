from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from utils.constants import UserAction, DATETIME_FORMAT


class IEntitySchema(Schema):
    created_utc = fields.DateTime(required=True)
    info = EnumField(UserAction, required=True)
    scan_link = fields.URL(required=True)

    class Meta:
        dateformat = DATETIME_FORMAT


class MilitaryEntityFamilySearchSchema(IEntitySchema):
    surname = fields.Str(required=True, attribute='nazwisko', data_key='nazwisko')
    born_year = fields.Str(required=True, attribute='data_ur', data_key='data_ur')
