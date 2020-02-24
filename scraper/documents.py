from elasticsearch_dsl import Document, Text, Date, Object, Keyword

from etl.config.elasticsearch import connect_db


class RawScholarship(Document):
    name = Text(required=True)

    description = Text()

    deadline = Text()

    fundingType = Text()

    spider = Object(
        required=True,
        properties={
            'name': Keyword(required=True),
            'extractedAt': Date(required=True),
        },
    )

    class Index:
        name = 'raw_scholarships'

    @staticmethod
    def create(item):
        scholarship = RawScholarship(**item)
        scholarship.save()

def init_indexes():
    connect_db()
    RawScholarship.init()

if __name__ == '__main__':
    init_indexes()
