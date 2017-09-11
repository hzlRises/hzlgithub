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
    "cookie": 'user-key=e3d00dbc-c8fa-42b6-96e7-e932379e7366; TrackID=1WNjCq0T_OBs_k1l2BLZlcN-8zExv4rSd-h3rSJbWo1c8occcD2ZuWsozGWjWZbosQU_NI3_Mfhq4ooBgQRvJ1A; cn=0; mt_xid=V2_52007VwMXWltaUlMfSxleAmIGFVFYWVRSF0EpDABmVxpXVQtODhdIG0AANAUXTlRfVQkDGh9dVjcKEAIPXgcJL0oYXAN7AhpOXFxDWhhCGV4OZgMiUG1YYloeThhcAGMKFWJdXVRd; unpl=V2_ZzNtbRFeQBBzAUYEKRkOB2IDEw4RUEQTclgSAX0cWwRvBxIPclRCFXMUR1xnGFsUZwAZXUVcQRRFCEdkeBFVBGUKEl1KZxMXdwtOUX0aXDVXABJtSmdDEH0ORFRyGV4FZQQXWEVURhRzAE5cSylaAVczRAkaDgdNRQpGUHIbWAVhCiJcclZzXhsJC1R%2bEVoHZwoSX0JVRBBwD0VReh9UDW8zE21B; _AIRLINE_VALUE_="z8PDxSyxsb6pLDIwMTctMTAtMDgsMSxPVw=="; _pst=jd_53c836d89d9e0; unick=jd_619237350; pin=jd_53c836d89d9e0; _tp=v3jaNqGkC7JI3eyGwLdKcShMkQUtIh4HZu%2FnFibvd98%3D; ipLocation=%u5317%u4EAC; areaId=1; ipLoc-djd=1-2810-4194-0; sso.jd.com=daea1326bf48483d835c681584e9c8d8; dmpjs=dmp-d6192601679053d017c712d7732c24dbb1fc3d5; __jdv=122270672|dmp|dmp_52|cpc|dmp_52_11104_d6192601679053d017c712d7732c24dbb1fc3d5_1505117122|1505117124118; __jda=122270672.1497318131364462407999.1497318131.1505117124.1505123198.13; __jdb=122270672.19.1497318131364462407999|13.1505123198; __jdc=122270672; __jdu=1497318131364462407999; 3AB9D23F7A4B3C9B=SRFBEFEUQOW6A6HQK43UV4IIDN2F3ZNPV2LWJPBJJWDCACNBBMNYPY7ZYPLYE43ZEQGT7BO74O3V3VOUNSDW3C5KPI',
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
