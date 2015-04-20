#!usr/bin/python
# -*- coding: utf-8 -*-
'''
    define topic
    @author: marvin
    @email: bobozns@gmail.com
'''
import json
import os
import logging
from lib.util import *


class topic_config(object):

    """docstring for topic"""

    def __init__(self):
        init_logging()
        self.topic_name = None
        self.topic_columns = None
        self.config_path = os.path.split(os.path.realpath(__file__))[0]
        config_file = self.config_path + '/topic.json'
        with open(config_file) as f:
            config_info = json.load(f)
        if config_info is not None:
            # logging.debug("topic has been defined successful!")
            self.topic_name = config_info['name']
            self.topic_columns = config_info['columns']
        else:
            logging.debug('Fail to define topic!')
        pass

    def GetName(self):
        return self.topic_name

    def GetColumns(self):
        return self.topic_columns
