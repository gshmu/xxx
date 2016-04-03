#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests

from django.http import HttpResponse

__author__ = 'gshmu'


def index(request):

    return HttpResponse("Hello, world. You're at the polls index.")


def M500(request, name, phone):

    url = 'http://appapns.www.gov.cn/govdata/survey.shtml'
    data = {
        'answer': "{}",
        'name': name,
        'phone': phone,
        'format': "script",
        'callback': 'surveycallback'
    }
    # response = requests.post(url, data=data)
    # if response.status_code == 200:
    #     return HttpResponse("It's  OK...<br><br> Response: %s" % response.text)

    return HttpResponse("ERROR!!!<br><br>  name: %s<br>  phone: %s" % (name, phone))