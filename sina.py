#coding:utf-8
import pycurl
import re
import StringIO
from time import ctime,sleep
'''
关键词放在kw.txt中，kw.txt文件需要用notepad++转换为ANSI编码
结果保存在result.txt中，示例：
http://finance.sina.com.cn/roll/2016-04-25/doc-ifxrprek3287200.shtml报告称首季大陆企业海外并购交易额超以往任何年度 中国新闻网 2016-04-25 16:56:17
'''
#获取网页代码
def getHtml(url):
	c = pycurl.Curl()
	c.setopt(pycurl.FOLLOWLOCATION,True)
	c.setopt(pycurl.MAXREDIRS,3)
	c.setopt(pycurl.CONNECTTIMEOUT,60)
	c.setopt(pycurl.ENCODING,'gzip,deflate')
	c.fp =StringIO.StringIO()
	c.setopt(pycurl.URL, url)
	c.setopt(c.WRITEFUNCTION, c.fp.write)
	c.perform()
	html = c.fp.getvalue()
	return html
#获取搜索结果页链接和标题
def getWant(html):
	pattern = re.compile('<h2><a href="(.*)</h2>')
	htmlContent = pattern.findall(html)
	htmlContentListToStr = ','.join(htmlContent)#列表转换为字符串，以逗号分割
	#替换掉没用的字符
	htmlContentListToStr = htmlContentListToStr.replace('" target="_blank">','').replace('<span style="color:#C03">','').replace('</span>','').replace('<span class="fgray_time">','').replace('</span>','').replace('</a>','')
	#字符串再转换为列表，方便写入文件换行
	htmlContentStrToList = htmlContentListToStr.split(',')
	return htmlContentStrToList
def getUrl(keyword):
	url = 'http://search.sina.com.cn/?q=%s&sort=time&sort=time&range=title&c=news&from=channel&page=1'% keyword
	return url
num = 0
f = open('result.txt',r'w')
for line in open('kw.txt'):
	num += 1
	keyword = line.strip()
	geturl = getUrl(keyword)
	html = getHtml(geturl)
	result = getWant(html)
	print 'begin:%s'%ctime()
	f.write('%s result:'%keyword+'\n')
	f.writelines(line+'\n' for line in result)#将列表依次写入TXT文件
	print '%s'%keyword+'done'
	print 'end:%s'%ctime()	
f.close()
