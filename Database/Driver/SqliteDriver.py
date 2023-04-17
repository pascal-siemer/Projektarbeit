import sqlite3
from typing import Any
from Interfaces.ISqlDataMapper import ISqlDataMapper
from Interfaces.ISqlDriver import ISqlDriver


class SqliteDriver(ISqlDriver):

    def __init__(self, file_path: str):
        self.connection = sqlite3.connect(file_path)

    def get(self, query: str, mapper: ISqlDataMapper) -> list[Any]:
        cursor = self.connection.cursor()
        cursor.execute(query)
        return mapper.map(cursor)
