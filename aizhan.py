#coding:utf-8
import requests,time,sys,re
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
	"Cache-Control": "no-cache",
	"Connection": "keep-alive",
	"Cookie": "Hm_lvt_b8865d93695223dea9b264b5d77c5188=1501239542,1501467157,1502093003,1502097616; allWords=%E7%9F%A5%E8%8C%B6%7C%E4%BA%8C%E8%90%A5%E9%95%BFSEO%2C0; _csrf=496249692f65a75662ee9216b84964a089ed27c98a0e394990d3b497d5e780a0a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22JtiTkBMjbKXVmpViyJOBqV3PSfN60_JQ%22%3B%7D; Hm_lvt_b37205f3f69d03924c5447d020c09192=1532335609; Hm_lpvt_b37205f3f69d03924c5447d020c09192=1532337686; allSites=jd.com%7Cmovie.jd.com%7Cjos.jd.com%7Cyp.m.jd.com%7Cchannel.jd.com%7Citem.jd.com%7Cwww.jd.com%7Cbaike.baidu.com%7Cwww.didiglobal.com%7Cheziliang.cn",
	"Host": "baidurank.aizhan.com",
	"Pragma": "no-cache",
	"Upgrade-Insecure-Requests": "1",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}


def get_max_page(dm):
	max_page = 1
	max_page_m = 1	
	
	url = 'https://baidurank.aizhan.com/baidu/%s/'%dm
	url_m = 'https://baidurank.aizhan.com/mobile/%s/'%dm
	
	r = requests.get(url,headers=headers,timeout=60)
	r_m = requests.get(url_m,headers=headers,timeout=60)
	
	s = BeautifulSoup(r.content,"lxml")
	s_m = BeautifulSoup(r_m.content,"lxml")
	try:
		a_tag = s.find('div',attrs={"class":"baidurank-pager"}).find_all('a')		
		max_page = a_tag[-1].get_text().strip()
	except Exception,e:
		print e
	try:
		a_tag_m = s_m.find('div',attrs={"class":"baidurank-pager"}).find_all('a')
		max_page_m = a_tag_m[-1].get_text().strip()
	except Exception,e:
		print e
	return max_page,max_page_m

		
def write_pc(dm,max_page):
	f = open('r_pc.txt',r'a+')
	for i in range(1,int(max_page)+1):		
		url = 'https://baidurank.aizhan.com/baidu/%s/-1/0/%s/position/1/'%(dm,i)
		r = requests.get(url,headers=headers,timeout=60)
		s = BeautifulSoup(r.content,"lxml")			
		tr = s.find('div',attrs={"class":"baidurank-list"}).find_all('tr')
		[soup.extract() for soup in s('tr',attrs={"class":"thead"})]
		[soup.extract() for soup in s('td',attrs={"class":"path"})]
		
		for t in tr:
			t = t.find_all('td')
			_str = dm + '>pc>'
			for td in t:
				td = td.get_text().strip()
				td = re.sub(r'[\s]*','',td)
				_str = _str + td +'>'
			f.write(_str+'\n')		
		time.sleep(1)
		print 'pc' + str(i)
		#break	
	f.close()
	
	
def write_m(dm,max_page_m):
	f = open('r_m.txt',r'a+')
	for i in range(1,int(max_page_m)+1):
		url = 'https://baidurank.aizhan.com/mobile/%s/-1/0/%s/position/1/'%(dm,i)
		r = requests.get(url,headers=headers,timeout=60)
		s = BeautifulSoup(r.content,"lxml")			
		tr = s.find('div',attrs={"class":"baidurank-list"}).find_all('tr')
		[soup.extract() for soup in s('tr',attrs={"class":"thead"})]
		[soup.extract() for soup in s('td',attrs={"class":"path"})]
		
		for t in tr:
			t = t.find_all('td')
			_str = dm + '>m>'
			for td in t:
				td = td.get_text().strip()
				td = re.sub(r'[\s]*','',td)
				_str = _str + td +'>'
			f.write(_str+'\n')		
		time.sleep(1)
		print 'm' + str(i)
		#break	
	f.close()
	
	
	
def main():
	
	for dm in open('domain.txt'):
		dm = dm.strip()
		print dm
		max_page,max_page_m = get_max_page(dm)		
		print dm,max_page,max_page_m
		write_pc(dm,max_page)		
		write_m(dm,max_page_m)		
		time.sleep(5)
	
	
if __name__ == '__main__':
	main()
	
