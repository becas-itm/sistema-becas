import elasticsearch_dsl as dsl


class Scholarship(dsl.Document):
    class Index:
        name = 'scholarships'

    @property
    def id(self):
        return self.meta.id

    name = dsl.Text(required=True)

    description = dsl.Text()

    deadline = dsl.Date()

    state = dsl.Keyword(required=True)

    createdAt = dsl.Date(required=True)

    approval = dsl.Object(
        properties={
            'approvedAt': dsl.Date(required=True),
        },
    )

    denial = dsl.Object(
        properties={
            'deniedAt': dsl.Date(required=True),
            'reason': dsl.Text(required=True),
        },
    )

    def to_dict(self):
        doc = super().to_dict()
        doc.update({'id': self.id})
        return doc
