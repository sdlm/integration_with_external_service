# Задача пакета
Предполагается что данные мы уже [как-то получили](https://github.com/sdlm/simplest_grabber.git). Далее нам нужно:
- выделить интересующие нас данные
- провалидировать данные

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