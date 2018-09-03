#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@license : (C) Copyright 2013-2018, Easy doesnt enter into grown-up life.
@Software: PyCharm
@Project : wechatInfo
@Time : 2018/6/13 上午9:13
@Author : achilles_xushy
@contact : yuqingxushiyin@gmail.com
@Site : 
@File : postgresql.py
@desc :
"""
from sqlalchemy import create_engine, ForeignKey, Boolean
from sqlalchemy import Table, Column, Integer, Numeric, String, DateTime
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

Base = declarative_base()


class AccountInfo(Base):
    """
    微信账户信息
    """
    __tablename__ = 'account_info'
    a_id = Column(Integer(), primary_key=True, autoincrement=True)
    app_id = Column(String(64), index=True)
    app_secret = Column(String(64))
    app_aes_key = Column(String(64))
    app_token = Column(String(64))

    def __repr__(self):
        return f'{type(self).__name__}(app_id={self.app_id},' \
               f' app_secret={self.app_secret}, app_aes_key={self.app_aes_key})'


class BwgApiInfo(Base):
    """
    搬瓦工api接口key
    """
    __tablename__ = 'bwg_api'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    veid = Column(String(32), index=True, unique=True)
    api_key = Column(String(64))


class DataAccessLayer:
    def __init__(self, in_conn_str=''):
        self._conn_str = in_conn_str
        self.engine = None
        self._Session = None
        self._session = None

    @property
    def conn_str(self):
        return self._conn_str

    @conn_str.setter
    def conn_str(self, in_conn_str):
        self._conn_str = in_conn_str

    def connect_db(self, **kwargs):
        self.engine = create_engine(self.conn_str, **kwargs)
        Base.metadata.create_all(self.engine)
        self._Session = sessionmaker(bind=self.engine, autocommit=True)
        self._session = self._Session()

    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, in_ss):
        self._session = in_ss


dal = DataAccessLayer()


if __name__ == '__main__':
    pass

