from Database.Mapper.QustionMapper import QuestionMapper
from Definitions.Question import Question
from Interfaces.ISqlDriver import ISqlDriver
from Interfaces.ISqlReader import ISqlReader


class QuestionSqlReader(ISqlReader):

    __query = """
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

    def read(self) -> list[Question]:
        return self.__driver.get(self.__query, QuestionMapper())

