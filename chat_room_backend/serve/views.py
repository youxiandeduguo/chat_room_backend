from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from . import models
import os
import sys
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
    user_name=request.GET.get('user_name')
    print('||',user_name)
    if user_name =='':
        return HttpResponse("用户名不能为空")
    return HttpResponse("登录成功")




