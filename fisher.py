#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, make_response
from helper import is_isbn_or_key
from yushu_book import YuShuBook

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    q: 关键字 或者 isbn
    page:
    # isbn isbn13 13个0到9的数字组成
    # isbn10 10个0到9数字组成，含有一些 '-'
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        YuShuBook.search_by_isbn(q)
    else:
        YuShuBook.search_by_keyword(q)
    pass


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
