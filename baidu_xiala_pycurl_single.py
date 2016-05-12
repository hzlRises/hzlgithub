#coding:utf-8
from time import ctime
import pycurl
import re
import StringIO

def getUrl(keyword):
	url = 'http://suggestion.baidu.com/su?wd=%s' %keyword
	return url

def getHtml(url):
	c = pycurl.Curl();
	c.setopt(pycurl.CONNECTTIMEOUT, 60)
	c.setopt(pycurl.TIMEOUT,120)	
	c.setopt(pycurl.ENCODING, 'gzip,deflate')
	c.setopt(pycurl.URL, url)
	c.fp = StringIO.StringIO()
	c.setopt(c.WRITEFUNCTION, c.fp.write)
	c.perform()
	html = c.fp.getvalue()
	return html
	
def getXiala(html):
	pattern = re.compile(r'"(.*?)"')
	xiala = pattern.findall(html)
	return xiala
	
print 'Begin:%s' %ctime()
f = open('result.txt',r'w')
for line in open('kws.txt'):
	keyword = line.strip()
	url = getUrl(keyword)
	html = getHtml(url)
	xiala = getXiala(html)
	print '%s done'%keyword
	f.writelines(line+'\n' for line in xiala)
f.close()
print 'End:%s' %ctime()
	
	
	