# Задача пакета
Предполагается что данные мы уже [как-то получили](https://github.com/sdlm/simplest_grabber.git). Далее нам нужно:
- выделить интересующие нас данные
- провалидировать данные
- собрать данные для создания инстанса модели
- создать инстанс модели

Идея реализации взята из библиотеки [marshmallow](https://marshmallow.readthedocs.io/en/latest/).

```
raw_data -> ExternalEndpointSerializer -> validated_data
validated_data -> ModelSerializer -> instance
```

# Пример использования
```
class SomeSchema(Schema):
    first_field = fields.String()
    second_field = fields.String()
    date_field = fields.Date()
    nested_field = fields.Nested(OtherSchema)

...

schema = SomeSchema()
validated_data = schema.load(raw_data)
```

```
class ModelSchema(Schema):
    ...

    @classmethod
    def post_load(cls, data):
        return Model(**data)

...

schema = ModelSchema()
model_instance = schema.load(data)
```