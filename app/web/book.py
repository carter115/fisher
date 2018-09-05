#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import jsonify
from fisher import app
from helper import is_isbn_or_key
from yushu_book import YuShuBook

print('id为 {} 的app注册路由'.format(id(app)))


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    q: 关键字 或者 isbn
    page:
    # isbn isbn13 13个0到9的数字组成
    # isbn10 10个0到9数字组成，含有一些 '-'
    """
    # app.add_url_rule('url', view_func='search', endpoint='search')
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
