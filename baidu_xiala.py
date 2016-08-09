#coding:utf-8
#kws.txt以utf-8编码
import re,urllib2,time
from time import ctime
print 'Begin:%s' %ctime()
start = time.clock()
f = open('result.txt',r'a+')
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
end = time.clock()
print 'End:%s' %ctime()
print 'RunTime: '+'%1.f s' %(end-start)
