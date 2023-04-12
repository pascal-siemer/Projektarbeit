from SQL.Driver.MssqlDriver import MSSQLDriver
from SQL.Mapper.QustionMapper import QuestionMapper

driver = MSSQLDriver("localhost", "Gameshow")
result = driver.get("SELECT * FROM dbo.TestQuestions", QuestionMapper())

for question in result:
    print(question)