from datetime import datetime


class ScholarshipApproved:
    def __init__(self, scholarship_id, timestamp):
        self.scholarship_id = scholarship_id
        self.timestamp = timestamp

    @classmethod
    def fire(cls, scholarship_id):
        return cls(scholarship_id, datetime.utcnow())


class ScholarshipDenied:
    def __init__(self, scholarship_id, reason, timestamp):
        self.scholarship_id = scholarship_id
        self.reason = reason
        self.timestamp = timestamp

    @classmethod
    def fire(cls, scholarship_id, reason):
        return cls(scholarship_id, reason, datetime.utcnow())
