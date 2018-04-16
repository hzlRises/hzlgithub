#coding:utf-8
import	HeaderData,re,sys
import requests,time
from bs4 import BeautifulSoup

reload(sys) 
sys.setdefaultencoding('utf8')


file_name = 'article_zhuangxiu'


def main():	
	for i in range(1,610):#遍历每个一级导航下的所有圈子页数
		url = 'http://www.meilele.com/article/zhuangxiu/page-%s/'%i
		try:
			r = requests.get(url,headers=HeaderData.get_header(),timeout=60)				
			s = BeautifulSoup(r.content,"lxml")
			imatag = s.find_all('h2')			
			for a in imatag:
				url =  a.find('a').get('href')	
				f.write(url+'\n')
		except Exception,e:
			print e			
		time.sleep(0.1)
		print i
if __name__ == '__main__':
	f = open('%s_detail_url.txt'%file_name,r'a+')
	main()
	f.close()
	
	
	
	
'''
JD游戏 （电脑） > 全部圈子	http://group.jd.com/circle/all-circle/20000001.htm
手机站  > 全部圈子    		http://group.jd.com/circle/all-circle/20000151.htm
智能站  > 全部圈子			http://group.jd.com/circle/all-circle/20000121.htm
摄影站  > 全部圈子			http://group.jd.com/circle/all-circle/20000391.htm
娱乐站  > 全部圈子			http://group.jd.com/circle/all-circle/20000241.htm
妆比社(超市)  > 全部圈子	http://group.jd.com/circle/all-circle/20000541.htm
'''
