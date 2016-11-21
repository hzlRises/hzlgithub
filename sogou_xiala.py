#coding:utf-8
#kws.txt以utf-8编码
'''
author = 'heziliang'
'''
import re,urllib2,time
from time import ctime
print 'Begin:%s' %ctime()
start = time.clock()
f = open('result.txt',r'a+')
file = open('jianjun.txt')
for line in file:
	line = line.strip()#http://www.sogou.com/suggnew/ajajjson?type=web&key=seo
	url = 'http://www.sogou.com/suggnew/ajajjson?type=web&key=%s' %line
	html = urllib2.urlopen(url).read()
	
	pattern = re.compile(r'\(\[".*"\,\[(".*?")\]')
	result = pattern.findall(html)
	
	f.writelines(line.replace(',','\n').replace('"','')+'\n' for line in result)
	print '%s done' %line
f.close()
end = time.clock()
print 'End:%s' %ctime()
print 'RunTime: '+'%1.f s' %(end-start)
