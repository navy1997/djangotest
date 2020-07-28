import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from seri.models import Student
from seri.serializers import StudentSerializer


def test(request):
    #序列化单个对象
    id = request.GET.get("id")
    student = Student.objects.get(pk=id)
    s = StudentSerializer(student)

    print(s.data)
    data = {
        'code': 200,
        'msg': '查询成功',
        'data':s.data
    }
    return JsonResponse(data)

def test2(request):
    #序列化一个集合
    students = Student.objects.all()
    s = StudentSerializer(students,many=True)

    print(s.data)
    data = {
        'code': 200,
        'msg': '查询成功',
        'data':s.data
    }
    return JsonResponse(data)

def test3(request):
    #请求序列化
    body = json.loads(request.body)
    s = StudentSerializer(data=body)
    t = s.create(body)
    print(t)
    return JsonResponse({})
