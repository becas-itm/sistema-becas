from unittest.mock import patch

import pytest

from scraper.cache.key_hasher import Sha1KeyHasher


@pytest.fixture
def hasher():
    return Sha1KeyHasher()


class FakeHash:
    def hexdigest(self):
        return 'foo'


class TestHashingAlgorithm:
    def test_should_be_deterministic_between_calls(self, hasher):
        item_name = 'foo'
        hashed1 = hasher.hash(item_name)
        hashed2 = hasher.hash(item_name)
        assert hashed1 == hashed2

    @patch('hashlib.sha1', return_value=FakeHash())
    def test_should_use_sha1(self, sha1, hasher):
        assert hasher.hash('bar') == 'foo'
        assert sha1.called_with('bar')


class TestItemNameNormalization:
    def test_leading_spaces_are_stripped(self, hasher):
        assert hasher.hash('    foo  ') == hasher.hash('foo')

    def test_spaces_are_replaced(self, hasher):
        hashed = hasher.hash('foo bar')
        assert hashed == hasher.hash('foo   bar')
        assert hashed == hasher.hash('foo\t\n\nbar')
        assert hashed == hasher.hash('foo\t\n   \n    bar')

    def test_string_are_lower_case(self, hasher):
        hashed = hasher.hash('foo bar')
        assert hashed == hasher.hash('FOO BAR')
        assert hashed == hasher.hash('Foo Bar')
        assert hashed == hasher.hash('fOO bAR')
