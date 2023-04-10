from abc import ABC, abstractmethod
from pyodbc import Cursor

class ISqlDataMapper(ABC):

    @staticmethod
    def map(cursor: Cursor):
        pass