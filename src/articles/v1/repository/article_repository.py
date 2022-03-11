from abc import ABC, abstractmethod

class ArticleRepository(ABC, object):

    @abstractmethod
    def get_all(self, filters): pass

    # @abstractmethod
    # def get_by_id(self, pk): pass

    @abstractmethod
    def create(self, adict): pass

    @abstractmethod
    def update_by_id(self, adict): pass

    @abstractmethod
    def delete_by_id(self, adict): pass

    @abstractmethod
    def get_total(self, adict): pass
