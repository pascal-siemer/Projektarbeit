from abc import ABC, abstractmethod

from Interfaces.ISqlDataMapper import ISqlDataMapper


class ISqlDriver(ABC):

    @abstractmethod
    def get(self, query: str, mapper: ISqlDataMapper):
        pass