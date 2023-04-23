from abc import ABC, abstractmethod

from Interfaces.ISqlDriver import ISqlDriver


class ISqlReader(ABC):

    @abstractmethod
    def __init__(self, driver: ISqlDriver):
        pass

    @abstractmethod
    def read(self):
        pass
