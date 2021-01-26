#coding:utf-8
import MySQLdb
import sys
from urlparse import urlparse
from time import sleep
import subprocess
import os
#http://my.oschina.net/guol/blog/95699
reload(sys)
sys.setdefaultencoding('utf8')

conn = MySQLdb.connect('localhost','root','','rank',charset='utf8')
with conn:
	cur = conn.cursor()
	sql = 'select url from t_rank'
	cur.execute(sql)
	conn.commit()
	rowNum = int(cur.rowcount)
	for data in range(rowNum):
		row = cur.fetchone()	
		with open('domain.txt',r'a+') as my:
			my.write(urlparse(row[0]).netloc+'\n')
conn.close()
sleep(1)
subprocess.call(["cat domain.txt|sort|uniq -c|sort -r > result"],shell='true')
os.remove('domain.txt')