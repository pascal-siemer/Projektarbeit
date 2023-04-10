from abc import ABC, abstractmethod
from SQL.MSSQLDriver import MSSQLDriver


class ISQLReader(ABC):

    @abstractmethod
    def __init__(self, driver: MSSQLDriver):
        pass

    @abstractmethod
    def read(self):
        pass
