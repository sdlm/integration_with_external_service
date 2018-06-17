from typing import Union

from .abstract_classes import Field
from .schema import Schema
from .utils import from_iso_date, from_iso_datetime


class String(Field):

    def deserialize(self, value: str):
        return value


class Date(Field):

    def deserialize(self, value: str):
        return from_iso_date(value)


class DateTime(Field):

    def deserialize(self, value: str):
        return from_iso_datetime(value)


class Nested(Field):
    related_schema = None

    def __init__(self, schema):
        assert issubclass(schema, Schema)
        self.related_schema = schema
        super().__init__()

    def deserialize(self, value: Union[dict, list], many: bool = False):
        return self.related_schema.load(data=value, many=many)
