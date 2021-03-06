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
@File : application.py
@desc :
"""
import sys
import time
import signal
import logging.config
import traceback

from tornado.options import define, options, parse_command_line
import tornado.web
import tornado.gen
import tornado.util
import tornado.httpserver
import tornado.ioloop
from sqlalchemy.exc import SQLAlchemyError

from lib.postgresql import dal
from lib.db_logic import get_account_info
from lib.tool import load_config_from_json_file
import setting

# 具体运行时，需要在调用应用程序时填写参数，python application.py --ip=172.168.12.12 --port=16002
define('ip', default='127.0.0.1', type=str, help="server's ip")
define('port', default=12001, type=int, help="the app using port")


class Application(tornado.web.Application):
    def __init__(self):
        from urls import urls
        settings = dict()

        super().__init__(urls, **settings)


def main_entrance():
    parse_command_line()
    logging.config.dictConfig(setting.LOGGING_CONFIG)
    r_log = logging.getLogger()

    app = Application()
    m_server = app.listen(port=options.port, address=options.ip, xheaders=True)

    # try:
    #     params = load_config_from_json_file()
    # except Exception:
    #     r_log.error(f'load json file failed, stack info: <{traceback.format_exc()}>')
    #     sys.exit(-1)
    # else:
    #     try:
    #         dal.conn_str = params['connect_str']
    #         dal.connect_db(echo=True, pool_recycle=3600)
    #     except SQLAlchemyError:
    #         r_log.error(f'postgres connect failed, stack info: <{traceback.format_exc()}> ')
    #
    # setting.APP_ID, setting.APP_SECRET, setting.APP_AES_KEY, setting.API_TOKEN = get_account_info(1)

    def shutdown():
        r_log.info('Stopping wechat info server')
        m_server.stop()

        r_log.info(f'Will shutdown wechat info server in {setting.MAX_WAIT_SECONDS_BEFORE_SHUTDOWN} seconds ...,'
                   f' maybe longer')
        io_loop = tornado.ioloop.IOLoop.instance()

        deadline = time.time() + setting.MAX_WAIT_SECONDS_BEFORE_SHUTDOWN

        def stop_loop():
            nonlocal deadline

            now = time.time()
            if now < deadline:
                io_loop.add_timeout(now + 1, stop_loop)
            else:
                io_loop.stop()
                r_log.info('wechat server Shutdown')

        stop_loop()

    def sig_handler(sig, frame):
        r_log.warning(f'Caught signal: {sig}')
        tornado.ioloop.IOLoop.current().add_callback(shutdown)

    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    tornado.ioloop.IOLoop.current().start()

    r_log.info("wechat server Exit...")


if __name__ == '__main__':
    main_entrance()
