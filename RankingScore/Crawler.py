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
def getWant(line):
	keyword = sheet1.row_values(line)[0]		
	url = url_list[line]
	c = pycurl.Curl()
	c.setopt(c.URL,url)
	c.setopt(c.CONNECTTIMEOUT, 60)
	c.setopt(c.TIMEOUT,120) 
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
				sql = 'insert into t_rank_copy (keyword,url,pcrank) values("%s","%s","%s")' %(keyword,serpUrl,line+1) 
				cur.execute(sql)
				conn.commit()	
		print keyword+'done'		
#		sleep(0.1)
	except:
		print "An error has occurred..."
	
	#写入txt
	'''	
	with open('result.txt',r'a+') as my:
		my.write(keyword+'\n')		
	for line in range(10):		
		serpUrl = jsondata["feed"]["entry"][line]["url"]
		print serpUrl
		with open('result.txt',r'a+') as my:
			my.write(serpUrl+'\n')
	'''
	#写入excel
	'''	
	step = 0	
	for line in range(10):
		serpUrl = jsondata["feed"]["entry"][line]["url"]
		sql = 'insert into t_rank_copy (keyword,url,pcrank) values("%s","%s","%s")' %(keyword,serpUrl,line+1) 					
		sheet.write(index+step,0,keyword)
		sheet.write(index+step,1,serpUrl)
		sheet.write(index+step,2,line+1)
		step += rows
		#步长，keyword.xlsx里有多少词步长就必须设置成多少，写到excel里暂时还没想到好的方法，怎么让行数自增啊啊啊啊啊啊啊.....
	print keyword+'done'		
	sleep(0.5)
	wb.save("result.xls")
	'''
	mutex.release()

def getRange(line,r):
	for i in range(line,r):
		getWant(i)


'''
wb = xlwt.Workbook(encoding = 'ascii')#新建一个excel表格对象
sheet = wb.add_sheet('sheet0')#指定table名称sheet0    ,cell_overwrite_ok=True

sheet.write(0,0,'keyword')
sheet.write(0,1,'url')
sheet.write(0,2,'pcrank')
'''

totalThread  = 10

url_list = []

mutex = threading.Lock()

data = xlrd.open_workbook('keyword.xlsx')
sheet1 = data.sheets()[0]#第一个表
rows = sheet1.nrows#行数

for i in range(rows):		
	url = 'http://www.baidu.com/baidu?wd=%s&tn=json' %sheet1.row_values(i)[0].encode('utf-8')#这个编码啊啊啊啊啊啊啊...
	url_list.append(url)
	
gap = rows/totalThread

for line in range(0,rows,gap):
	t = threading.Thread(target=getRange,args=(line,line+gap))#注意最后一个线程中，list Index out of range，num要可以被totalThread整除
	t.start()
	sleep(1)
