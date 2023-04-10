from Interfaces.ISQLReader import ISQLReader
from SQL.MSSQLDriver import MSSQLDriver
from SQL.QustionMapper import QuestionMapper


class QuestionSQLReader(ISQLReader):

    query = """
            select 
                [ID],
                [Prompt],
                [Answer0],
                [Answer1],
                [Answer2],
                [Answer3],
                [IndexCorrect]
            from
                [dbo].[TestQuestions]
            """

    def __init__(self, driver: MSSQLDriver):
        self.driver = driver

    def read(self):
        return self.driver.get(self.query, QuestionMapper())

