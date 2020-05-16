import pickle


FILE_MODE_WRITE_BINARY = 'wb'
FILE_MODE_READ_BINARY = 'rb'


class PickleCacheLoader:
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        with self.open_file(FILE_MODE_WRITE_BINARY) as file:
            pickle.dump(data, file)

    def load(self):
        try:
            with self.open_file(FILE_MODE_READ_BINARY) as file:
                return pickle.load(file)
        except FileNotFoundError:
            return {}

    def open_file(self, modes):
        return open(self.filename, modes, encoding='utf8')
