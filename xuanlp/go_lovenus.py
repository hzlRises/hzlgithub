#coding:utf-8
import requests,sys,time
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')


def main():
	for i in range(1,92):
		time.sleep(5)
		headers = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Encoding": "gzip, deflate, sdch",
		"Accept-Language": "zh-CN,zh;q=0.8",
		"Connection": "keep-alive",
		"Cookie": "real_ipd=116.243.92.212; ECS_ID=2acbdce1d0d33b9d3ba99285d74a7d75833799f8; ECS[visit_times]=2; LXB_REFER=www.baidu.com; ECS[display]=grid; nTalk_CACHE_DATA={uid:kf_9746_ISME9754_guest1B28BDFA-6412-1D,tid:1504332333474143}; NTKF_T2D_CLIENTID=guest1B28BDFA-6412-1D60-5CCA-C770DDF38AFC; Hm_lvt_5dd4e9f0f9f64e70ce27e21fcf3b6dce=1502289649,1504332334; Hm_lpvt_5dd4e9f0f9f64e70ce27e21fcf3b6dce=1504333915",
#		":authority": "www.lovenus.cn",
#		":method":"GET",
#		":path":"/gift/article_cat-174-%s.html"%i,
#		":scheme":"https",
		"Referer":"https://www.lovenus.cn/gift/article_cat-174-2.html",
		"Upgrade-Insecure-Requests": "1",
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
		}
		try:
			url = 'https://www.lovenus.cn/gift/article_cat-174-%s.html'%i
			r = requests.get(url,headers=headers)
			s = BeautifulSoup(r.content,"lxml")
	#		articleid = url.split('-')[1].replace('.html','')
	#		print articleid
			litag = s.find_all('li',attrs={"class":"clearfix"})
		except Exception,e:
			print e
		try:
			for li in litag:
				time.sleep(0.1)
				#文章id
				articleid = li.find('div',attrs={"class":"pic"}).find('a').get('href').split('-')[1].replace('.html','')
				print articleid
				#文章图片
				articleurl = 'https://www.lovenus.cn/gift/article-%s.html'%articleid
				imageurl = li.find('div',attrs={"class":"pic"}).find('img').get('src')
				print imageurl
				#文章标题
				articletitle = li.find('div',attrs={"class":"title"}).get_text()
				print articletitle
				#文章描述
				articledesc = li.find('div',attrs={"class":"desc"}).get_text()
				print articledesc
				#文章标签
				articletag = li.find('div',attrs={"class":"kws"}).find_all('a')
				kws_list = []
				for tag in articletag:
					tagkw = tag.get_text()
					print tagkw
					kws_list.append(tagkw)
				with open('re.txt',r'a+') as my:
					my.write(str(articleid)+'|'+str(articleurl)+'|'+str(imageurl)+'|'+str(articletitle)+'|'+str(articledesc)+'|'+",".join(kws_list)+'\n')
		except Exception,e:
			print e
			
if __name__ == '__main__':
	main()
	
