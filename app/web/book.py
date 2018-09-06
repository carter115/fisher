#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import jsonify, request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel

from . import web


@web.route('/test')
def test1():
    from flask import request
    from app.libs.none_local import n
    print(n.v)
    n.v = 2
    print('-' * 35)
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print('-' * 35)
    return ''


@web.route('/book/search')
def search():
    """
    q: 关键字 或者 isbn
    page:
    # isbn isbn13 13个0到9的数字组成
    # isbn10 10个0到9数字组成，含有一些 '-'
    """
    # q = request.args['q']
    # page = request.args['page']
    # args = request.args.to_dict()
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            data = YuShuBook.search_by_isbn(q)
            result = BookViewModel.package_single(data, q)
        else:
            data = YuShuBook.search_by_keyword(q, page)
            result = BookViewModel.package_collection(data, q)
        return jsonify(result)
    else:
        return jsonify(form.errors)
