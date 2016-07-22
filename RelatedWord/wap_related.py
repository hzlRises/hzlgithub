#coding:utf-8
import requests,re,sys
from bs4 import BeautifulSoup
while 1:
	url = 'http://m.baidu.com/s'
	print '---------------------------------WAP-related'
	word = raw_input()
#	keyword = word.decode('gbk').encode('utf-8')
	if word == 'over':
		sys.exit()
	payload = {'word':'%s'%word}
	r = requests.get(url,params=payload)	
	soup = BeautifulSoup(r.content,"lxml")
	relativewords = soup.find(id="relativewords").find_all("a")
	for word in relativewords:
		print word.string