#coding:utf-8
import requests,sys,time
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
def getSerp(kw,num):
	try:
		url = 'http://www.baidu.com/s?wd=%s&tn=json'%kw
		r2 = requests.get(url)
		if 'item.jd.com' in r2.content:
			pass
		else:
			with open('countNum.txt',r'a+') as my:
				my.write(kw+'|'+num+'\n')
	except Exception,e:
		print e
		pass
def main():
	for line in open('result.txt'):
		try:
			url = 'https://search.jd.com/Search?keyword=%s&enc=utf-8'%line.strip()
			r = requests.get(url)
			s = BeautifulSoup(r.content,'lxml')
			resCount = s.find('span',attrs={'id':'J_resCount'}).get_text()
			if '+' in str(resCount):
				resCount = resCount.replace('+','')
				if int(str(resCount)) >= 10:
					getSerp(line.strip(),resCount)
					time.sleep(1)
		except Exception,e:
			print e
			continue

main()
