#coding:utf-8
import threading
import json
import pycurl
import StringIO
import MySQLdb
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf8')
conn = MySQLdb.connect('localhost','root','','rank',charset='utf8')
def getWant(line):
	keyword = keyword_list[line]	
	url = url_list[line]
	c = pycurl.Curl()
	c.setopt(c.URL,url)
	b = StringIO.StringIO()
	c.setopt(c.WRITEFUNCTION,b.write)
	c.perform()
	html = b.getvalue()
	mutex.acquire()	
	jsondata = json.loads(html)
	#写入MySQL
	try:
		with conn:
			cur = conn.cursor()
			for line in range(10):
				serpUrl = jsondata["feed"]["entry"][line]["url"]
				sql = 'insert into t_rank (keyword,url) values("%s","%s")' %(keyword,serpUrl) 
				cur.execute(sql)
				conn.commit()	
		print keyword+'done'		
		sleep(1)
	except:
		print "An error has occurred..."
	'''
	#写到本地txt文件
	with open('result.txt',r'a+') as my:
		my.write(keyword+'\n')		
	for line in range(10):		
		serpUrl = jsondata["feed"]["entry"][line]["url"]
		print serpUrl
		with open('result.txt',r'a+') as my:
			my.write(serpUrl+'\n')
	'''
	mutex.release()

def getRange(line,r):
	for i in range(line,r):
		getWant(i)

file = open('keyword.txt',r'r')
totalThread  = 18	
keyword_list = []
url_list =[]
mutex = threading.Lock()
sum = 0
for line in file:
	line = line.strip()
	keyword_list.append(line)
	url = 'http://www.baidu.com/baidu?wd=%s&tn=json' %line
	url_list.append(url)
	sum += 1

gap = sum/totalThread

for i,j in enumerate(url_list):
	lastIndex = i

for line in range(0,lastIndex,gap):
	t = threading.Thread(target=getRange,args=(line,line+gap))#注意最后一个线程中，list Index out of range，num要可以被totalThread整除
	t.start()