import json

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse, QueryDict
from django.shortcuts import render

from interface.models import Interface
from .models import Project

# Create your views here.
def hello(request):
    return HttpResponse("es hello world")

def project_list(request):
    '''
    获取项目列表
    :param request:
    :return:
    '''
    #获取当前页，默认第一页
    page = request.GET.get('page',1)
    #获取每页显示条数
    page_size = request.GET.get('pageSize',2)
    #查询数据
    projects = Project.objects.all()
    #使用分页器进行分页，每页显示条数
    paginator = Paginator(projects,page_size)
    #定位到第几页
    page_of_project = paginator.page(page)

    project_list = []
    for project in page_of_project:
        project_list.append(project.to_dict())
    data = {
        'code': 200,
        'msg': '查询成功',
        'data': project_list
    }
    return JsonResponse(data)

def project(request,pid):
    '''
    根据id获取项目
    :param request:
    :param pid:
    :return:
    '''
    project = Project.objects.get(pk=pid)
    if request.method == 'GET':
        data = {
            'code': 200,
            'msg': '查询成功',
            'data': project.to_dict()
        }
        return JsonResponse(data)

    if request.method == 'DELETE':
        project.delete()
        data = {
            'code': 200,
            'msg': '删除成功',
            'data': None
        }
        return JsonResponse(data)

    if request.method == 'PUT':
        put = QueryDict(request.body)
        put_str = list(put.items())[0][0]  # 将获取的QueryDict对象转换为str 类型
        put_dict = eval(put_str)  # 将str类型转换为字典类型
        project.name = put_dict.get('name')
        project.host = put_dict.get('host')
        project.desc = put_dict.get('desc')
        project.save()
        data = {
            'code': 200,
            'msg': '更新成功',
            'data': project.to_dict()
        }
        return JsonResponse(data)


def add_project(request):
    body = json.loads(request.body)
    project = Project()
    project.name = body['name']
    project.host = body['host']
    project.desc = body['desc']
    project.save()
    data = {
        'code': 200,
        'msg': '添加成功',
        'data': project.to_dict()
    }
    return JsonResponse(data)


def interfases(request,pid):
    '''
    根据pid获取所有的接口
    :param request:
    :param pid:
    :return:
    '''
    if request.method == "GET":
        inters = Interface.objects.filter(project=pid)
        result = []
        for i in inters:
            result.append(i.to_dict())
        data = {
            'code': 200,
            'msg': '查询成功',
            'data': result
        }
        return JsonResponse(data)