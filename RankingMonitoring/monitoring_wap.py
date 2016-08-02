#coding:utf-8
_author_ = 'heziliang'
'''
转载请注明出处:https://github.com/hzlRises
'''
import time
import re
import threading
import json
import pycurl
import StringIO
import MySQLdb
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf8')
today = time.strftime("%Y-%m-%d",time.localtime(time.time()))

threadNum = 5
match = 0
all = 0
num = 0
percentage = 0
url_list = []
keyword_list = []

def getSql():
	sql = 'select keyword from t_keyword order by rand() limit 10'
	return sql

def getIfmatch(html):	
	pattern = re.compile(r'm\.fang\.com/jiaju/[a-z]{2,8}/zhishi')
	zhishiurl = pattern.findall(html)
	bool = zhishiurl
	return bool
	
def getWant(line):
	keyword = keyword_list[line]
	url = url_list[line]
	try:		
		c = pycurl.Curl()
		c.setopt(c.URL,url)
		c.setopt(c.CONNECTTIMEOUT, 10)
		c.setopt(c.TIMEOUT,10) 
		b = StringIO.StringIO()
		c.setopt(c.WRITEFUNCTION,b.write)
		c.perform()
		html = b.getvalue()
		mutex.acquire()
		global match
		global all	
		global percentage
		if(getIfmatch(html)):
			match += 1
		else:
			pass
		all += 1	
		print 'all: '+str(all)+' match: '+str(match)+', percentage '+'%.1f'%((float(match)/all)*100)+'%'
		percentage = '%.1f'%((float(match)/all)*100)+'%'
		mutex.release()
	except:
		print '%s Empty reply from server' %keyword
def getRange(line,r):
	for i in range(line,r):
		getWant(i)

def getKeyword():
	try:
		conn = MySQLdb.connect('localhost','root','','heziliang',charset='utf8')#本地数据库
		print 'Connection Localhost Successful...'
	except:
		print 'Connection Localhost Fail...'
	try:
		with conn:#拿关键词
			cur = conn.cursor()
			sql = getSql()
			cur.execute(sql)
			conn.commit
		conn.close()
		print 'Getkeyword  Successful...'
	except:
		print 'Getkeyword  Fail...'
	data = cur.fetchall()
	return data	
def getUrl(data):	
	global num
	for row in data:#拼接url	
		keyword_list.append(row[0])
		url = 'http://m.baidu.com/s?word=%s' %row[0].encode('utf-8')
		url_list.append(url)
		num += 1
def inputAliyunDB(match,all):#将结果写入阿里云数据库
	rate = float(match)/all*100
	try:
		conn2 = MySQLdb.connect('ip','user','pass','baikedb',charset='utf8')
		print 'Connection Successful...'
	except:
		print 'Connection Fail...'
	try:
		with conn2:
			cur2 = conn2.cursor()
			sql = 'update baidu set waprank = %s where date="%s"' %(rate,today)
			cur2.execute(sql)
			conn2.commit
		conn2.close()
		print 'Input AliyunDB Successful...'
	except:
		print 'Input AliyunDB Fail...'
def main():
	print 'Begin'
	data = getKeyword()
	getUrl(data)
	totalThread  = threadNum
	global num	
	global all	
	global match
	gap = num/totalThread
	thread_list = []
	for line in range(0,num,gap):#num = 1000,gap = 100
		t = threading.Thread(target=getRange,args=(line,line+gap))#注意最后一个线程中，list Index out of range，num要可以被totalThread整除
		t.start()	
		thread_list.append(t)
	for tt in thread_list:
		tt.join()
	print match
	print all
	print '%.1f'%((float(match)/all)*100)+'%'
	print 'Calculate Done...'
	print 'Input AliyunDB Begin...'
	inputAliyunDB(match,all)
	print 'Input Done...'

mutex = threading.Lock()
main()
