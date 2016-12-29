#coding:utf-8
author = 'heziliang'
import requests,re,time,string
from bs4 import BeautifulSoup
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "",
    "Host": "www.kongfz.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",    
}

for word in string.uppercase:	
	r_fir = requests.get('http://www.kongfz.com/topic/%s/'%word,headers=headers)	
	for page in re.findall(r'</span><a href="/topic/A-(\d+)/',r_fir.content):
		print page
		for i in range(1,int(page)+1):
			url = 'http://www.kongfz.com/topic/%s-%s/' %(word,i)
			r = requests.get(url,headers=headers)
			for title in re.findall(r'title="(.*)"',r.content):
				print title
				with open('%s.txt'%word,r'a+') as my:
					my.write(title+'\n')
			time.sleep(1.5)
