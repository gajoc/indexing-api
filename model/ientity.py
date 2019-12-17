from marshmallow import Schema, fields, post_dump
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


class MilitaryShortEntityFamilySearchSchema(MilitaryEntityFamilySearchSchema):

    @post_dump
    def short_entity(self, data, **kwargs):
        raise NotImplementedError('Implementation from misc.short_print needed here. Use it in project.')
        pass
