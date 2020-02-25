from itm.documents import Scholarship


def save_scholarship(item: dict):
    Scholarship.create(item)
