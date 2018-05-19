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
import hashlib
import logging

from tornado.web import RequestHandler

import setting

r_log = logging.getLogger()


class ReceiveMsgHandle(RequestHandler):
    def get(self):
        in_sig = self.get_argument('signature', '')
        in_ts = self.get_argument('timestamp', '')
        in_nonce = self.get_argument('nonce', '')
        in_echo_str = self.get_argument('echostr', '')

        if in_sig and in_ts and in_nonce and in_echo_str:
            r_log.info(f'signature <{in_sig}>')
            r_log.info(f'timestamp <{in_ts}>')
            r_log.info(f'nonce <{in_nonce}>')
            r_log.info(f'echostr <{in_echo_str}>')
            s_list = [in_ts, in_nonce, setting.API_TOKEN]
            t_sha1 = hashlib.sha1()
            t_sha1.update(bytes(''.join(sorted(s_list)), encoding='utf-8'))
            r_log.info(f'sha1({"".join(sorted(s_list))}----><{t_sha1.hexdigest()}>)')
            self.write(in_echo_str)
        else:
            self.set_status(400, reason='parameters error')
            self.finish()
            return


class NoneHandle(RequestHandler):
    def get(self):
        self.set_status(404, reason=f'no the interface {self.request.uri}')
        return

    post = get


if __name__ == '__main__':
    pass
