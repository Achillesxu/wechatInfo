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
# 服务程序在8表后关闭，程序关闭时间可能超过8秒，时间取决于事件循环中是否添加了超时函数
MAX_WAIT_SECONDS_BEFORE_SHUTDOWN = 8

PERIODIC_SERVER_PORT = 0

# #################################channel token##################################################################
# 正式账号 a_id = 1
# 测试账号 a_id = 2
APP_ID = ''
APP_SECRET = ''
APP_AES_KEY = ''
API_TOKEN = ''

ACCESS_TOKEN_KEY = 'we_chat_access_token'

WE_CHAT_NAME = 'Subcription4Info'

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
