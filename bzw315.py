#coding:utf-8
from time import ctime
import pycurl
import re
import StringIO
import random
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
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
    ]
    newUa = random.choice(uaList)
    return newUa
def getHtml(url):
	headers = [
		"Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Encoding:gzip, deflate, br",
		"Accept-Language:zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
		"Connection:keep-alive",
		"Host:baike.bzw315.com",
		"User-Agent:%s" % getUA()
	]
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
	
	
	