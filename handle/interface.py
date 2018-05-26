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
import json
import hashlib
import logging

from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient, HTTPError

from lib.ssdb import db
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


class GetAccessToken(RequestHandler):
    """主动获取access token"""
    async def get(self):
        try:
            req_url = f'https://sz.api.weixin.qq.com/cgi-bin/token?' \
                      f'grant_type=client_credential&' \
                      f'appid={setting.APP_ID}&' \
                      f'secret={setting.APP_SECRET}'
            req_resp = await AsyncHTTPClient().fetch(req_url)
        except HTTPError as e:
            r_log.error(f'request <{req_url}>, error:<{e.code}><{e.message}>')
            self.set_status(e.code)
            return
        except Exception as e:
            r_log.error(f'request <{req_url}>, error:<{e}>')
            self.set_status(500, reason=f'{e}')
            return
        else:
            resp_dict = json.loads(req_resp.body, encoding='utf-8')
            if 'errcode' in resp_dict:
                r_log.error(
                    f'request access token error code <{resp_dict["errcode"]}>, error msg <{resp_dict["errmsg"]}>')
                self.set_status(500, reason=resp_dict["errmsg"])
                return
            else:
                # access token will disappear after 7200 second
                db.set(setting.ACCESS_TOKEN_KEY, resp_dict["access_token"])
                db.expire('we_chat_access_token', resp_dict["expires_in"])
                r_log.info(
                    f'request access token <{resp_dict["access_token"]}>, expires_in <{resp_dict["expires_in"]}>')
                self.set_status(200)
                return


class NoneHandle(RequestHandler):
    def get(self):
        self.set_status(404, reason=f'no the interface {self.request.uri}')
        return

    post = get


if __name__ == '__main__':
    pass
