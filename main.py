import asyncio

from Database.Driver.SqliteDriver import SqliteDriver
from Database.Reader.QuestionSqlReader import QuestionSqlReader
from Definitions.Game import Game
from Messaging.Handler.AnswerHandler import AnswerHandler
from Messaging.Handler.NextQuestionHandler import NextQuestionHandler
from Messaging.Handler.QuestionHandler import QuestionHandler
from Messaging.Handler.RegistrationHandler import RegistrationHandler
from Messaging.Handler.RoundHandler import RoundHandler
from Messaging.Handler.ScoreHandler import ScoreHandler
from Messaging.Handler.SelectionHandler import SelectionHandler
from Messaging.MessageReceiver import MessageReceiver
from Messaging.MessageRouter import MessageRouter
from Messaging.MessageSender import MessageSender
from Messaging.WebsocketListener import WebsocketListener

#setup

address = "localhost"
port = 8123
game = Game()
sql_driver = SqliteDriver("./Database/database.db")
question_reader = QuestionSqlReader(sql_driver)
router = MessageRouter()
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