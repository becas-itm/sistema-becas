from datetime import datetime


ISO_FORMAT = '%Y-%m-%d'

class DateParser:
    def __init__(self, dateformat):
        self.dateformat = dateformat

    def __call__(self, date: str):
        return self.parse(date)

    def parse(self, date: str):
        return datetime.strptime(date, self.dateformat)
