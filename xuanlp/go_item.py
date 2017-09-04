#coding:utf-8
from bs4 import BeautifulSoup

import requests,sys,time
reload(sys)
sys.setdefaultencoding('utf-8')
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "",
    "if-modified-since": "",
    "Referer": "",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
}
def main():
	num = 0
	for url in open('itemurl.txt'):
		sku_num = 0
		time.sleep(2)
		try:
			r = requests.get(url.strip(),headers=headers,timeout=30)
			s = BeautifulSoup(r.content,"lxml")
		except Exception,e:
			print e
		try:
			choose_attrs_tag = s.find('div',attrs={"id":"choose-attrs"})
			dd_tag = choose_attrs_tag.find('div',attrs={"class":"dd"})
			item_tag = dd_tag.find_all('div',attrs={"class":"item"})
		except Exception,e:
			print e
		sku_all_list = []
		try:
			for item in item_tag:
				sku = item.get('data-sku')#sku
				sku_value = item.get('data-value')#sku短描述
				sku_img = item.find('img').get('src')#图片
				
				sku_num += 1#sku数量
				sku_all = str(sku)+'|'+sku_value+'|'+sku_img
				sku_all_list.append(sku_all)
				
		except Exception,e:
			print e
		try:
			with open('re_200.txt',r'a+') as my:
				my.write(url.strip().split('/')[3].replace('.html','')+'|'+str(sku_num)+'|'+"|".join(sku_all_list)+'\n')
		except Exception,e:
			print e
		num += 1
		print num,url.strip(),sku_num
	
	
if __name__ == '__main__':
	main()
