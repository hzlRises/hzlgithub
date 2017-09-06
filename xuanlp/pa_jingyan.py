#coding:utf-8
import requests,sys,re,pycurl,StringIO,time
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "PSTM=1497341870; BIDUPSID=EF52C12648BF41D81E02C5C2456A8B31; BDUSS=c4ZHdkdjNBbFdUa3hPOVZueFFFRllrN1lNNWV3U0N6MDRkVHJ3d3BoLVdMV2RaSVFBQUFBJCQAAAAAAAAAAAEAAABh7s8nxLDErGxpZmUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJagP1mWoD9ZWT; bdshare_firstime=1497401481653; BAIDUID=9A5C9D50DFE3545AE21DCC7CF8238F0C:FG=1; __cfduid=d560c58dd04c7463850f88abfc7975fbd1500859613; MCITY=-131%3A; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a02546759411; BDSFRCVID=2d-sJeC62lSmj7TZGzrm5TQLJ2-FxjTTH6aoK2nts2txlbQzEGh1EG0PJU8g0Ku-TkjdogKK0mOTHvjP; H_BDCLCKID_SF=fR-j_KPKfIv2jJrg-tP_KnLHMfTMetJyaR0j-66bWJ5TMCoL5PjCLlDlQNLLQ5QnLmJZoDonbJ8-ShPC-x7a5pTbLnn9QPb3tRre-RvD3l02V-j9e-t2ynQDbabG54RMW20jWl7mWPQ8VKFlDjLWj63-jNRf-b-X5DOHW4T-a-OqKROvhj4KbKuyyxomtjjQLKjB_Mbu3-cKDD520fvkDCuz2M6nLUkqKCOioJr2-KoMJbRP0J6pQPvLQttjQUTPfIkja-KEQnv8eb7TyU42hf47yhjBQTT2-DA_oKKatDjP; PS_REFER=1; Hm_lvt_46c8852ae89f7d9526f0082fafa15edd=1504178805,1504607047,1504607175,1504688037; Hm_lpvt_46c8852ae89f7d9526f0082fafa15edd=1504688177; PSINO=2; H_PS_PSSID=1458_21084_17001_22072; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598",
    "Host": "jingyan.baidu.com",
    "Referer":"https://jingyan.baidu.com/search?word=%E4%B8%83%E5%A4%95%E9%80%81%E7%94%B7%E6%9C%8B%E5%8F%8B%E4%BB%80%E4%B9%88%E7%A4%BC%E7%89%A9",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}


def getHtml(k,url):#获取单页链接
	try:
		r = requests.get(url,headers=headers)
		s = BeautifulSoup(r.content,"lxml")
		ask_all = s.find_all('a')
	except Exception,e:
		print e
	try:
		for link in ask_all:
			if 'article' in link.get('href'):
				with open('links_jingyan.txt',r'a+') as my:
					#关键词、标题、详情页链接.decode('utf8')
					my.write(k+'|'+link.get_text()+'|'+'http://jingyan.baidu.com'+link.get('href')+'\n')
	except Exception,e:
		print e



def main():
	num = 0#关键词id
	for k in open('kw_jingyan.txt'):
		try:
			time.sleep(5)
			for i in range(0,5):#每个关键词请求页数
				url = 'https://jingyan.baidu.com/search?word=%s&lm=0&pn=%s'%(k.strip(),i*10)
				getHtml(k.strip(),url)
				time.sleep(1)
				
		except Exception,e:
			print e
		num += 1
		print num
if __name__ == '__main__':
	main()

	
	
