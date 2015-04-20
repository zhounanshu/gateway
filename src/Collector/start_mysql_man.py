#!usr/bin/python
# -*- coding: utf-8 -*-
'''
    start mysql adapter
    @author: marvin
    @email: bobozns@gmail.com
'''
from lib.MySQL.mpSQL import MySQLDevice
from mqpp.paho.sender import *
from pool.adapters.BR_adapter import MySQL_Adapter

BR_DSA = MySQLDevice()
results = BR_DSA.GetData()
conenct_broker()
i = 0
for result in results:
    i += 1
    B_R = MySQL_Adapter(result, i)
    if B_R.Praser():
        To_PoatData = B_R.FormatData()
        post_data(To_PoatData)
    else:
        print "failed!"
