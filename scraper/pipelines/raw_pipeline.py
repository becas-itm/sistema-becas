import os

from elasticsearch_dsl.connections import create_connection

from scraper.documents import RawScholarship


class RawPipeline:
    @classmethod
    def from_crawler(cls, crawler):
        # Setup default connection
        host = os.getenv('ELASTIC_HOST', '127.0.0.1')
        create_connection(alias='default', hosts=[host])

        return cls()

    def process_item(self, item, spider):
        RawScholarship.create(item)
