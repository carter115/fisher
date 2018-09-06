#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import jsonify, request, render_template, flash, current_app
import json

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection

from . import web


@web.route('/book/search', methods=['GET', 'POST'])
def search():
    print('start search ...')
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
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        # r = json.dumps(books, default=lambda o: o.__dict__)
        # return r
        # return jsonify(books)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books, form=form)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    pass


@web.route('/test')
def test():
    r = {
        'name': None,
        'age': 18
    }
    # data['age']
    r1 = {

    }
    flash('hello,qiyue', category='error')
    flash('hello, jiuyue', category='warning')
    # 模板 html
    return render_template('test.html', data=r, data1=r1)


@web.route('/test1')
def test1():
    print(id(current_app))
    from flask import request
    from app.libs.none_local import n
    print(n.v)
    n.v = 2
    print('-----------------')
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print('-----------------')
    return ''
