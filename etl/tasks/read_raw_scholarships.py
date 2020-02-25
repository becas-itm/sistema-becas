from scraper.spiders import SpiderName
from itm.documents import RawScholarship


def read_raw_scholarhips(spider: str):
    def run_task():
        search = RawScholarship.search() \
            .filter('term', **{'spider.name': spider.value})

        for item in search.scan():
            # Attach id to item
            item_id = item.meta.id
            item = item.to_dict()
            item['id'] = item_id

            yield item

    return run_task
