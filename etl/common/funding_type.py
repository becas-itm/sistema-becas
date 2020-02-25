from enum import Enum, unique


@unique
class FundingType(Enum):
    COMPLETE = 'COMPLETE'

    PARTIAL = 'PARTIAL'
