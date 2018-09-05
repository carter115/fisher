#!/usr/bin/env python
# -*- coding:utf-8 -*-
from . import web

@web.route('/user')
def login():
    return 'success.'