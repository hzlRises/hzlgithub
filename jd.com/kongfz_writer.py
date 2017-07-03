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
	for letter in string.uppercase:
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
			r = requests.get(url,headers=headers)
			s = BeautifulSoup(r.content,"lxml")
			writer = s.find_all('img')
			for i in writer:
				print i.get('alt')
				if u'孔夫子旧书网' in i.get('alt'):
					pass
				else:
					with open('%s.txt'%letter,r'a+') as my:
						my.write(i.get('alt')+'\n')
			time.sleep(3)
		time.sleep(60)
main()
