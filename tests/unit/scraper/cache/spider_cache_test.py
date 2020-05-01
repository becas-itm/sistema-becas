from unittest.mock import MagicMock

import pytest

from scraper.cache.key_hasher import Sha1KeyHasher
from scraper.cache.spider_cache import SpiderCache


@pytest.fixture
def cache():
    return SpiderCache(Sha1KeyHasher())


def test_add_new_item(cache):
    spider = 'foo'
    item = 'bar'
    assert not cache.exists(spider, item)
    cache.add(spider, item)
    assert cache.exists(spider, item)


def test_item_name_is_hashed():
    hasher = Sha1KeyHasher()
    hasher.hash = MagicMock()
    cache = SpiderCache(hasher)
    cache.add('_', 'foo')
    assert hasher.hash.called_with('foo')
