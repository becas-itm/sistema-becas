from datetime import datetime


def add_timestamps(item: dict):
    item['createdAt'] = datetime.utcnow()
    return item
