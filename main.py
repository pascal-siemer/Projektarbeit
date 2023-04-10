from Definitions.Game import Game
from Definitions.Score import Score
from Endpoints.EndpointRouter import EndpointRouter
from Endpoints.QuestionHandler import QuestionHandler
from Endpoints.ScoreHandler import ScoreHandler
from SQL.MSSQLDriver import MSSQLDriver
from SQL.QustionMapper import QuestionMapper
from WebsocketHandler import WebsocketHandler
import asyncio

game = Game()


address = "localhost"
port = 8123



sql_server_address = "localhost"
database = "Gameshow"
sql_driver = MSSQLDriver(sql_server_address, database)

sql_query_get_questions = """
select 
    [ID],
    [Prompt],
    [Answer0],
    [Answer1],
    [Answer2],
    [Answer3],
    [IndexCorrect]
from
    [Gameshow].[dbo].[TestQuestions]
"""

game.questions = sql_driver.get(sql_query_get_questions, QuestionMapper())

game.scores = [
    Score("peter", 900),
    Score("brammen", 1500),
    Score("chris", 1500),
    Score("sep", 600),
    Score("jay", 1200),
]



router = EndpointRouter()
router.add("Question", QuestionHandler(game))
router.add("Score", ScoreHandler(game))
socket = WebsocketHandler(router)

asyncio.run(socket.listen(address, port))
