#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    headers = {
        'content-type': 'application/json',
        'location': 'http://www.bing.com'
    }
    resp = make_response('<html>Hello</html>', 301)

    return resp, 301, headers
    # return '<html>Hello World!<html>'


app.run(host='127.0.0.1', port=81, debug=app.config['DEBUG'])
