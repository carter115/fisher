#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, current_app, request, Request

# 应用上下文 对象 Flask
# 请求上下文 对象 Request
# Flask AppContext
# Request RequestContext
# 离线应用、单元测试

app = Flask(__name__)

# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# print(a, d)
# ctx.pop()

# 实现了上下文协议的对象使用with
# 上下文管理器
with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']
    print(a, d)


class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print('process exception')
        else:
            print('no exception')
        print('close resource connect')
        # return True
        # return False

    def query(self):
        print('query data')


try:
    with MyResource() as resource:
        1 / 0
        resource.query()
except Exception as e:
    print(e)
