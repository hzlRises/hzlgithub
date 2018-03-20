#coding:utf-8
import requests,time
from bs4 import BeautifulSoup
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "UM_distinctid=16101ada415525-0d24551773a595-454c092b-100200-16101ada416307; bdshare_firstime=1516151612749; Hm_lvt_4752611d874ab431605fa080036e93af=1520843961,1520843964,1520844038,1521013704; _haicha=27385bdeafead0ba20027b78e7485476; CNZZDATA2903449=cnzz_eid%3D881119266-1516147207-null%26ntime%3D1521529684",
    "Host": "www.puercn.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",    
}
def main():
	f = open('heicha_url.txt',r'w+')
	for i in range(1,18):
		print i
		time.sleep(0.1)
		url = 'http://www.puercn.com/cpp/heicha/index_%s.html'%i
		r = requests.get(url,headers=headers)
		s = BeautifulSoup(r.content,"lxml")
		h3tag = s.find_all('h3')
		for item in h3tag:
			#print item.find('a').get('href')	
			f.write(item.find('a').get('href')+'\n')
	f.close()



if __name__ == '__main__':
	main()