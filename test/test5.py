#!/usr/bin/env python
# -*- coding:utf-8 -*-

class MyResource:
    # def __enter__(self):
    #     print('connect to resource')
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     print('close resource connection')

    def query(self):
        print('query data')


from contextlib import contextmanager


@contextmanager
def make_myresource():
    print('connect to resource')
    yield MyResource()
    print('close resource connection')


with make_myresource() as r:
    r.query()


@contextmanager
def book_mark():
    print('<<', end='')
    yield
    print('>>', end='')


with book_mark():
    print('且将生活饮而尽', end='')
