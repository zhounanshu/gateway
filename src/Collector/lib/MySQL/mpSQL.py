#!/usr/bin/python
# -*-coding:utf-8 -*-
'''
    mysql api
    @marvin
    @email: bobozns@gmail.com
'''

import MySQLdb
import logging
from lib.util import *
from config import MySQLConfig


class MySQLDevice(object):

    def __init__(self):
        init_logging()
        self.host = None
        self.port = None
        self.user = None
        self.passwd = None
        self.db = None
        self.key_vaalue = None
        self.JsonData = None
        self.Config = MySQLConfig().get_cofig()

    def LodeConfig(self):
        ConfigInfo = self.Config
        if ConfigInfo is None:
            logging.debug("Loding configuration failed.....")
            return False
        else:
            self.host = ConfigInfo[0]
            self.port = int(ConfigInfo[1])
            self.user = ConfigInfo[2]
            self.passwd = ConfigInfo[3]
            self.db = ConfigInfo[4]
            self.key_value = ConfigInfo[5]
            logging.info("Loding configuration successful.....")
            return True

    def QueryData(self, host, user, passwd, db, port):
        con = None
        if self.key_value is not None:
            key = self.key_value.keys()[0]
            value = self.key_value[key]

        # sql = "select * from compressor where pv = 'meter4'"
        sql = "select * from compressor where " + \
            key + " = " + "'" + value + "'"
        print sql
        try:
            con = MySQLdb.connect(
                host=host, user=user, passwd=passwd, db=db, port=port,
                charset='utf8')
            cur = con.cursor(MySQLdb.cursors.DictCursor)
            cur.execute(sql)
            self.JsonData = cur.fetchall()
            cur.close()
            con.close()
        except Exception:
            print 'connecting db failed..........'
        pass

    def GetData(self):
        if self.LodeConfig():
            self.QueryData(
                self.host, self.user, self.passwd, self.db, self.port)
        if self.JsonData is None:
            logging.debug("there is no data coming from db....")
            return None
        else:
            return self.JsonData
