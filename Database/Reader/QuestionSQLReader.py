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
                [Questions]
            """

    def __init__(self, driver: ISqlDriver):
        self.__driver = driver

    def read(self):
        return self.__driver.get(self.query, QuestionMapper())

