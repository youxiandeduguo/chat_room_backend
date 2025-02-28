from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from . import models
import os
import sys
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'chat_room_backend')))


users=[]





def test(request):
    return HttpResponse("成功")



def select_friend(request):
    friend=[]
    user_id=request.GET.get('id')
    data=models.Friend.objects.filter(id1=user_id)
    for item in data.values('id2'):
        friend.append({'id':item['id2'],'name':models.User.objects.get(id=item['id2']).name})

    data=models.Friend.objects.filter(id2=user_id)
    for item in data.values('id1'):
        friend.append({'id':item['id1'],'name':models.User.objects.get(id=item['id1']).name})


    return JsonResponse(friend,safe=False)

def login(request):
    # ip_address=request.GET.get('ip_address')
    username=request.GET.get('username')
    print(username)
    if username =='':
        return HttpResponse("用户名不能为空",status=400)
    
    user=models.User.objects.filter(name=username)
    if user.exists():
        user_info={
            'id':user.first().id,
            'name':user.first().name
        }
        return JsonResponse(user_info)
    else: 
        return HttpResponse("用户不存在",status=404)

def get_history(request):
    message_list=[]
    username=request.GET.get('username')
    to_name=request.GET.get('to_name')
    messages=models.Messages.objects.filter((Q(user1=username)&Q(user2=to_name))|(Q(user1=to_name)&Q(user2=username)))
    for message in messages.values('user1','user2','Message','time'):
        if message['user1']==username:
            message_list.append({'sender':username,'message':message['Message'],'time':message['time']})
        else:
            message_list.append({'sender':to_name,'message':message['Message'],'time':message['time']})
    
    return JsonResponse(message_list,safe=False)


def get_group_history(request):
    message_list=[]
    name=request.GET.get('name')
    messages=models.Group_Messages.objects.filter(name=name)
    for message in messages.values('user','Message','time'):
        message_list.append({'sender':message['user'],'message':message['Message'],'time':message['time']})
    
    return JsonResponse(message_list,safe=False)

@csrf_exempt
def append_history(request):
    data = json.loads(request.body)
    sender = data.get('sender')
    message = data.get('message')
    receiver = data.get('receiver')
    time = data.get('time')
    print(data,'||')
    models.Messages.objects.create(
        user1=sender,
        user2=receiver,
        Message=message,
        time=time
    )
    return JsonResponse({'message': '消息保存成功'}, status=200)


@csrf_exempt
def append_group_history(request):
    data = json.loads(request.body)
    name = data.get('name')
    user = data.get('user')
    message = data.get('message')
    time = data.get('time')
    print(data,'|||')
    models.Group_Messages.objects.create(
        name=name,
        user=user,
        Message=message,
        time=time
    )
    return JsonResponse({'message': '消息保存成功'}, status=200)

def get_private_info(request):
    message_list=[]
    username=request.GET.get('username')
    new_user_message=[]
    messages=models.Messages.objects.filter(Q(user1=username)|Q(user2=username))
    flag=False
    for message in messages.values('user1','user2','Message','time'):
        if message['user1']==username:
            flag=False
            for item in new_user_message:
                if item.get('sender') == message['user2']:
                    item['message']=message['Message']
                    flag=True
            if not flag:
                new_user_message.append({"sender":message['user2'],"message":message['Message'],'time':message['time']})
        elif message['user2']==username:
            flag=False
            for item in new_user_message:
                if item.get('sender') == message['user1']:
                    item['message']=message['Message']
                    flag=True
            if not flag:
                new_user_message.append({"sender":message['user1'],"message":message['Message'],'time':message['time']})
    print(new_user_message)
    return JsonResponse(new_user_message,safe=False)

def add_friend(request):
    message_list=[]
    username=request.GET.get('username')
    to_user=request.GET.get('to_user')
    models.Friend_Request.objects.create(
        user1=username,
        user2=to_user,
    )
    
    return HttpResponse("请求发送成功")


def check_friend_request(request):
    friend_requests_list=[]
    username=request.GET.get('username')
    friend_requests=models.Friend_Request.objects.filter(Q(user1=username)|Q(user2=username))
    for friend_req in friend_requests.values('user1','user2'):
        if friend_req['user2']==username:
            friend_requests_list.append(friend_req['user1'])
    return JsonResponse(friend_requests_list,safe=False)

def accept_friend_request(request):
    message_list=[]
    username=request.GET.get('username')
    to_user=request.GET.get('to_user')
    print(username,'||',to_user)
    friend_requests=models.Friend_Request.objects.filter(Q(user1=to_user)&Q(user2=username))
    
    
    friend_requests.delete()
    id1=models.User.objects.get(name=username).id
    id2=models.User.objects.get(name=to_user).id
    print(id1,'||',id2)
    models.Friend.objects.create(
        id1=id1,
        id2=id2,
    )
    
    return HttpResponse("接受好友请求成功")









