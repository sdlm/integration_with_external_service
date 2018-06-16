from abstract_classes import Field
from utils import from_iso_date, from_iso_datetime


class String(Field):

    def deserialize(self, value: str):
        return value


class Date(Field):

    def deserialize(self, value: str):
        return from_iso_date(value)


class DateTime(Field):

    def deserialize(self, value: str):
        return from_iso_datetime(value)
