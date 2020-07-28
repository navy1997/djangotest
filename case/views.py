from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
import json
# Create your views here.
from case.models import Case
from interface.models import Interface


def hello(request):
    return HttpResponse("case hello world")



def run(request,pid):
    '''
    根据项目pid运行子下用例
    :param request:
    :param pid:
    :return:
    '''
    ints = Interface.objects.filter(project=pid)
    ids = []
    case_run = []
    data = []
    for i in ints:
        ids.append(i.id)

    for interface_id in ids:
        cases = Case.objects.filter(interface=interface_id)
        for case in cases:
            case_run.append(case)
    for c in case_run:
        data.append(c.to_dict())

    for d in data:
        print(d["body"])
        print(json.loads(d["body"]))
        print(type(json.loads(d["body"])))

    d = {
        "data":data
    }
    return JsonResponse(d)