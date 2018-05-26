#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2018, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : wechatInfo
@Time : 2018/5/14 下午9:59
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : urls.py
@desc :
"""
import handle.interface
from handle.interface import we_robot
from werobot.contrib.tornado import make_handler


urls = [
    (r'/msg', make_handler(we_robot)),
    (r'.*', handle.interface.NoneHandle)
]

p_urls = [
    (r'/get_access_token', handle.interface.GetAccessToken),
    (r'.*', handle.interface.NoneHandle),
]

if __name__ == '__main__':
    pass
