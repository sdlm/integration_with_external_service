import datetime
import unittest

from faker import Faker

from serializer import fields
from serializer.schema import Schema


class TestSchema(Schema):
    first_field = fields.String()
    second_field = fields.String()
    date_field = fields.Date()


class TestSchemaWithNestedField(Schema):
    some_field = fields.String()
    nested_field = fields.Nested(TestSchema)


class SchemaTest(unittest.TestCase):

    def setUp(self):
        self.fake = Faker()
        self.timestamp = datetime.datetime.utcnow()

    def get_test_data(self):
        return {
            'first_field': self.fake.word(),
            'second_field': self.fake.word(),
            'date_field': self.timestamp.isoformat(),
            'trash_field': self.fake.word(),
        }

    def get_expected_data(self, raw_data):
        expected = raw_data.copy()
        del expected['trash_field']
        expected['date_field'] = self.timestamp.date()
        return expected

    def test_basic(self):
        schema = TestSchema()

        raw_data = self.get_test_data()
        result = schema.load(raw_data)

        expected = self.get_expected_data(raw_data)
        self.assertEqual(result, expected)

    def test_nested_field(self):
        schema = TestSchemaWithNestedField()
        raw_nested_data = self.get_test_data()

        raw_data = {
            'some_field': self.fake.word(),
            'nested_field': raw_nested_data
        }
        result = schema.load(raw_data)

        expected = raw_data.copy()
        expected['nested_field'] = self.get_expected_data(raw_nested_data)
        self.assertEqual(result, expected)
