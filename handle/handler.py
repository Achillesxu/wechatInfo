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

from lib.ssdb import db, hash_get_fields


class TextHandle:
    @staticmethod
    def get_category(in_msg):
        r_list = hash_get_fields(in_msg.content)
        if r_list:
            r_list.append('输入以上电影名字，获取链接，点击链接播放')
            s_str = '\n'.join(r_list)
        else:
            s_str = f'{in_msg.content} 分类下没有内容'
        return TextReply(in_msg, content=s_str)

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
