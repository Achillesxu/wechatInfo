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
@File : turing.py
@desc : 图灵机器人输入类型支持文本，图片，音频，客户端信息，
        详细信息查看https://www.kancloud.cn/turing/web_api/522992
"""
import json
import logging
import traceback
import pprint

from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPError
from tornado.httputil import HTTPHeaders

r_log = logging.getLogger()


class TuringInterface:
    def __init__(self):
        pass

    async_client = AsyncHTTPClient()
    API_URL = 'http://openapi.tuling123.com/openapi/api/v2'

    async def text_api(self, in_text):
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
        req_headers = HTTPHeaders({
            'content-type': 'application/json; charset=utf-8',
        })
        req_obj = HTTPRequest(self.API_URL, method='POST',
                              headers=req_headers,
                              body=json.dumps(in_dict, ensure_ascii=False))
        try:
            req_rep = await self.async_client.fetch(req_obj)
        except HTTPError as e:
            r_log.error(f'http error <{e.code, e.message}>')
            return None
        except Exception:
            r_log.error(f'request error <{traceback.format_exc()}>')
            return None
        else:
            j_dict = json.loads(req_rep.body, encoding='utf-8')
            r_log.info(req_rep.body)
            if 'results' in j_dict:
                print(j_dict['results'][0]['values']['text'])
                return j_dict['results'][0]['values']['text']
            else:
                return None


if __name__ == '__main__':
    t_h = TuringInterface()
    import asyncio
    io_loop = asyncio.get_event_loop()
    io_loop.run_until_complete(t_h.text_api('刘梦'))
