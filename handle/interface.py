#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2018, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : wechatInfo
@Time : 2018/5/14 下午10:00
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : interface.py
@desc :
"""
from tornado.web import RequestHandler


class NoneHandle(RequestHandler):
    def get(self):
        self.set_status(404, reason=f'no the interface {self.request.uri}')
        return

    post = get


if __name__ == '__main__':
    pass
