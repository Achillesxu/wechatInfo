#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2018, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : wechatInfo
@Time : 2018/5/20 下午1:40
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : redis.py
@desc : 使用redis.py连接连接ssdb数据库，返回的数据都是
"""
import logging
import redis

r_log = logging.getLogger()
db = redis.StrictRedis(host='localhost', port=6379)


def get_key(in_k_name):
    try:
        ret_val = db.get(in_k_name)
    except redis.RedisError as e:
        r_log.error(f'redis get <{in_k_name}> failed, error <{e}>')
        return None
    except OSError as e:
        r_log.error(f'redis get <{in_k_name}> failed, error <{e}>')
        return None
    else:
        return ret_val.decode('utf-8')


def hash_get_fields(in_key):
    try:
        r_list = db.hkeys(in_key)
    except redis.RedisError as e:
        r_log.error(f'redis hkeys <{in_key}> failed, error <{e}>')
        return None
    except OSError as e:
        r_log.error(f'redis hkeys <{in_key}> failed, error <{e}>')
        return None
    else:
        if r_list:
            return [j.decode('utf-8') for j in r_list]
        else:
            return []


if __name__ == '__main__':
    h_name = f'电影'
    for i in db.hkeys(h_name):
        print(i.decode('utf-8'))
