from itm.shared.domain.errors import DomainError


class ScholarshipError(DomainError):
    def __init__(self, scholarship_id):
        self.scholarship_id = scholarship_id
        self.code = self.CODE


class IncompleteError(ScholarshipError):
    CODE = 'SCHOLARSHIP_INCOMPLETE'


class StateError(ScholarshipError):
    CODE = 'SCHOLARSHIP_STATE'


class ExpiredError(ScholarshipError):
    CODE = 'SCHOLARSHIP_EXPIRED'
