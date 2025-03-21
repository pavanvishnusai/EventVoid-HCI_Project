from channels.generic.websocket import AsyncWebsocketConsumer
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings

class ChatBotConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        chatbot = ChatBot(**settings.CHATTERBOT)
        response = chatbot.get_response(text_data)

        await self.send(text_data=response.text)