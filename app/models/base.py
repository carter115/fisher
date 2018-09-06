#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True  # 不创建数据表
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)
