#coding:utf-8
import urllib2
import sys
import re
import pycurl
import StringIO
reload(sys)
sys.setdefaultencoding('utf-8')
url = 'http://home.fang.com/zhishi/'
html = urllib2.urlopen(url).read()
youlian = re.search(r'<div class="links">([\s\S]*)</ul>',html)
link = re.findall(r'<li><a href="(.*)" target',youlian.group(0))

for url in link:
	c = pycurl.Curl()
	c.setopt(c.URL,url)
	c.setopt(c.FOLLOWLOCATION, True)
	c.setopt(c.MAXREDIRS,2)
	b = StringIO.StringIO()
	c.setopt(c.WRITEFUNCTION, b.write)
	c.perform()
	code = b.getvalue()
	match = re.search(r'home.fang.com/zhishi/',code)
	with open('result.txt',r'a+') as my:
		if match:
			print url+'yes'			
		else:
			print url+'no'
			my.write(url+'\n')