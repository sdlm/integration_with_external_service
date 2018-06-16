import abc
from typing import Union


class Grabber(abc.ABC):

    @abc.abstractmethod
    def load_data(self) -> Union[dict, list]:
        """
        Получить данные из внешнего источника.
        """
        pass


class Field(abc.ABC):
    name: str
    attribute: str

    def __init__(self, attribute: str = None):
        self.attribute = attribute

    @abc.abstractmethod
    def deserialize(self, value: str):
        """
        Преобразовать во внутренний тип.
        """
        pass
