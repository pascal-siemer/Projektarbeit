import asyncio

from Database.Driver.SqliteDriver import SqliteDriver
from Database.Reader.QuestionSQLReader import QuestionSQLReader
from Definitions.Game import Game
from Messaging.Endpoints.EndpointRouter import EndpointRouter
from Messaging.Endpoints.NextQuestionHandler import NextQuestionHandler
from Messaging.Endpoints.PlayerHandler import PlayerHandler
from Messaging.Endpoints.QuestionHandler import QuestionHandler
from Messaging.MessageReceiver import MessageReceiver
from Messaging.MessageSender import MessageSender
from Messaging.WebsocketListener import WebsocketListener


address = "localhost"
port = 8123
game = Game()
sql_driver = SqliteDriver("./Database/database.db")
question_reader = QuestionSQLReader(sql_driver)
router = EndpointRouter()
sender = MessageSender()
receiver = MessageReceiver(router)
listener = WebsocketListener(receiver)

game.questions = question_reader.read()
game.question_index = 0
router.add("Question", QuestionHandler(game, sender))
router.add("NextQuestion", NextQuestionHandler(game, sender))
router.add("Init", PlayerHandler(game, sender))

print("listening...")
asyncio.run(listener.listen(address, port))










"""

--- OLD CODE ---
sql_driver = SqliteDriver("./Database/database.db")
#sql_driver = MSSQLDriver("localhost", "Gameshow")
sql_reader = QuestionSQLReader(sql_driver)

questions = sql_reader.read()
scores = [Score("peter", 900), Score("brammen", 1500), Score("chris", 1500), Score("sep", 600), Score("jay", 1200)]
game = Game(questions, scores)

router = EndpointRouter()
router.add("Question", NextQuestionHandler(game))
router.add("Score", ScoreHandler(game))
router.add("Round", RoundHandler(game))

address = "localhost"
port = 8123
socket = WebsocketHandler(router)

print("listening...")
asyncio.run(socket.listen(address, port))

"""