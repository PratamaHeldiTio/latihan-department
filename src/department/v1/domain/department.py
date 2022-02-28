class Department(object):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.status = kwargs.get('status')
        self.created_at = kwargs.get('created_at')
        self.modified_at = kwargs.get('modified_at')


    @classmethod
    def from_dict(self, adict):
        department = Department(**{
            "id": adict.get('id'),
            "name": adict.get('name'),
            "status": adict.get('status'),
            "created_at": adict.get('created_at'),
            "modified_at": adict.get('modified_at'),
         })

        return department
