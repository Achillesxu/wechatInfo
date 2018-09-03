#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2018, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : wechatInfo
@Time : 2018/9/3 下午8:39
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : bwg_interface.py
@desc :
"""
import logging
import traceback
from datetime import datetime
from urllib.parse import urlencode
from sqlalchemy.exc import SQLAlchemyError

import requests

from lib.db_logic import get_bwg_api_key

r_log = logging.getLogger()


class BwgInterface:
    BWG_API = 'https://api.64clouds.com/v1/{}?'

    def __init__(self):
        pass

    def get_request(self, in_command):
        try:
            veid, api_key = get_bwg_api_key()
        except SQLAlchemyError:
            r_log.error(f'access <{get_bwg_api_key}>, stack info: <{traceback.format_exc()}>')
        else:
            parms_dict = {
                'veid': veid,
                'api_key': api_key
            }
            p_str = urlencode(parms_dict)
            req_url = self.BWG_API.format(in_command)
            print(req_url + p_str)
            try:
                req_rep = requests.get(req_url + p_str, timeout=4.0)
            except Exception:
                r_log.error(f'request <{req_url}>, stack info: <{traceback.format_exc()}>')
                return None
            else:
                if req_rep.status_code == 200:
                    r_log.info(req_rep.text)
                    r_dict = req_rep.json()
                    today_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    next_time = datetime.fromtimestamp(r_dict['data_next_reset'])
                    total_data = r_dict['plan_monthly_data'] // (1024 * 1024 * 1024)
                    used_data = r_dict['data_counter'] / (1024 * 1024 * 1024)
                    ret_str = f'日期：{today_str}\n服务器地点：{r_dict["node_location"]}\n' \
                              f'服务器数据中心：{r_dict["node_datacenter"]}\n' \
                              f'服务器ip：{r_dict["ip_addresses"]}\n' \
                              f'服务器当月流量：{total_data}GB\n' \
                              f'服务器目前已经使用流量：{used_data:.3}GB\n' \
                              f'服务器流量下次重置时间：{next_time:%Y-%m-%d %H:%M:%S}'
                    return ret_str
                else:
                    return None


if __name__ == '__main__':
    from lib.postgresql import dal
    from lib.tool import load_config_from_json_file

    params = load_config_from_json_file()
    dal.conn_str = params['connect_str']
    dal.connect_db(echo=True, pool_recycle=3600)

    bwg = BwgInterface()
    pp = bwg.get_request('getServiceInfo')
    print(pp)
