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
@File : ssdb.py
@desc : 使用redis.py连接连接ssdb数据库，返回的数据都是
"""
import logging
import redis

r_log = logging.getLogger()
db = redis.StrictRedis(host='localhost', port=8881)

# db.set('hi xushiyin', 'uu')
# print(db.get('hi xushiyin').decode('utf-8'))
# db.execute_command('set', 'ppp', 'ret')
# print(db.execute_command('get', 'ppp').decode('utf-8'))


def get_key(in_k_name):
    try:
        ret_val = db.get(in_k_name)
    except redis.RedisError as e:
        r_log.error(f'ssdb get <{in_k_name}> failed, error <{e}>')
        return None
    except OSError as e:
        r_log.error(f'ssdb get <{in_k_name}> failed, error <{e}>')
        return None
    else:
        return ret_val.decode('utf-8')


if __name__ == '__main__':
    print(get_key('we_chat_access_token'))
