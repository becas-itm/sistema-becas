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

    def add_original_id(self, original_id):
        if 'sourceDetails' in self._item:
            self._item['sourceDetails']['id'] = original_id
        else:
            self._item['sourceDetails'] = {'id': original_id}
        return self

    def add_url(self, url):
        if 'sourceDetails' in self._item:
            self._item['sourceDetails']['url'] = url
        else:
            self._item['sourceDetails'] = {'url': url}
        return self

    def add_deadline(self, deadline):
        self._item['deadline'] = deadline
        return self

    def add_funding_type(self, funding):
        self._item['fundingType'] = funding
        return self

    def add_country(self, country):
        self._item['country'] = country
        return self

    def add_language(self, language):
        self._item['language'] = language.value
        return self

    def build(self):
        return self._item
