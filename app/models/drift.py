#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import Column, Integer, SmallInteger, String, Boolean, ForeignKey, desc, func
from sqlalchemy.orm import relationship

from app.libs.enums import PendingStatus
from .base import Base


class Drift(Base):
    """
    一次具体的交易信息
    """
    id = Column(Integer, primary_key=True)

    # 邮寄信息
    recipient_name = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    message = Column(String(200))
    mobile = Column(String(20), nullable=False)

    # 书籍信息
    isbn = Column(String(13))
    book_title = Column(String(50))
    book_author = Column(String(30))
    book_img = Column(String(50))

    # 请求者信息
    requester_id = Column(Integer)
    requester_nickname = Column(String(20))

    # 赠送者信息
    gifter_id = Column(Integer)
    gift_id = Column(Integer)
    gifter_nickname = Column(String(20))

    # requester_id = Column(Integer, ForeignKey('user.id'))
    # requester = relationship('User')
    # gift_id = Column(Integer, ForeignKey('gift.id'))
    # gift = relationship('Gift')

    _pending = Column('pending', SmallInteger, default=1)

    # 数字类型、枚举类型的转换
    @property
    def pending(self):
        return PendingStatus(self._pending)

    @pending.setter
    def pending(self, status):
        self._pending = status.value
