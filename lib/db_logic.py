#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2018, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : wechatInfo
@Time : 2018/9/2 下午4:25
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : db_logic.py
@desc :
"""
from lib.postgresql import dal, AccountInfo, BwgApiInfo


def get_account_info(in_id=1):
    query = dal.session.query(AccountInfo)
    ac_info = query.filter(AccountInfo.a_id == in_id).first()
    return ac_info.app_id, ac_info.app_secret, ac_info.app_aes_key, ac_info.app_token


def get_bwg_api_key(in_id=1):
    query = dal.session.query(BwgApiInfo)
    ac_info = query.filter(BwgApiInfo.id == in_id).first()
    return ac_info.veid, ac_info.api_key


if __name__ == '__main__':
    from lib.postgresql import dal
    from lib.tool import load_config_from_json_file

    params = load_config_from_json_file()
    dal.conn_str = params['connect_str']
    dal.connect_db(echo=True, pool_recycle=3600)
    print(get_bwg_api_key())
