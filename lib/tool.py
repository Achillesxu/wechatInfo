#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2018, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : wechatInfo
@Time : 2018/5/20 下午6:10
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : tool.py
@desc :
"""
import json
import logging
import traceback
from xmltodict import parse

r_log = logging.getLogger()


def load_config_from_json_file():
    with open('/var/www/WeChatPublic/config.json') as fp:
        params = json.load(fp)
        return params


if __name__ == '__main__':
 #    str_xml = """<xml>
 # <ToUserName><![CDATA[粉丝号]]></ToUserName>
 # <FromUserName><![CDATA[公众号]]></FromUserName>
 # <CreateTime>1460541339</CreateTime>
 # <MsgType><![CDATA[text]]></MsgType>
 # <Content><![CDATA[test]]></Content>
 # </xml>"""
 #    for k, v in parse(str_xml).items():
 #        print(k, v)
    print(load_config_from_json_file())
