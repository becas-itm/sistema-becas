class ApproveScholarship:
    def __init__(self, repository, id):
        self.repository = repository
        self.id = id

    def execute(self):
        return self.repository \
            .get_by_id(self.id) \
            .approve()
