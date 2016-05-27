#coding:utf-8
import re
import pycurl
import StringIO
import threading
def getTotal(line):	
	url = url_list[line]
	keyword_list[line]
	c = pycurl.Curl()
	c.setopt(pycurl.URL, url)
	c.setopt(pycurl.FOLLOWLOCATION,True)
	c.setopt(pycurl.MAXREDIRS,3)
	c.setopt(pycurl.CONNECTTIMEOUT,60)
	c.setopt(pycurl.TIMEOUT,120)
	c.setopt(pycurl.ENCODING,'gzip,deflate')
	c.fp =StringIO.StringIO() 
	c.setopt(c.WRITEFUNCTION, c.fp.write)
	c.perform()
	html = c.fp.getvalue()
	mutex.acquire()
	result = re.findall(r'<total>(.*?)</total>',html)	
	f.write(keyword_list[line]+result[0]+'\n')
	print result[0]
	mutex.release()
	
def getRange(line,r):
	for i in range(line,r):
		getTotal(i)
		
totalThread = 650
url_list =[]
keyword_list = []
mutex = threading.Lock()

f = open('result.txt',r'w')
file = open('kws.txt')
sum = 0
for line in file:
	sum += 1
	line = line.strip()	
	keyword_list.append(line)
	url = 'http://search.fang.com/news/searchxml1.jsp?q=%s&newschannel=家居网&start=0&occur=and&fld=title'  %line
	url_list.append(url)
gap = sum/totalThread
for i,j in enumerate(url_list):
	lastIndex = i
for line in range(0,lastIndex,gap):
	t = threading.Thread(target=getRange,args=(line,line+gap))
	t.start()
