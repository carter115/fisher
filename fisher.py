#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, make_response, jsonify

app = Flask(__name__)
print('id为 {} 的app实例化'.format(id(app)))
app.config.from_object('config')

from app.web import book

if __name__ == '__main__':
    print('id为 {} 启动'.format(id(app)))
    app.run(host='127.0.0.1', port=5000, debug=app.config['DEBUG'])
