from etl.common.funding_type import FundingType


partial_words = set(('parcial', 'partial'))
complete_words = set(('completa', 'complete'))

def parse_funding_type(item: dict):
    if 'fundingType' not in item:
        return item

    funding_type = clean_string(item['fundingType'])

    if funding_type in partial_words:
        item['fundingType'] = FundingType.PARTIAL.value
    elif funding_type in complete_words:
        item['fundingType'] = FundingType.COMPLETE.value

    return item

def clean_string(string: str):
    return string.strip().lower()
