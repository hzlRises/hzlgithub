#coding:utf-8
'''url放到url.txt中'''
'''结果保存在result.txt'''
import re
import urllib2
def getHtml(url):
	html = urllib2.urlopen(url).read()
#	pattern = re.compile(r'rtright',html)
#	result = pattern.findall(html)
	result = re.findall(r'rtright',html)
	return result
f=open('result.txt',r'a')
for line in open('url.txt'):
	sum = 0
	for line in getHtml(line):
		sum += 1
	#print sum	
	f.write(str(sum)+'\n')
f.close()