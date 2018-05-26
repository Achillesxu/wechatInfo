#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2018, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : wechatInfo
@Time : 2018/5/26 下午3:55
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : handler.py
@desc : 各种消息处理类
"""
from werobot.replies import TextReply

from lib.ssdb import db


class TextHandle:
    @staticmethod
    def get_url(in_msg):
        b_str = db.hget('电影', in_msg.content)
        if b_str:
            s_str = b_str.decode('utf-8')
        else:
            s_str = '找不到，请联系wechat:xushiyin1986'
        return TextReply(in_msg, content=s_str)


if __name__ == '__main__':
    pass
