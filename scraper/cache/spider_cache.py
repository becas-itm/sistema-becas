class SpiderCache:
    def __init__(self, hasher, cache_by_spider=None):
        self.hasher = hasher
        self.cache_by_spider = cache_by_spider or {}

    def add(self, spider, item_name):
        cache = self._get_cache(spider)
        hashed = self._hash(item_name)
        cache.add(hashed)

    def exists(self, spider, item_name):
        return self._hash(item_name) in self._get_cache(spider)

    def _get_cache(self, spider):
        if spider in self.cache_by_spider:
            return self.cache_by_spider[spider]

        cache = set()
        self.cache_by_spider[spider] = cache
        return cache

    def _hash(self, string):
        return self.hasher.hash(string)
