#coding:utf-8
import requests
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
import random
import time
reload(sys)
sys.setdefaultencoding('utf8')
conn = MySQLdb.connect('localhost','root','','rank',charset='utf8')

def getUA():
	uaList = [
		'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1;+.NET+CLR+1.1.4322;+TencentTraveler)',
		'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1;+.NET+CLR+2.0.50727;+.NET+CLR+3.0.4506.2152;+.NET+CLR+3.5.30729)',
		'Mozilla/5.0+(Windows+NT+5.1)+AppleWebKit/537.1+(KHTML,+like+Gecko)+Chrome/21.0.1180.89+Safari/537.1',
		'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1)',
		'Mozilla/5.0+(Windows+NT+6.1;+rv:11.0)+Gecko/20100101+Firefox/11.0',
		'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+SV1)',
		'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+GTB7.1;+.NET+CLR+2.0.50727)',
		'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+KB974489)',
		'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
		'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
		"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
		"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
	]
	newUa = random.choice(uaList) 
	return newUa


def getWant(line):
	keyword = sheet1.row_values(line)[0]		
	url = url_list[line]
	
	headers = {
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
		"Accept-Encoding":"gzip, deflate, br",
		"Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
		"Cache-Control":"no-cache",
		"Connection":"keep-alive",
		"Cookie":"BAIDUID=2033772EEBCB46478009DBFED664CC4E:FG=1; BIDUPSID=2033772EEBCB46478009DBFED664CC4E; PSTM=1522486596; __cfduid=d528bcd15bea5bb7521cb3997076e327e1522489086; MSA_WH=375_812; BDUSS=Gh2UGdwOU5uRGZLOXpJTlRZN0Noa0Y0RGNVbWVOdnQ2bUU3V0xyWDVIQ3FZMnBjQVFBQUFBJCQAAAAAAAAAAAEAAABh7s8nxLDErGxpZmUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKrWQlyq1kJcd; BD_UPN=12314353; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-%3A; locale=zh; sug=3; sugstore=0; ORIGIN=0; bdime=0; H_PS_645EC=04c1I5Hag20s%2FajYlmyDY22dPgHuyyVILkUI3XqTM4ocVPce8Z6O5R1zmRI; BDRCVFR[VjobkFsAYtR]=mk3SLVN4HKm; delPer=0; BD_CK_SAM=1; PSINO=2; BDSVRTM=102; H_PS_PSSID=",
		"Host":"www.baidu.com",
		"Pragma":"no-cache",
		"Upgrade-Insecure-Requests":"1",
		"User-Agent":getUA(),
	}
	r = requests.get(url,headers=headers,timeout=60)
	html = r.content
	'''
	c = pycurl.Curl()
	c.setopt(c.URL,url)
	c.setopt(c.CONNECTTIMEOUT, 60)
	c.setopt(c.TIMEOUT,120) 
	b = StringIO.StringIO()
	c.setopt(c.WRITEFUNCTION,b.write)
	c.perform()
	html = b.getvalue()
	'''	
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
		print i
		time.sleep(5)


'''
wb = xlwt.Workbook(encoding = 'ascii')#新建一个excel表格对象
sheet = wb.add_sheet('sheet0')#指定table名称sheet0    ,cell_overwrite_ok=True
sheet.write(0,0,'keyword')
sheet.write(0,1,'url')
sheet.write(0,2,'pcrank')
'''

totalThread  = 1

url_list = []

mutex = threading.Lock()

data = xlrd.open_workbook('keyword.xlsx')
sheet1 = data.sheets()[0]#第一个表
rows = sheet1.nrows#行数

for i in range(rows):		
	url = 'http://www.baidu.com/baidu?wd=%s&tn=json' %sheet1.row_values(i)[0]#.encode('utf-8')#这个编码啊啊啊啊啊啊啊....
	
	url_list.append(url)
	
gap = rows/totalThread

for line in range(0,rows,gap):
	t = threading.Thread(target=getRange,args=(line,line+gap))#注意最后一个线程中，list Index out of range，num要可以被totalThread整除
	t.start()
	sleep(1)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
