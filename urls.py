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


urls = [
    (r'/nn_sms/status/ruidong/send', handle.interface),
    (r'/nn_sms/status/mengwang/send', handle.interface),
    (r'.*', handle.interface.NoneHandle)
]

if __name__ == '__main__':
    pass
