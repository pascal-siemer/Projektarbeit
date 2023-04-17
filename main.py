from Definitions.Game import Game
from Definitions.Score import Score
from Messaging.Endpoints.EndpointRouter import EndpointRouter
from Messaging.Endpoints.QuestionHandler import QuestionHandler
from Messaging.Endpoints.RoundHandler import RoundHandler
from Messaging.Endpoints.ScoreHandler import ScoreHandler
from Database.Reader.QuestionSQLReader import QuestionSQLReader
from Database.Driver.SqliteDriver import SqliteDriver
from WebsocketHandler import WebsocketHandler
import asyncio


sql_driver = SqliteDriver("./Database/database.db")
#sql_driver = MSSQLDriver("localhost", "Gameshow")
sql_reader = QuestionSQLReader(sql_driver)

questions = sql_reader.read()
scores = [Score("peter", 900), Score("brammen", 1500), Score("chris", 1500), Score("sep", 600), Score("jay", 1200)]
game = Game(questions, scores)

router = EndpointRouter()
router.add("Question", QuestionHandler(game))
router.add("Score", ScoreHandler(game))
router.add("Round", RoundHandler(game))

address = "localhost"
port = 8123
socket = WebsocketHandler(router)

print("listening...")
asyncio.run(socket.listen(address, port))

