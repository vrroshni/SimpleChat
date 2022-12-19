import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self): #initial request from client
        self.accept()
        
        self.send(text_data=json.dumps({
            'type':'Connection Established',
            'message':'You are now connected'
        }))
        
    def receive(self,text_data): #when we receive message from client
        pass
        
    def disconnect(self,close_code): #client disconnect from the consumer
        pass
        