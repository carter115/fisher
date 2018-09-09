#!/usr/bin/env python
# -*- coding:utf-8 -*-

class A():
    def __call__(self):
        return object()


class B():
    def run(self):
        return object()


def func():
    return object()


def main(callable):
    callable()
    # 想在main中调用传入的参数，得到一个对象object
    # a.go() -> 修改后:a()
    # b.run()
    # func()
    pass


main(A())
main(B())
main(func())
