import abc
from typing import Union


class Grabber:

    @abc.abstractmethod
    def load_data(self) -> Union[dict, list]:
        """
        Получить данные из внешнего источника.
        """
        pass


class Mapper:
    """
    под капотом marshmallow
    """

    @abc.abstractmethod
    def clean_data(self, data: dict) -> dict:
        """
        Очистить данные(убрать всё не нужное), провалидировать поля.
        """
        pass

    @abc.abstractmethod
    def make_instances(self, data: dict):
        """
        Сгруппировать данные для создания/обновления инстансов моделей ORM.
        """
        pass


class Serializer:

    @abc.abstractmethod
    def create(self, data: dict):
        """
        Добавить запись в БД.
        """
        pass

    @abc.abstractmethod
    def update(self, data: dict):
        """
        Обновить запись в БД.
        """
        pass
