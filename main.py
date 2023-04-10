from Definitions.Game import Game
from Definitions.Score import Score
from Endpoints.EndpointRouter import EndpointRouter
from Endpoints.QuestionHandler import QuestionHandler
from Endpoints.ScoreHandler import ScoreHandler
from SQL.MSSQLDriver import MSSQLDriver
from SQL.QuestionSQLReader import QuestionSQLReader
from WebsocketHandler import WebsocketHandler
import asyncio

sql_server_address = "localhost"
sql_database = "Gameshow"
sql_driver = MSSQLDriver(sql_server_address, sql_database)
sql_reader = QuestionSQLReader(sql_driver)

questions = sql_reader.read()
scores = [Score("peter", 900),
          Score("brammen", 1500),
          Score("chris", 1500),
          Score("sep", 600),
          Score("jay", 1200)]
game = Game(questions, scores)

router = EndpointRouter()
router.add("Question", QuestionHandler(game))
router.add("Score", ScoreHandler(game))

address = "localhost"
port = 8123
socket = WebsocketHandler(router)
asyncio.run(socket.listen(address, port))
