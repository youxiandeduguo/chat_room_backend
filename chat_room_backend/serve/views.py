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

@csrf_exempt
def append_history(request):
    data = json.loads(request.body)
    user1 = data.get('user1')
    user2 = data.get('user2')
    new_messages = data.get('new_messages')









