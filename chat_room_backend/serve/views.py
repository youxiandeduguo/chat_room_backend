from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from . import models

# Create your views here.



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

