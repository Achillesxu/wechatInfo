#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2018, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : wechatInfo
@Time : 2018/5/19 下午2:29
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : app_get_token_per_2_hour.py
@desc :
"""
import sys
import time
import traceback
from datetime import datetime
from datetime import timedelta
import signal
import logging.config
from logging.handlers import RotatingFileHandler
import json

from tornado.options import define, options, parse_command_line
import tornado.web
import tornado.gen
import tornado.httpserver
import tornado.ioloop
from tornado import util
from tornado.httpclient import AsyncHTTPClient, HTTPError
from sqlalchemy.exc import SQLAlchemyError

from lib.postgresql import dal
from lib.db_logic import get_account_info
from lib.tool import load_config_from_json_file

from lib.redis import db
import setting

# 具体运行时，需要在调用应用程序时填写参数，python application.py --ip=172.168.12.12 --port=16002
define('ip', default='127.0.0.1', type=str, help="server's ip")
define('port', default=12002, type=int, help="the app using port")

LOG_NAME = 'TOKEN_PERIODIC'
LOG_FILE_NAME = f'/var/log/supervisor/wechatperiodic/{LOG_NAME}.log'  # 服务器文件夹地址
# LOG_FILE_NAME = '{}/{}.log'.format(os.path.dirname((os.path.abspath(__file__))), LOG_NAME)
LOG_MAX_BYTES = 50 * 1024 * 1024
LOG_BACK_COUNT = 10

# 将log更新到stdout or stderr
r_log = logging.getLogger()
rotate_handle = RotatingFileHandler(LOG_FILE_NAME,
                                    LOG_MAX_BYTES,
                                    LOG_BACK_COUNT,
                                    encoding='utf-8')
stdout_formatter = logging.Formatter(
    f'%(name)s-%(asctime)s-%(levelname)s-%(filename)s-[line:%(lineno)d]-%(message)s')
rotate_handle.setFormatter(stdout_formatter)
r_log.addHandler(rotate_handle)
r_log.setLevel(logging.INFO)


class Application(tornado.web.Application):
    def __init__(self):
        from urls import p_urls
        settings = dict()
        self.p_handle = None
        super().__init__(p_urls, **settings)


async def asy_request():
    try:
        req_url = f'https://api.weixin.qq.com/cgi-bin/token?' \
                  f'grant_type=client_credential&' \
                  f'appid={setting.APP_ID}&' \
                  f'secret={setting.APP_SECRET}'
        req_resp = await AsyncHTTPClient().fetch(req_url)
    except HTTPError as e:
        r_log.error(f'request <{req_url}>, error:<{e.code}><{e.message}>')
    except Exception as e:
        r_log.error(f'request <{req_url}>, error:<{e}>')
    else:
        resp_dict = json.loads(req_resp.body, encoding='utf-8')
        if 'errcode' in resp_dict:
            r_log.error(f'request access token error code <{resp_dict["errcode"]}>, error msg <{resp_dict["errmsg"]}>')
        else:
            # access token will disappear after 7200 second
            db.set(setting.ACCESS_TOKEN_KEY, resp_dict["access_token"])
            db.expire('we_chat_access_token', resp_dict["expires_in"])
            r_log.info(f'request access token <{resp_dict["access_token"]}>, expires_in <{resp_dict["expires_in"]}>')


def main_entrance():
    parse_command_line()

    setting.PERIODIC_SERVER_PORT = options.port

    app = Application()
    m_server = app.listen(port=options.port, address=options.ip, xheaders=True)

    try:
        params = load_config_from_json_file()
    except Exception:
        r_log.error(f'load json file failed, stack info: <{traceback.format_exc()}>')
        sys.exit(-1)
    else:
        try:
            dal.conn_str = params['connect_str']
            dal.connect_db(echo=True, pool_recycle=3600)
        except SQLAlchemyError:
            r_log.error(f'postgres connect failed, stack info: <{traceback.format_exc()}> ')

    setting.APP_ID, setting.APP_SECRET, setting.APP_AES_KEY, setting.API_TOKEN = get_account_info(1)

    def shutdown():
        r_log.info('Stopping token periodic server')
        m_server.stop()
        r_log.info('Stopping token periodic handle')
        app.p_handle.stop()

        r_log.info(f'Will shutdown token periodic server in {3}'
                   f' seconds ..., maybe longer')
        io_loop = tornado.ioloop.IOLoop.instance()

        deadline = time.time() + 3

        def stop_loop():
            nonlocal deadline

            now = time.time()
            if now < deadline:
                io_loop.add_timeout(now + 1, stop_loop)
            else:
                io_loop.stop()
                r_log.info('token periodic server Shutdown')

        stop_loop()

    def sig_handler(sig, frame):
        r_log.warning(f'Caught signal: {sig}')
        tornado.ioloop.IOLoop.current().add_callback(shutdown)

    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    def periodic_request():
        r_log.info(f'get we public token at <{datetime.now().strftime("%Y-%m-%d %H:%M:%D")}>')
        tornado.gen.with_timeout(timedelta(seconds=setting.TOKEN_REQ_TIMEOUT), asy_request(),
                                 quiet_exceptions=(util.TimeoutError,))

    app.p_handle = tornado.ioloop.PeriodicCallback(periodic_request, setting.TOKEN_PERIODIC)

    app.p_handle.start()
    # 启动马上获取一次access token
    tornado.gen.with_timeout(timedelta(seconds=setting.TOKEN_REQ_TIMEOUT), asy_request())

    tornado.ioloop.IOLoop.current().start()

    r_log.info("token periodic server Exit...")


if __name__ == '__main__':
    main_entrance()
    # import asyncio
    # i_loop = asyncio.get_event_loop()
    # i_loop.run_until_complete(asy_request())
