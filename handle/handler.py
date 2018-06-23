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

from lib.turing import TuringInterface


class TextHandle:
    @staticmethod
    async def process_text(in_msg):
        t_api = TuringInterface()
        ret_text = await t_api.text_api(in_msg.content)
        if ret_text:
            return TextReply(in_msg, content=ret_text)
        else:
            return TextReply(in_msg, content='服务有点问题，稍后再试')


if __name__ == '__main__':
    pass
