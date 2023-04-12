from abc import ABC, abstractmethod
from SQL.Driver.MssqlDriver import MSSQLDriver


class ISqlReader(ABC):

    @abstractmethod
    def __init__(self, driver: MSSQLDriver):
        pass

    @abstractmethod
    def read(self):
        pass
