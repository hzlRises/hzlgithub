#coding:utf-8
from time import ctime
import pycurl,re,StringIO,random

def getHtml(url):
	c = pycurl.Curl()
	c.setopt(pycurl.CONNECTTIMEOUT, 60)
	c.setopt(pycurl.TIMEOUT,120)	
	c.setopt(pycurl.ENCODING, 'gzip,deflate')
	c.setopt(pycurl.URL, url)
	c.fp = StringIO.StringIO()
	c.setopt(c.WRITEFUNCTION, c.fp.write)
	c.perform()
	html = c.fp.getvalue()
	return html
def getWord(html):
	pattern = re.compile(r'<li><a.*?>(.*?)</a></li>')
	word = pattern.findall(html)
	return word
print 'Begin:%s' %ctime()
f = open('result.txt',r'w')
url = ['http://baike.bzw315.com/zx/','http://baike.bzw315.com/sj/','http://baike.bzw315.com/cp/','http://baike.bzw315.com/pp/','http://baike.bzw315.com/sh/']
for line in url:
	html = getHtml(line)
	word = getWord(html)
	f.writelines(line+'\n' for line in word)
f.close()
print 'End:%s' %ctime()
	
	
	
