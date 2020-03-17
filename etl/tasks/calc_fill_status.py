from itm.publishing.domain.scholarship import Scholarship, FillStatus


def current_status(doc):
    scholarship = Scholarship.from_document(doc)
    return FillStatus.COMPLETE if scholarship.is_complete else FillStatus.INCOMPLETE


def calc_fill_status(item):
    item['fillStatus'] = current_status(item).value
    return item
