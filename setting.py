#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2018, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : wechatInfo
@Time : 2018/5/14 下午9:33
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : setting.py
@desc :
"""
import os
import logging

from lib.ssdb import get_key
# 服务程序在8表后关闭，程序关闭时间可能超过8秒，时间取决于事件循环中是否添加了超时函数
MAX_WAIT_SECONDS_BEFORE_SHUTDOWN = 8

PERIODIC_SERVER_PORT = 0

# #################################channel token##################################################################
API_TOKEN = 'ABC3C027B63A54E4E66B0E8F734E6238'
APP_ID = get_key('APP_ID')
APP_SECRET = get_key('APP_SECRET')
APP_AES_KEY = get_key('ENCODING_AES_KEY')

ACCESS_TOKEN_KEY = 'we_chat_access_token'

WE_CHAT_NAME = 'Subcription4Info'

MEDIA_TYPE = ['电影']

# #################################channel token##################################################################
TOKEN_PERIODIC = 100 * 60 * 1000  # 每100分钟请求一次token
TOKEN_REQ_TIMEOUT = 25  # 请求超时时间25秒
# #################################server log configuration#######################################################

LOGGING_CONFIG = dict(
    version=1,
    formatters={
        'f_root': {
            'format': '%(name)s-%(asctime)s-%(levelname)s-%(filename)s-[line:%(lineno)d]-%(message)s',
        }
    },
    handlers={
        'std_stream': {
            'class': 'logging.StreamHandler',
            'formatter': 'f_root',
            'level': logging.INFO,
            'stream': 'ext://sys.stdout'
        },
    },
    loggers={
        'tornado.access': {
            'handlers': ['std_stream'],
            'level': logging.INFO,
            'propagate': False
        },
        'tornado.application': {
            'handlers': ['std_stream'],
            'level': logging.INFO,
            'propagate': False
        },
        'tornado.general': {
            'handlers': ['std_stream'],
            'level': logging.INFO,
            'propagate': False
        }
    },
    root={
        'handlers': ['std_stream'],
        'level': logging.INFO,
    },
)


if __name__ == '__main__':
    print(os.path.dirname((os.path.abspath(__file__))))
