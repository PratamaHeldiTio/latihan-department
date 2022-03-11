from abc import ABC, abstractmethod

class DepartmentRepository(ABC, object):

    @abstractmethod
    def get_all(self, filters): pass

    @abstractmethod
    def create(self, adict): pass

    @abstractmethod
    def update_by_id(self, adict): pass

    @abstractmethod
    def delete_by_id(self, adict): pass

    @abstractmethod
    def get_total(self, adict): pass
