#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2018, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : wechatInfo
@Time : 2018/6/23 下午2:34
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : turing_interface.py
@desc : 图灵机器人输入类型支持文本，图片，音频，客户端信息，
        详细信息查看https://www.kancloud.cn/turing/web_api/522992
"""
import json
import logging
import traceback
import pprint

import requests

r_log = logging.getLogger()


class TuringInterface:
    def __init__(self):
        pass

    API_URL = 'http://openapi.tuling123.com/openapi/api/v2'

    def text_api(self, in_text):
        in_dict = {
            'reqType': 0,  #文本
            'perception': {
                'inputText': {
                    'text': in_text
                }
            },
            'userInfo': {
                'apiKey': '874c9fa735324bb5b630c00d8d74e61b',
                'userId': 'SubInfo',
            }
        }

        try:
            req_rep = requests.post(self.API_URL, json=in_dict, timeout=2.0)
        except Exception:
            r_log.error(f'request error <{traceback.format_exc()}>')
            return None
        else:
            if req_rep.status_code == 200:
                r_log.info(req_rep.text)
                j_dict = req_rep.json()
                if 'results' in j_dict:
                    return j_dict['results'][0]['values']['text']
                else:
                    return None
            else:
                return None


if __name__ == '__main__':
    t_h = TuringInterface()
    t_h.text_api('刘梦')
