# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 21:40:36 2021

@author: USER
"""

import pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456789',db='web')

cursor = conn.cursor()  #資料集