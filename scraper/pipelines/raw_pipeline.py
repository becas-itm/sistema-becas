from itm.documents import connect_db, RawScholarship


class RawPipeline:
    @classmethod
    def from_crawler(cls, crawler):
        connect_db()
        return cls()

    def process_item(self, item, spider):
        RawScholarship.create(item)
