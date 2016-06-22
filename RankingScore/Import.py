#coding:utf-8
import threading
import json
import pycurl
import StringIO
import MySQLdb
from time import sleep
from urlparse import urlparse
import xlrd
import xlwt
import sys
reload(sys)
sys.setdefaultencoding('utf8')
conn = MySQLdb.connect('localhost','root','','rank',charset='utf8')
data = xlrd.open_workbook('keyword.xlsx')
sheet1 = data.sheets()[0]#第一个表
rows = sheet1.nrows#行数
with conn:
	cur = conn.cursor()
	for i in range(rows):		
		sql = 'insert into t_keyword (keyword,searchnum) values("%s","%s")' %(sheet1.row_values(i)[0],sheet1.row_values(i)[1])
		cur.execute(sql)
		conn.commit()
conn.close()

		
