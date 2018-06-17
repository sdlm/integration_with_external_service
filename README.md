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
class ExampleSchema(Schema):
    first_field = fields.String()
    second_field = fields.String()
    date_field = fields.Date()

...

schema = ExampleSchema()
validated_data = schema.dump(raw_data)
```