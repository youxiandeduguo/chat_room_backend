from django.shortcuts import render,HttpResponse

# Create your views here.



def test(request):
    return HttpResponse("成功")



def select_friend(request):
    user_id=request.GET.get('id')
    return HttpResponse(f"{user_id}")

