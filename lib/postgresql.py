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


m_engine = create_engine('postgresql+psycopg2://achilles_pgsql:Filter@1986@47.104.229.96/wechat',
                         echo=True, pool_recycle=3600)

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


Base.metadata.create_all(m_engine)

Session = sessionmaker(bind=m_engine)

m_session = Session()


def get_account_info(in_id):
    query = m_session.query(AccountInfo)
    ac_info = query.filter(AccountInfo.a_id == in_id).first()
    return ac_info.app_id, ac_info.app_secret, ac_info.app_aes_key, ac_info.app_token


if __name__ == '__main__':
    print(get_account_info(1))

