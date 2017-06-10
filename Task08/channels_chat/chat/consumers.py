from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http
from models import ChatMessage, Chat_room, Chat_group, GroupChatMessage
from channels import Channel
import json


#Connected to websocket.connect
@channel_session_user_from_http
def ws_connect(message):

    print("ws_connect")

    try:
        group = Chat_group.objects.get(global_group=True)
    except:
        group = Chat_group.objects.create(global_group=True)
        group.users.add(message.user)
    
    Group("chat-group-global").add(message.reply_channel)

    message.reply_channel.send({'accept': True})


# connected to websocet.receive 
@channel_session
def ws_message(message):

    print("ws_message")
    
    payload = json.loads(message['text'])
    payload['reply_channel'] = message.content['reply_channel']
    Channel("chat.receive").send(payload)

    
# connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    print("LEAVE CHAT") 
    #Group("chat-%s" % message.channel_session['room']).discard(message.reply_channel)
    #Group("chat-1-2").discard(message.reply_channel)

@channel_session
def chat_join(message):
    room = message['room']
    Group("chat-%s" % room).add(message['reply_channel'])
    
    roomObj = Chat_room.objects.get(pk=room)

    content = json.dumps({
        "room_background": roomObj.background_color,
        "room_title": roomObj.title,
        "room": room,
        "content_type": "joined"
    })
    message.reply_channel.send({
        "text": content
    })
    
    print("JOIN CHAT")

@channel_session
def group_chat_join(message):

    room = message['room']
    Group("chat-group-%s" % room).add(message['reply_channel'])
    
    roomObj = Chat_group.objects.get(pk=room)

    content = json.dumps({
        "room_background": roomObj.background_color,
        "room_title": roomObj.title,
        "room": room,
        "content_type": "joined_a_group"
    })
    message.reply_channel.send({
        "text": content
    })
    
    print("JOIN GROUP CHAT")

def chat_leave(message):
    print("LEAVE CHAT") 
    room = message['room']
    print(room)
    Group("chat-%s" % room).discard(message.reply_channel)

@channel_session_user
def chat_send(message):
    print("SEND CHAT")
    room = message['room']
    msg_type = message['message_type']
    msg_content = message['content_type']

    content = json.dumps({
        "message_type": msg_type,
        "content_type": message['content_type'],
        "message": message['message'],
        "room": room,
        "username": str(message.user),
        "user_id": message.user.id,
        "user_image": str(message.user.profile.profile_photo)
    })
      
    if msg_type == "private":
        roomObj = Chat_room.objects.get(pk=room)
        ChatMessage.objects.create(
            room=roomObj,
            message=message['message'],
            user=message.user,
            username=message.user.username,
            user_image=str(message.user.profile.profile_photo),
            content_type=msg_content
        )
        # Broadcast to listening sockets\
        print("SENDING TO PRIVATE GROUP")
        Group("chat-%s" % room).send({
            "text": content
        })
    elif msg_type == "global":
        groupObj = Chat_group.objects.get(global_group=True)
        GroupChatMessage.objects.create(
            group=groupObj,
            message=message['message'],
            user=message.user,
            username=message.user.username,
            user_image=str(message.user.profile.profile_photo),
            content_type=msg_content
        )
        # Broadcast to listening sockets
        print("SENDING TO GLOBAL CHAT")
        Group("chat-group-%s" % room).send({
            "text": content
        })
    elif msg_type == "group":
        groupObj = Chat_group.objects.get(pk=room)
        GroupChatMessage.objects.create(
            group=groupObj,
            message=message['message'],
            user=message.user,
            username=message.user.username,
            user_image=str(message.user.profile.profile_photo),
            content_type=message['content_type']
        )
        # Broadcast to listening sockets
        print("SENDING TO GROUP CHAT")
        Group("chat-group-%s" % room).send({
            "text": content
        })