from pyodbc import Cursor
from Definitions.Question import Question
from Interfaces.ISqlDataMapper import ISqlDataMapper


class QuestionMapper(ISqlDataMapper):

    @staticmethod
    def map(cursor: Cursor) -> list[Question]:
        result = []
        for row in cursor:
            question = Question(row[1], row[2:6], row[6])
            result.append(question)
        return result
