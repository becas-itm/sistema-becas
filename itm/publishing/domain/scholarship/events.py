from datetime import datetime


class ScholarshipApproved:
    def __init__(self, scholarship_id, timestamp):
        self._scholarship_id = scholarship_id
        self._timestamp = timestamp

    @classmethod
    def fire(cls, scholarship_id):
        return cls(scholarship_id, datetime.utcnow())

    @property
    def scholarship_id(self):
        return self._scholarship_id

    @property
    def timestamp(self):
        return self._timestamp
