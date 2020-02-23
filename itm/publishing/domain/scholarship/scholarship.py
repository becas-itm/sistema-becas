import uuid


class Id:
    UUID_VERSION = 4

    def __init__(self, value: uuid.UUID):
        if value.version != Id.UUID_VERSION:
            raise TypeError(f'{value!r} is not a valid {Id.__name__}')

        self._value = value

    @property
    def value(self):
        return str(self._value)

    @classmethod
    def generate(cls):
        return cls(uuid.uuid4())

    @classmethod
    def from_string(cls, string: str):
        return cls(uuid.UUID(string, version=cls.UUID_VERSION))


class StringValueObject:
    def __init__(self, value: str):
        self._set_value(value)

    @property
    def value(self):
        return self._value

    def _set_value(self, value: str):
        if not isinstance(value, str):
            raise TypeError(f'{value!r} is not a valid {self.__class__.__name__}')

        if value == '':
            raise ValueError(f'{self.__class__.__name__} must not be empty')

        if len(value) > self.MAX_CHARACTERS:
            raise ValueError(f'{self.__class__.__name__} must contain up to '
                             f'{self.MAX_CHARACTERS} characters')

        self._value = value


class Name(StringValueObject):
    MAX_CHARACTERS = 250


class Description(StringValueObject):
    MAX_CHARACTERS = 500
