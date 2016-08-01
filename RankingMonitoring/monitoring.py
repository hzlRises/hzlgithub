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
today = time.strftime("%Y-%m-%d",time.localtime(time.time()))#获取当前日期0000-00-00
conn = MySQLdb.connect('localhost','root','','rank',charset='utf8')#本地数据库
match = 0#初始化可以匹配的数量
all = 0#初始化查询关键词所有的数量
percentage = 0#初始排名比值

def getIfmatch(html):#是否匹配	
	pattern = re.compile(r'home.fang.com\\/zhishi\\/')
	zhishiurl = pattern.findall(html)
	bool = zhishiurl
	return bool
	
def getWant(line):#计算匹配占比	
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
		mutex.release()
	except:
		print '%s Empty reply from server' %keyword	
def getRange(line,r):#每个线程控制的数量
	for i in range(line,r):
		getWant(i)

def inputAliyunDB(match,all):#将查询的结果插入到阿里云的数据库	
	rate = float(match)/all*100
	try:
		conn2 = MySQLdb.connect('IP','USER','PASS','db',charset='utf8')
		print 'Connection successful...'
	except:
		print 'Connection fail...'
	try:
		with conn2:
			cur2 = conn2.cursor()
			sql = 'INSERT INTO `baidu` (pcrank,waprank,date) VALUES (%s,0,"%s")' %(rate,today)#waprank这里先写死，查询wap端时再update
			cur2.execute(sql)
			conn2.commit
		conn2.close()
		print 'Input aliyunDB successful...'
	except:
		print 'Input aliyunDB fail...'

print 'begin'
with conn:#拿关键词
	cur = conn.cursor()
	sql = 'select keyword from t_keyword order by rand() limit 20'
	cur.execute(sql)
	conn.commit
conn.close()
data = cur.fetchall()
num = 0
keyword_list = []
url_list = []
for row in data:#拼接url	
	keyword_list.append(row[0])
	url = 'http://www.baidu.com/baidu?wd=%s&tn=json' %row[0].encode('utf-8')
	url_list.append(url)
	num += 1
totalThread  = 10#设置线程数
gap = num/totalThread#设置步长
mutex = threading.Lock()#设置锁
thread_list = []
for line in range(0,num,gap):
	t = threading.Thread(target=getRange,args=(line,line+gap))#注意最后一个线程中，list Index out of range，num要可以被totalThread整除
	t.start()#循环开
	thread_list.append(t)
for tt in thread_list:#循环join
	tt.join()
#打印出有排名占比	
print match
print all
print '%.1f'%((float(match)/all)*100)+'%'
print 'Calculate done...'
print 'Input aliyunDB begin...'
inputAliyunDB(match,all)
print 'Input done'
