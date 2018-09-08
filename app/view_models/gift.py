#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .book import BookViewModel


# from collections import namedtuple
# MyGift = namedtuple('MyGift', ['id', 'book', 'wishes_count'])


class MyGifts:
    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []
        self.__gifts_os_mine = gifts_of_mine
        self.__wish_coutn_list = wish_count_list
        self.gifts = self.__parse()

    def __parse(self):
        temp_gifts = []
        for gift in self.__gifts_os_mine:
            my_gift = self.__matching(gift)
            temp_gifts.append(my_gift)
        return temp_gifts

    def __matching(self, gift):
        count = 0
        for wish_count in self.__wish_coutn_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        # my_gift = MyGift(gift.id, BookViewModel(gift.book), count)

        my_gift = {
            'id': gift.id,
            'book': BookViewModel(gift.book),
            'wishes_count': count
        }
        return my_gift
