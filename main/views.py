# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, HttpResponse
from main.models import Person
import re
import json 
from datetime import datetime
from datetime import date 
from django.conf import settings

# Create your views here.

def home(request):
    dic = _get_dic()
    dic['persons'] = Person.objects.all()
    now = datetime.now()
    dic['persons'] = sorted(dic['persons'], key = lambda person: (now - _date2datetime(person.start_date)).total_seconds() 
            / (_date2datetime(person.end_date) - _date2datetime(person.start_date)).total_seconds(), reverse = True)
    person = dic['persons'][3]
    return render(request, 'home.html', dic)

@csrf_exempt
def regist(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            start = request.POST['start']
            end = request.POST['end']
        except Exception as e:
            return HttpResponseBadRequest()

        if len(name) >= 10:
            return _response_json({'code' : 1, 'message' : u'이름은 10자 이하여야 합니다.'})
        if len(name) == 0:
            return _response_json({'code' : 2, 'message' : u'이름을 입력해주세요.'})

        try:
            start_dt = datetime.strptime(start, '%Y-%m-%d')
            end_dt = datetime.strptime(end, '%Y-%m-%d')
            cur_dt = datetime.now()
        except Exception as e:
            return _response_json({'code' : 3, 'message' : u'날짜 형식이 잘못되었습니다.'})
        if start_dt >= end_dt:
            return _response_json({'code' : 4, 'message' : u'시작일이 종료일보다 빠릅니다.'})
        if cur_dt >= end_dt:
            return _response_json({'code' : 5, 'message' : u'이미 지나간 이벤트입니다.'})
        if cur_dt <= start_dt:
            return _response_json({'code' : 6, 'message' : u'아직 시작되지 않은 이벤트입니다.'})
        if (end_dt - start_dt).total_seconds() > (100 * 3600 * 24 * 365):
            return _response_json({'code' : 7, 'message' : u'너무 긴 이벤트입니다.'})
        p = Person(name = name, start_date = start_dt, end_date = end_dt)
        p.save()
        return _response_json({'code' : 0, 'message' : u'등록 성공!'})
    else:
        return HttpResponseBadRequest()

def _response_json(dic):
    return HttpResponse(json.dumps(dic))

def _get_dic():
    dic = {}
    dic['base_url'] = settings.BASE_URL
    return dic

def _date2datetime(d):
    return datetime.combine(d, datetime.min.time())
