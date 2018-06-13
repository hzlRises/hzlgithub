#coding:utf-8
from bs4 import BeautifulSoup

import requests,sys,time
reload(sys)
sys.setdefaultencoding('utf-8')
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "accept-Encoding": "gzip, deflate, br",
    "accept-Language": "zh-CN,zh;q=0.8",
    "cache-control": "max-age=0",
    "cookie": '',
    "if-modified-since": "Mon, 11 Sep 2017 10:11:35 GMT",
    "referer": "https://list.jd.com/list.html?cat=1672,2575,5257",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
}
def main():
	for url in open('url_img.txt'):
		time.sleep(0.5)
		str_list = []
		try:
			r = requests.get(url.strip(),headers=headers,timeout=60)
			s = BeautifulSoup(r.content,"lxml")
		except Exception,e:
			print 'requests error...'
			with open('img_error.txt',r'a+') as my:
				my.write(url.strip()+','+'requests error'+'\n')
		try:
			url_tag = s.find('ul',attrs={"class":"lh"}).find_all('img')
		except Exception,e:
			print 'analysis error...'
			with open('img_error.txt',r'a+') as my:
				my.write(url.strip()+','+'analysis error'+'\n')
		for img in url_tag:
			str_list.append(img.get('src'))
		
		with open('re_img.txt',r'a+') as my:
			my.write(url.strip()+'|'+",".join(str_list)+'\n')
		print url.strip()
if __name__ == '__main__':
	main()
