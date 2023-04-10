from pyodbc import Connection, Cursor, Row #Types
from pyodbc import connect #Methods
from SQL.MSSQLDriver import MSSQLDriver
from SQL.QustionMapper import QuestionMapper

driver = MSSQLDriver("localhost", "Gameshow")
result = driver.get("SELECT * FROM dbo.TestQuestions", QuestionMapper())

for question in result:
    print(question)