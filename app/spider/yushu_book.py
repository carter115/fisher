#!/usr/bin/env python
# -*- coding:utf-8 -*-
from app.libs.httper import HTTP
from flask import current_app


class YuShuBook:
    # 描述特征(类变量、实例变量)
    # 行为(方法)
    # 面向过程
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def search_by_keyword(self, keyword, page=1):
        size = current_app.config['PRE_PAGE']
        url = self.keyword_url.format(keyword, size, (page - 1) * size)
        # url = self.keyword_url.format(keyword, current_app.config['PRE_PAGE'], self.calc_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    @property
    def first(self):
        return self.books[0] if self.total > 0 else None
