from scrapy.exceptions import DropItem

from scraper.cache import SpiderCache, Sha1KeyHasher, PickleCacheLoader


class DuplicateItemsPipeline:
    def __init__(self, cache: SpiderCache, loader: PickleCacheLoader):
        self.cache = cache
        self.loader = loader

    @classmethod
    def from_crawler(cls, crawler):
        filename = crawler.settings['CACHE_ITEMS_FILENAME']
        loader = PickleCacheLoader(filename)
        cache = SpiderCache(Sha1KeyHasher(), loader.load())
        return cls(cache, loader)

    def process_item(self, item, spider):
        if not self.cache.exists(item['spider']['name'], item['name']):
            self.cache.add(item['spider']['name'], item['name'])
            return item

        raise DropItem

    def close_spider(self, spider):
        self.loader.save(self.cache.cache_by_spider)
