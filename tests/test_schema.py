import datetime
import unittest

from faker import Faker

from serializer import fields
from serializer.schema import Schema


class TestSchema(Schema):
    first_field = fields.String()
    second_field = fields.String()
    date_field = fields.Date()


class SchemaTest(unittest.TestCase):

    def setUp(self):
        self.fake = Faker()

    def test_basic(self):
        schema = TestSchema()
        timestamp = datetime.datetime.utcnow()
        data = {
            'first_field': self.fake.word(),
            'second_field': self.fake.word(),
            'date_field': timestamp.isoformat(),
            'trash_field': self.fake.word(),
        }
        result = schema.dump(data)
        expected = {
            'first_field': data['first_field'],
            'second_field': data['second_field'],
            'date_field': timestamp.date()
        }
        self.assertEqual(result, expected)
