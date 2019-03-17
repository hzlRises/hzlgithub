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
import subprocess
import os
#http://my.oschina.net/guol/blog/95699
'''
最终会生成:
result.xls	存放最终计算结果...
t_keyword.txt 存放异常关键词...

'''
reload(sys)
sys.setdefaultencoding('utf8')

conn = MySQLdb.connect('localhost','root','','rank',charset='utf8')
with conn:
	cur = conn.cursor()
	sql = 'select keyword,url,pcrank from t_rank_copy'
	cur.execute(sql)
	conn.commit()
	rowNum = int(cur.rowcount)
	for data in range(rowNum):
		row = cur.fetchone()
		with open('domain.txt',r'a+') as my:
			my.write(urlparse(row[1]).netloc+'\n')
	print '写入完毕'	
