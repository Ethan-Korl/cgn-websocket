# consumer are like the channels version of django views
# except they do more then views(more than response to request). 
# they can initiate request with the client
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

# create first consumer
# reponsible for receving messages and broadcasting them to anyone 
# conected to this conusmer all in realtime

class ChatConsumer(WebsocketConsumer):
    # initial request that comes from the user
    def connect(self):
        # on connection we wanna set a groups name
        # normally this will be a dynamic data from the url
        # or whatever groups the use join
        # for testing purposes lets just have one groups "test"
        # and all users will eb added to this group
        self.room_group_name = "test"
        # using async_to_sync method 
        # we will access the channel layerData undefined
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
            # to add a users name to the group
            # we simply spycify the group name
        
            # and channel name(this will created automatically creted for each user)
           
            # 
        # )
        self.accept()
        # self.send(text_data=json.dumps({
        #     'type':'connection_establish',
        #     'message':'You are connected',
        # }))
        # return super().connect()


    # when we receive messages from the client
    def receive(self, text_data=None, bytes_data=None):
        # lets listen and get incoming messages
        text_message= json.loads(text_data);
        # print(text_data)
        # # print(text_message)Data undefined
        data = {'type':'chat_message', 'message':text_message['message']}
        # # now on recive lets broadacst the message 
        # # to every user in the group(which in this case a 'test')
        # still using async_to_sync
        async_to_sync(self.channel_layer.group_send)(self.room_group_name, data)
    
    def chat_message(self, event):
        message = event['message']
        # print(message)
        self.send(text_data=json.dumps({'type':'message','message':message}))
    # Message.objects.create(user=)
    # return super().receive(text_data, bytes_data)
    

    # what happen when user disconnect the conection
    # def disconnect(self, code):
    #     return super().disconnect(code)