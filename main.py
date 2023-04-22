import asyncio

from Database.Driver.SqliteDriver import SqliteDriver
from Database.Reader.QuestionSQLReader import QuestionSQLReader
from Definitions.Game import Game
from Messaging.Endpoints.AnswerHandler import AnswerHandler
from Messaging.Endpoints.EndpointRouter import EndpointRouter
from Messaging.Endpoints.NextQuestionHandler import NextQuestionHandler
from Messaging.Endpoints.RegistrationHandler import RegistrationHandler
from Messaging.Endpoints.QuestionHandler import QuestionHandler
from Messaging.Endpoints.RoundHandler import RoundHandler
from Messaging.Endpoints.ScoreHandler import ScoreHandler
from Messaging.Endpoints.SelectionHandler import SelectionHandler
from Messaging.MessageReceiver import MessageReceiver
from Messaging.MessageSender import MessageSender
from Messaging.WebsocketListener import WebsocketListener
from Tools.Debouncer import Debouncer

#setup

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
router.add("Register", RegistrationHandler(game, sender))
router.add("Round_Start", RoundHandler(game, sender))
router.add("Round_End", RoundHandler(game, sender))
router.add("Selection", SelectionHandler(game))
router.add("Score", ScoreHandler(game, sender))
router.add("Answer", AnswerHandler(game, sender))

#start

print("listening...")
asyncio.run(listener.listen(address, port))