#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import print_function

import os
import string
import random

__author__ = 'gshmu'


# Get ascii Characters numbers and punctuation (minus quote characters as they could terminate string).
chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '')

SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(50)])

expired_key = os.environ.get('SECRET_KEY', "")
os.environ.setdefault("SECRET_KEY", SECRET_KEY)
print(os.environ.get('SECRET_KEY', expired_key) != expired_key)
