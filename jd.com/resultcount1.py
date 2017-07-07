#coding:utf-8
import requests,sys,time
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
def main():
	for line in open('result.txt'):
		try:
			url = 'https://search.jd.com/Search?keyword=%s&enc=utf-8'%line.strip()
			r = requests.get(url)
			s = BeautifulSoup(r.content,'lxml')
			resCount = s.find('span',attrs={'id':'J_resCount'}).get_text()
			if '+' in str(resCount):
				resCount = resCount.replace('+','')
			with open('countNum_.txt',r'a+') as my:
				my.write(line.strip()+':'+resCount+'\n')
		except Exception,e:
			with open('fail.txt') as my:
				my.write(line.strip()+'\n')
			print e
			continue 
main()
