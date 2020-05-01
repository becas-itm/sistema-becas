import pytest

from scraper.cache.pickle_cache_loader import PickleCacheLoader


@pytest.fixture
def loader(tmp_path):
    filename = tmp_path / 'spider_cache.test'
    return PickleCacheLoader(filename.as_posix())


def test_save_should_serialize_data(loader):
    data = {'foo': 'bar'}
    loader.save(data)
    assert loader.load() == data


def test_load_initial_data_if_file_not_exist(loader):
    assert loader.load() == {}
