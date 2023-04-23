from abc import ABC, abstractmethod


class ISqlDataMapper(ABC):

    @staticmethod
    @abstractmethod
    def map(cursor):
        pass
