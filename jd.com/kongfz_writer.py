#coding:utf-8
import requests,sys,time
import string
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')


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

def main():
	for letter in ['I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
		print letter
		url = 'http://www.kongfz.com/writer/%s_1/'%letter
		r = requests.get(url,headers=headers)
		s = BeautifulSoup(r.content,"lxml")
		pageBox = s.find('div',attrs={'class':'page_box'}).find_all('a')
		page_list = []
		for page in pageBox:
			if str.isdigit(str(page.get_text())):
				page_list.append(page.get_text())
			else:
				pass
		pageNum = page_list[-1]
		#以上只是确定某个字母开头的最大页数
		for i in range(1,int(pageNum)+1):#20886
			url = 'http://www.kongfz.com/writer/%s_%s/'%(letter,i)
			try:
				r = requests.get(url,headers=headers,timeout=10)
				s = BeautifulSoup(r.content,"lxml")
				writer = s.find_all('img')
				for j in writer:
					print j.get('alt')
					if u'孔夫子旧书网' in j.get('alt'):
						pass
					else:
						with open('%s.txt'%letter,r'a+') as my:
							my.write(j.get('alt')+'\n')
				time.sleep(1)			
			except Exception,e:
				print e
				time.sleep(60)
				continue
			print i
		time.sleep(60)
main()


'''
#coding:utf-8
import requests,sys,time
import string
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": '''shoppingCartSessionId=b0d68aa53c8a274f983e894d51513ddf; reciever_area=1000000000; PHPSESSID=b3fb5743e7aeb41f5e9dbef15a22564b6dec7523; kfz-tid=75b885cdd2d6f8558151de5b31821f08; acw_tc=AQAAAPdxSi17LwwAHHMmap1fImnd3l6W; KFZ_ADMIN_SESSION_NAME=qc7ke79nkfj6nvdv1du73akr96''',
    "Host": "lib.kongfz.com",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",    
}

def main():
	for i in range(1,4):
		url = 'http://lib.kongfz.com/author/occu_291/p%s/'%i
		r = requests.get(url,headers=headers,timeout=60)
		s = BeautifulSoup(r.content,"lxml")		
		writer = s.find_all('li',attrs={"class":"book_box"})
		
		for p in writer:
			print p.get_text().strip()
			with open('result.txt',r'a+') as my:
				my.write(p.get_text().strip()+'\n')
		time.sleep(1)
		
main()


'''
