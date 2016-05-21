#coding:utf-8
import urllib2,re

'''
使用时替换url即可，本程序采集爱站所有目录关键词，保存在 'kws.txt'
'''

url = 'http://baidurank.aizhan.com/baidu/ent.sina.com.cn/'

#爱站提取关键词及对应指数的正则
KWS_REG = re.compile('<td class="blue t_l word">\s*<a .*?>(.+?)</a>[\s\S]*?class="zhishu".*?>(.+?)</a>')

# 提取当前所有页数的正则
TOTAL_PAGE_AREA_REG = re.compile('<div class="page">([\s\S]*?)</div>')
TOTAL_PAGE_REG = re.compile('<a .*?>(\d+)</a>')

# 提取当前所有目录的正则
Total_Category_Area_Req = re.compile('<ul class="urlpath">([\s\S]*?)</ul>')
Total_Category_Req = re.compile('<a href="(http://baidurank.aizhan.com/baidu/.*?)">')

def grtHtml(url):
	'''给定一个URL，打开并读取html'''
	html = urllib2.urlopen(url).read()
	return html
	
def html_parse_category(html):
    '''给定一个URL，提取所有目录'''
    area = Total_Category_Area_Req.search(html).group(0)
    category = Total_Category_Req.findall(area)
    return category

def html_parse_page(html):
	'''给定一个爱站页面的html，提取出最大页数'''
	try:
		area = TOTAL_PAGE_AREA_REG.search(html).group(1)
		pages = TOTAL_PAGE_REG.findall(area)
		max_page = max([ int(page) for page in pages ])
		return max_page
	except:
		return 1

def html_parse_kws(html):
	'''给定一个爱站页面的html，提取出上面的关键词'''
	matches = KWS_REG.findall(html)
	return matches

html = grtHtml(url)
category = html_parse_category(html)

for line in category:
	html = grtHtml(line)
	max_page = html_parse_page(html)
	print u'\n正在采集目录%s \n' %line
	
	if line == url:
		for num in xrange(1,max_page+1):
			url = line + '-1/0/%d/' %num
			print u'正在采集页面%s' %url
			html = grtHtml(url)
			kws = html_parse_kws(html)
			for k,v in kws:
				f = open('kws.txt','a')
				f.write(k +'\n')
			f.close()
	else:
		for num in xrange(1,max_page+1):
			url = line + '0/%d/' %num
			print u'正在采集页面%s' %url
			html = grtHtml(url)
			kws = html_parse_kws(html)
			for k,v in kws:
				f = open('kws.txt','a')
				f.write(k +'\n')
			f.close()