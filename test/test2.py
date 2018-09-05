#!/usr/bin/env python
# -*- coding:utf-8 -*-
from werkzeug.local import LocalStack

# push,pop,top
s = LocalStack()
s.push(1)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

s.push(1)
s.push(2)
# 栈：后进先出
print(s.top)
print(s.top)
print(s.pop())
print(s.top)
