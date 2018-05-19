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

# #################################channel token##################################################################
API_TOKEN = 'ABC3C027B63A54E4E66B0E8F734E6238'

# #################################channel token##################################################################
TOKEN_PERIODIC = 100 * 1000  # 每100分钟请求一次token
TOKEN_REQ_TIMEOUT = 25  # 请求超时时间25秒
# #################################server log configuration#######################################################
LOG_NAME = 'WE_PUBLIC'
LOG_FILE_NAME = '{}/{}.log'.format(os.path.dirname((os.path.abspath(__file__))), LOG_NAME)
# LOG_FILE_NAME = '{}/{}.log'.format('/var/log/wepubliclog', LOG_NAME)

LOGGING_CONFIG = dict(
    version=1,
    formatters={
        'f_root': {
            'format': '%(name)s-%(asctime)s-%(levelname)s-%(filename)s-[line:%(lineno)d]-%(message)s',
        }
    },
    handlers={
        'rotate_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'f_root',
            'level': logging.INFO,
            'filename': LOG_FILE_NAME,
            'maxBytes': 50 * 1024 * 1024,
            'backupCount': 10,
        },
    },
    loggers={
        'tornado.access': {
            'handlers': ['rotate_file'],
            'level': logging.INFO,
            'propagate': False
        },
        'tornado.application': {
            'handlers': ['rotate_file'],
            'level': logging.INFO,
            'propagate': False
        },
        'tornado.general': {
            'handlers': ['rotate_file'],
            'level': logging.INFO,
            'propagate': False
        }
    },
    root={
        'handlers': ['rotate_file'],
        'level': logging.INFO,
    },
)


if __name__ == '__main__':
    print(os.path.dirname((os.path.abspath(__file__))))
