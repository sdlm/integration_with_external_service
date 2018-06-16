import abc


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
