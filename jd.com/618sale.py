#coding:utf-8
import requests
from bs4 import BeautifulSoup
import sys
sys.getdefaultencoding()
def main():
	for line in open('url.txt'):
		r = requests.get(line.strip())
		s = BeautifulSoup(r.content,"lxml")
		title = s.title.get_text().replace('	','').replace('\n','')
		if u'京东618' in title:
			print title
			if u'全品类' in title:
				print 'warning'
		else:
			print('\n')
			print '------------------------------------------------------'
			print title
			print line.strip()
			if u'全品类' in title:
				print 'warning'
			print '------------------------------------------------------'
			print('\n')
main()
