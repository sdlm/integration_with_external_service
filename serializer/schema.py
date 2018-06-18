from typing import Union


class Schema:

    @classmethod
    def load(cls, data: Union[dict, list], many: bool = False):
        if many:
            assert isinstance(data, list)
            return [cls.__load_data(x) for x in data]

        assert isinstance(data, dict)
        return cls.__load_data(data)

    @classmethod
    def __load_data(cls, data: dict) -> dict:
        result = {}
        props = cls.__get_props()
        for prop_name in props:
            value = data.get(prop_name)
            if not value:
                continue
            field = getattr(cls, prop_name)
            result[prop_name] = field.deserialize(value)

        return cls.__try_make_object(data)

    @classmethod
    def __get_props(cls):
        return [x for x in cls.__dict__.keys() if not x.startswith('__')]

    @classmethod
    def __try_make_object(cls, data: dict):
        obj = cls.post_load(data)
        if obj is None:
            return data
        return obj

    @classmethod
    def post_load(cls, data: dict):
        return None
