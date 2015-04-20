#!usr/bin/python
# -*- coding: utf-8 -*-

import json
import sys
import test
import os

class DF(object):
    def Data(self):
    	with open('/Users/marvinzns/Project/gateway/src/Collector/test/test.json') as json_file:
		#json_file = open('./test.txt','r')
		jdata = json.load(json_file)
		print os.path.dirname(sys.path[0])
                host = jdata["host"]
                port = jdata["port"]
                user = jdata["user"] 
		return (host, port, user)

