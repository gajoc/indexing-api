from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from utils.constants import UserAction, DATETIME_FORMAT


class IEntitySchema(Schema):
    created_utc = fields.DateTime(required=True)
    info = EnumField(UserAction, required=True)
    scan_link = fields.URL(required=True)

    class Meta:
        dateformat = DATETIME_FORMAT
