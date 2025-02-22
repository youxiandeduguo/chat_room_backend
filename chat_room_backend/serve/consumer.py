import json
from channels.generic.websocket import AsyncWebsocketConsumer

online_users={}

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.user_name = self.scope['url_route']['kwargs']['user_name']
        print(self.room_name)

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name,
        )
        
        if self.room_name not in online_users:
            online_users[self.room_name]=[]
            online_users[self.room_name].append(self.user_name)

        else:
            online_users[self.room_name].append(self.user_name)

        await self.channel_layer.group_send(
            self.room_name,  
            {
                "type": "update_users", 
                "users": online_users[self.room_name],     
            }
        )
        
        await self.accept()

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name,
        )
        online_users[self.room_name].remove(self.user_name)
        
        await self.channel_layer.group_send(
            self.room_name,  
            {
                "type": "update_users", 
                "users": online_users[self.room_name],     
            }
        )



    async def receive(self, text_data):

        data = json.loads(text_data)
        message = data['message']
        sender=data['sender']

        await self.channel_layer.group_send(
            self.room_name,  
            {
                "type": "group_chat", 
                "sender":sender,
                "message": message,     
            }
        )

    async def group_chat(self, event):

        message = event['message']
        sender = event['sender']
        await self.send(text_data=json.dumps({
            'sender':sender,
            'message': message
        }))

    async def update_users(self, event):
        users = event['users']
        await self.send(text_data=json.dumps({
            'type': 'users',
            'users': users,
        }))
