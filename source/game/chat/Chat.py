import uuid


class Chat:

    def __init__(self, chat_id: uuid):
        self.chat_id = chat_id

    def broadcast(self):
        """Broadcasts the message for all users in the chat"""
        pass

    def private_message(self, player_id):
        """Sends a private message to a user in the chat"""
