from unittest.mock import MagicMock

import pytest

from scrapy.exceptions import DropItem

from scraper.pipelines import DuplicateItemsPipeline
from scraper.cache import SpiderCache, Sha1KeyHasher, PickleCacheLoader


@pytest.fixture
def loader(tmp_path):
    filename = tmp_path / 'spider_cache.test'
    return PickleCacheLoader(filename)


class TestProcessItem:
    def test_new_item_should_be_cached(self, loader):
        cache = SpiderCache(Sha1KeyHasher())
        pipeline = DuplicateItemsPipeline(cache, loader)

        item = {'spider': {'name': 'foo'}, 'name': 'bar'}
        pipeline.process_item(item, spider=None)

        assert cache.exists('foo', 'bar')

    def test_item_should_be_returned_if_cached(self, loader):
        cache = SpiderCache(Sha1KeyHasher())
        pipeline = DuplicateItemsPipeline(cache, loader)

        item = {'spider': {'name': 'foo'}, 'name': 'bar'}
        assert item == pipeline.process_item(item, spider=None)

    def test_cached_item_should_throw(self, loader):
        cache = SpiderCache(Sha1KeyHasher())
        item = {'spider': {'name': 'foo'}, 'name': 'bar'}
        cache.add(item['spider']['name'], item['name'])

        pipeline = DuplicateItemsPipeline(cache, loader)

        with pytest.raises(DropItem):
            pipeline.process_item(item, spider=None)


@pytest.fixture
def fake_crawler(tmp_path):
    filename = tmp_path / 'spider_cache.test'

    class FakeCrawler:
        def __init__(self):
            self.settings = {'CACHE_ITEMS_FILENAME': filename}

    return FakeCrawler()


class TestFromCrawlerFactory:
    def test_should_return_a_pipeline_instance(self, fake_crawler):
        pipeline = DuplicateItemsPipeline.from_crawler(fake_crawler)
        assert isinstance(pipeline, DuplicateItemsPipeline)


def test_close_spider_cache_should_be_save(fake_crawler):
    pipeline = DuplicateItemsPipeline.from_crawler(fake_crawler)
    loader = pipeline.loader

    save_mock = MagicMock()
    loader.save = save_mock

    pipeline.close_spider(spider=None)

    assert save_mock.called
