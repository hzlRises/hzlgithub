#coding:utf-8
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("sss.html"),"lxml")

tags = soup.find_all('a',attrs={'class':'grace-table-value ng-binding'})

fi = open('bbb.txt',r'a+')
num = 0
for tag in tags:
	print tag.get_text()
	if num % 20 == 19:
		fi.write(tag.get_text()+'\n')
	else:
		fi.write(tag.get_text()+'>')
	num += 1
