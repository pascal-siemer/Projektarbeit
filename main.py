from Definitions.Game import Game
from Definitions.Score import Score
from Endpoints.EndpointRouter import EndpointRouter
from Endpoints.QuestionHandler import QuestionHandler
from Endpoints.RoundHandler import RoundHandler
from Endpoints.ScoreHandler import ScoreHandler
from SQL.Driver.MssqlDriver import MSSQLDriver
from SQL.Reader.QuestionSQLReader import QuestionSQLReader
from SQL.Driver.SqliteDriver import SqliteDriver
from WebsocketHandler import WebsocketHandler
import asyncio


sql_driver = SqliteDriver("./Database/database.db")
#sql_driver = MSSQLDriver("localhost", "Gameshow")
sql_reader = QuestionSQLReader(sql_driver)

questions = sql_reader.read()
scores = [Score("peter", 900), Score("brammen", 1500), Score("chris", 1500), Score("sep", 600), Score("jay", 1200)]
game = Game(questions, scores)

router = EndpointRouter()
router.add(QuestionHandler.identifier, QuestionHandler(game))
router.add(ScoreHandler.identifier, ScoreHandler(game))
router.add(RoundHandler.identifier, RoundHandler(game))

address = "localhost"
port = 8123
socket = WebsocketHandler(router)

print("listening...")
asyncio.run(socket.listen(address, port))

