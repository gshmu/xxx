#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests

from django.http import HttpResponse

__author__ = 'gshmu'


def index(request):

    return HttpResponse("500M free data at: /w/500M/name/phone_number/<br/><br/>replace your name and number, Good Luck!")


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