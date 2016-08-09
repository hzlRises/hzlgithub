#coding:utf-8
import urllib
import re
def getVideo():
	html = urllib.urlopen('http://www.budejie.com/video/').read()
	pattern = re.compile(r'data-mp4="(.*?)"')
	return re.findall(pattern,html)
for line in getVideo():
	urllib.urlretrieve(line,'video/ %s'%line.split('/')[-1]) 
