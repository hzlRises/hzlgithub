#coding:utf-8
''' 提取百度关键词排名首页的真实地址，并过滤（隐形）阿拉丁及开放平台 '''
import urllib2,urllib,requests,re

word_list = ['SEO'] #放入你要查的关键词

''' 提取加密地址的正则 '''
Url_Req = re.compile(r'<div class="f13"><a target="_blank" href="(http://www.baidu.com/link\?url=[^\s|&|"]*)')

for line in word_list:
	url = 'http://www.baidu.com/s?wd=%s' %urllib.quote(line) #对查询词编码,构建查询url,查询前三页可添加&rn=30
	html = urllib2.urlopen(url).read()
	urls = Url_Req.findall(html) #采集加密的地址
	for line in urls:
		header = requests.head(line).headers #获取header内容，以字典的方式返回
		print header['location'] #打印真实地址
		file = open('realurls.txt','a')
		file.write(header['location']+'\n')		
	file.close()