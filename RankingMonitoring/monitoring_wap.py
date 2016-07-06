#coding:utf-8
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
date = time.strftime("%Y-%m-%d",time.localtime(time.time()))
conn = MySQLdb.connect('localhost','root','','heziliang',charset='utf8')
match = 0
all = 0
percentage = 0
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
		c.setopt(c.CONNECTTIMEOUT, 60)
		c.setopt(c.TIMEOUT,120) 
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
		
url_list = []
keyword_list = []

with conn:
	cur = conn.cursor()
	sql = 'select keyword from t_keyword order by rand() limit 1000'
	cur.execute(sql)
	conn.commit
conn.close()
data = cur.fetchall()
num = 0
for row in data:	
	keyword_list.append(row[0])
#	print row[0]
	url = 'http://m.baidu.com/s?word=%s' %row[0].encode('utf-8')
	url_list.append(url)
	num += 1
#	print url
	
totalThread  = 20
gap = num/totalThread
mutex = threading.Lock()
thread_list = []

for line in range(0,num,gap):#num = 1000,gap = 100
	t = threading.Thread(target=getRange,args=(line,line+gap))#注意最后一个线程中，list Index out of range，num要可以被totalThread整除
	t.start()	
	thread_list.append(t)
for tt in thread_list:
	tt.join()
print match
print all
print percentage