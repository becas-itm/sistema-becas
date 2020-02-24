from datetime import datetime


class ItemBuilder:
    def __init__(self):
        self._item = {}

    @classmethod
    def from_spider(cls, spider):
        builder = cls()
        builder._item['spider'] = dict(name=spider.name, extractedAt=datetime.utcnow())
        return builder

    def add_name(self, name):
        self._item['name'] = name
        return self

    def add_description(self, description):
        self._item['description'] = description
        return self

    def add_deadline(self, deadline):
        self._item['deadline'] = deadline
        return self

    def add_funding_type(self, funding):
        self._item['fundingType'] = funding
        return self

    def build(self):
        return self._item
