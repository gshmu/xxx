#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
from datetime import datetime

from django.http import HttpResponse

__author__ = 'gshmu'


def index(request):

    return HttpResponse("China Phone 500M free data is out of date, see you.")


def timestamp(request, sec):
    return HttpResponse("%s" % datetime.fromtimestamp(int(sec)).strftime("%Y-%m-%d %H:%M:%S"))


def ip_addr(request):
    return HttpResponse("%s" % request.META.get('REMOTE_ADDR'))


def M500(request, name, phone):

    url = 'http://appapns.www.gov.cn/govdata/survey.shtml'
    data = {
        'answer': "{}",
        'name': name,
        'phone': phone,
        'format': "script",
        'callback': 'surveycallback'
    }
    response = requests.post(url, data=data, timeout=180)
    if response.status_code == 200:
        return HttpResponse("It's  OK...<br><br> Response: %s" % response.text)

    return HttpResponse("ERROR!!!<br><br>  name: %s<br>  phone: %s" % (name, phone))
