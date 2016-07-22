#coding:utf-8
import requests,re,sys
while 1:
	url = 'http://www.baidu.com/s'
	print '---------------------------------PC-related'
	word = raw_input()
	keyword = word.decode('gbk').encode('utf-8')
	if word == 'over':
		sys.exit()
	payload = {'tn':'baidurs2top','wd':'%s'%keyword}
	r = requests.get(url,params=payload)	
	kw = r.content.replace(',','\n')
	print kw.decode('utf-8').encode('gbk')