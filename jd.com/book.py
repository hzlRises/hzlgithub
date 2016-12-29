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
'''
#coding:utf-8
import requests,re,time,string,random
from bs4 import BeautifulSoup
def getUA():
	uaList = [
		'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1;+.NET+CLR+1.1.4322;+TencentTraveler)',
		'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1;+.NET+CLR+2.0.50727;+.NET+CLR+3.0.4506.2152;+.NET+CLR+3.5.30729)',
		'Mozilla/5.0+(Windows+NT+5.1)+AppleWebKit/537.1+(KHTML,+like+Gecko)+Chrome/21.0.1180.89+Safari/537.1',
		'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1)',
		'Mozilla/5.0+(Windows+NT+6.1;+rv:11.0)+Gecko/20100101+Firefox/11.0',
		'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+SV1)',
		'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+GTB7.1;+.NET+CLR+2.0.50727)',
		'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+KB974489)',
		'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
		'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
		"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
		"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
	]
	newUa = random.choice(uaList) 
	return newUa

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
#    "Cookie": "aliyungf_tc=AQAAAPCwKmNNIA0AE3MmagNhDFYh3JrH; PHPSESSID=d72mofht5iet5mnjf27nnjp440; kfz-tid=c522d23cb2034d2aff21a1c8e44acdf8; shoppingCartSessionId=d7728a04d2c91d78b29b4bc642eb43a6; Hm_lvt_bca7840de7b518b3c5e6c6d73ca2662c=1482982081; Hm_lpvt_bca7840de7b518b3c5e6c6d73ca2662c=1482982081; Hm_lvt_33be6c04e0febc7531a1315c9594b136=1482982081; Hm_lpvt_33be6c04e0febc7531a1315c9594b136=1482982081",
    "Host": "www.kongfz.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": getUA(),    
}

word = 'E'
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


'''
