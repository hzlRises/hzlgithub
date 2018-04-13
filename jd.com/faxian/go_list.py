#coding:utf-8
import	HeaderData,re
import requests,time
from bs4 import BeautifulSoup
file_name = 'jrhelp.jd.com_index'

def main():	
	f = open('%s_detail_url.txt'%file_name,r'a+')
	'''
	4生活
	6数码
	8亲子
	9风尚
	19美食
	23手机
	24女神
	25型男
	26运动
	27汽车
	28家居
	29家电
	30休闲	
	'''	
	for t in [4,6,8,9,19,23,24,25,26,27,28,29,30]:
		for i in range(1,100):#爬取			
			url = 'https://ai.jd.com/index_new.php?app=Discovergoods&action=getRecommendList&callback=listCallback&page=%s&style=&type=%s&des=DiscRecommend'%(i,t)
			content_url_list = []		
			#try:
			r = requests.get(url,headers=HeaderData.get_header(),timeout=60)				
			id = re.findall(r'"articleId":(\d+),',r.content)			
			#except Exception,e:
			#	print e
			if id:
				for artId in id:
					f.write(str(artId)+'\n')
			print t,i,len(id)

			
		
	f.close()



if __name__ == '__main__':
	main()
