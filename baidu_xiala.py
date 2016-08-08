#coding:utf-8
import re
import urllib2
from time import ctime
print 'Begin:%s' %ctime()
f = open('result.txt',r'w')
file = open('kws.txt')
for line in file:
	line = line.strip()
	url = 'http://suggestion.baidu.com/su?wd=%s' %line
	html = urllib2.urlopen(url).read()
	pattern = re.compile(r'"(.*?)"')
	result = pattern.findall(html)
	f.writelines(line+'\n' for line in result)
	print '%s done' %line
f.close()
print 'End:%s' %ctime()
