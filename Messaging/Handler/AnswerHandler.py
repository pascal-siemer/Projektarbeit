from Definitions.Connection import Connection
from Definitions.Game import Game
from Definitions.Message import Message
from Interfaces.IMessageHandler import IMessageHandler
from Messaging.MessageSender import MessageSender
from Tools.JsonConverter import JsonConverter


class AnswerHandler(IMessageHandler):

    """
    AnswerHandler: Nimmt einen Antwort-Index an und gibt zurück, ob die Antwort richtig ist.
    """

    def __init__(self, game: Game, sender: MessageSender):
        self.__game = game
        self.__sender = sender

    async def handle_message(self, connection: Connection, message: Message) -> None:
        current_question = self.__game.questions[self.__game.question_index]
        is_answer_correct = message.value == current_question.indexCorrect
        json_of_is_answer_correct = JsonConverter.deserialize(is_answer_correct)
        answer = Message(message.handler, json_of_is_answer_correct)
        await self.__sender.send(connection, answer)
