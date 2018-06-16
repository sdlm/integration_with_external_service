from typing import Union


class Schema:

    def dump(self, data: Union[dict, list], many: bool = False) -> Union[dict, list]:
        if many:
            assert isinstance(data, list)
            return [self.__dump_data(x) for x in data]

        assert isinstance(data, dict)
        return self.__dump_data(data)

    def __dump_data(self, data: dict) -> dict:
        result = {}
        props = self.__get_props()
        for prop_name in props:
            value = data.get(prop_name)
            if not value:
                continue
            field = self.__getattribute__(prop_name)
            result[prop_name] = field.deserialize(value)
        return result

    def __get_props(self):
        return [x for x in self.__class__.__dict__.keys() if not x.startswith('__')]
