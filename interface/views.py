from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from interface.models import Interface


def hello(request):
    return HttpResponse("interface hello world")

def interfaces(request):
    inters = Interface.objects.all()
    print(inters)
    result = []
    for i in inters:
        result.append(i.to_dict())
    data = {
        'code': 200,
        'msg': '用例查询成功',
        'data': result
    }
    return JsonResponse(data)

