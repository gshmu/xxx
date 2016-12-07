#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import time
import requests
from datetime import datetime

from django.http import HttpResponse

__author__ = 'gshmu'


def index(request):

    # return HttpResponse("Shaanxi 500M. <br>/w/500M/name/phone_number/<br/><br/>replace your name and number, Good Luck!")
    return HttpResponse("API Pro")


def timestamp(request, sec):
    return HttpResponse("%s" % datetime.fromtimestamp(int(sec)).strftime("%Y-%m-%d %H:%M:%S"))


def ip_addr(request):
    return HttpResponse("%s" % request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR'))


def null(request):
    return HttpResponse(status=444)


def M500(request, name, phone):
    # 国务院
    # url = 'http://appapns.www.gov.cn/govdata/survey.shtml'
    # data = {
    #     'answer': "{}",
    #     'name': name,
    #     'phone': phone,
    #     'format': "script",
    #     'callback': 'surveycallback'
    # }
    # response = requests.post(url, data=data, timeout=180)
    # 陕西省
    _a = 'http://dt.shxca.gov.cn/checkAnswer.php'
    xlh = {'data': '[{"id":258,"answer":1}]'}

    url = 'http://dt.shxca.gov.cn/getFlows.php'
    data = {
        'name': name,
        'phone': phone,
        'xlh': json.loads(requests.post(_a, data=xlh, timeout=180).text)["message"]
    }
    response = requests.post(url, data=data, timeout=180)
    return HttpResponse("Learn to control your desire, to respect your power, and to regard the authority you have.")
    # if json.loads(response.text)["code"] == 1:
    #     return HttpResponse("Only ShaanXi.<br>It's  OK...<br><br> Response: %s" % response.text)
    #
    # return HttpResponse("ERROR!!!<br><br>  name: %s<br>  phone: %s<br><br>%s" % (name, phone, response.text))


def random_20x(request):
    now = datetime.now().time()
    # code = 200 if (now.hour + now.minute / 20) % 2 == 0 else 451
    code = 200 + (now.hour + now.minute / 20) % 2
    return HttpResponse(status=code)
