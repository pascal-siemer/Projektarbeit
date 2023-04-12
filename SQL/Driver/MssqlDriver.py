from typing import Any

from pyodbc import Connection, Cursor, Row
from pyodbc import connect

from Interfaces.ISqlDataMapper import ISqlDataMapper
import sqlite3



class MSSQLDriver:

    """
    Implementierung des MSSQL-Drivers nach Microsoft-Empfehlung
    siehe: https://learn.microsoft.com/de-de/sql/connect/python/pyodbc/python-sql-driver-pyodbc?view=sql-server-ver16
    """

    def __init__(self, address: str, database: str):
        connection_parameters = self.create_connection_parameters(address, database)
        self.connection: Connection = connect(connection_parameters)

    @staticmethod
    def create_connection_parameters(address: str, database: str) -> str:
        return "Driver={ODBC Driver 17 for SQL Server};" \
               f"Server={address};" \
               f"Database={database}; " \
               f"Trusted_Connection=yes;"

    # maybe use generics: https://docs.python.org/3/library/typing.html
    def get(self, query: str, mapper: ISqlDataMapper) -> list[Any]:
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return mapper.map(cursor)
