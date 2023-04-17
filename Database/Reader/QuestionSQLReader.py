from Interfaces.ISqlDriver import ISqlDriver
from Interfaces.ISqlReader import ISqlReader
from Database.Mapper.QustionMapper import QuestionMapper


class QuestionSQLReader(ISqlReader):

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
                [TestQuestions]
            """

    def __init__(self, driver: ISqlDriver):
        self.driver = driver

    def read(self):
        return self.driver.get(self.query, QuestionMapper())

