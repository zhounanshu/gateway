#!usr/bin/python
# -*- coding: utf-8 -*-
'''
    define B&R topic
    @author:marvin
    @email:boboznd@gmial.com
'''
from pool.topic import *
# from lib.util import *
import time


class MySQL_Adapter(object):

    def __init__(self, rawdata, sequence):
        init_logging()
        self.ponits = []
        self.Dict = {}
        self.topic_name = None
        self.topic_colums = None
        self.rawdata = rawdata
        self.sequence = sequence

    def Praser(self):
        if self.rawdata is None:
            # logging.debug("Please loading data!")
            return False
        else:
            # logging.debug("Start defining topic.......")
            topic = topic_config()
            colums = topic.GetColumns()
            time_feild = colums[0]
            data_feild = colums[1:]
            # format time for mqtt client
            standard_time = int(
                time.mktime(time.strptime(
                    self.rawdata[time_feild][:-4],
                    "%Y-%m-%d %H:%M:%S"))) * 1000
            data_dict = {}
            data_dict.setdefault("timestamp", standard_time)
            for feild in data_feild:
                data_dict[feild] = float(self.rawdata[feild])
            data_dict["id"] = self.sequence
            data_dict["device"] = "B&R"
            self.Dict = data_dict
            return True

    def FormatData(self):
        return self.Dict
