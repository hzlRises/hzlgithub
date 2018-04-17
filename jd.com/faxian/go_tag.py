#coding:utf-8
import requests,sys,re,pycurl,StringIO,time,xlrd,xlwt,HeaderData,md5,json
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver
reload(sys) 
sys.setdefaultencoding('utf-8')

def get_tag(title):	
	tag = ''
	url = 'http://custom.p-search.jd.local/?pagesize=1&qp_disable=no&client=&key=%s'%urllib.quote(title)
	print url
	r = requests.get(url)
	
	#JSON.Head.Query.WordSearchInfo.ShowWordOne
	try:
		j_data = json.loads(r.content.decode('gbk'))#.encode('utf-8')
		tag = j_data["Head"]["Query"]["WordSearchInfo"]["ShowWordOne"]	
	except Exception,e:
		print e		
	if tag:
		return tag
	else:
		return 'jd'

		
def main():
	for line in open('title_tag.txt'):
		kw = line.strip()
		with open('tag_result.txt',r'a+') as my:
			my.write(get_tag(kw.encode('gbk'))+'\n')
		
				
if __name__ == '__main__':	
	main()
	
