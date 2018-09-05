#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
import time
from werkzeug.local import Local

# class A:
#     b = 1
# my_obj = A()

my_obj = Local()
my_obj.b = 1


def worker():
    my_obj.b = 2
    print('in new thread b is: {}'.format(my_obj.b))


new_t = threading.Thread(target=worker, name='qiyue_thread')
new_t.start()
time.sleep(1)

# 主线程
print('in main thread b is: {}'.format(my_obj.b))
