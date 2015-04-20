#!usr/bin/python
# -*- coding: utf-8 -*-
'''
    MySQL config
    @author: marvin
    @email:bobozns@gmial.com
'''
import json
import os
# sys.path.append(os.path.split(os.path.realpath(__file__)[1])
# sys.path.append(os.getcwd())
from lib.util import *
import logging


class MySQLConfig(object):
    DEFAULTS = {"host": "localhsot", "port": "3306",
                "user": "root", "db": "testdb"}

    def __init__(self):
        self.arg = None
        init_logging()
        # get the real path of this file
        self.path = os.path.split(os.path.realpath(__file__))[0]
        print os.getcwd()

    def get_cofig(self):
        config_file_name = str(self.path) + "/mySQL.json"
        with open(config_file_name) as f:
            conf_infor = json.load(f)
        host = conf_infor["host"]
        port = conf_infor["port"]
        user = conf_infor["user"]
        passwd = conf_infor["passwd"]
        db = conf_infor["db"]
        key_value = conf_infor["key"]
        logging.debug("loading mysql config information.....")
        return (host, port, user, passwd, db, key_value)
