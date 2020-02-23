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
