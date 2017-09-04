#coding:utf-8
from bs4 import BeautifulSoup

import requests,sys
reload(sys)
sys.setdefaultencoding('utf-8')
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "user-key=e3d00dbc-c8fa-42b6-96e7-e932379e7366; TrackID=1WNjCq0T_OBs_k1l2BLZlcN-8zExv4rSd-h3rSJbWo1c8occcD2ZuWsozGWjWZbosQU_NI3_Mfhq4ooBgQRvJ1A; cn=0; ipLocation=%u5317%u4EAC; dmpjs=dmp-d6534753c911d79a26901ce79dd1af7fd6da353; unpl=V2_YDNtbRJURxd1W0VRKxtUBmIBRVVLBxcWdAkWXSsaCVZjBkUIclRCFXMUR1xnGFwUZwsZX0RcQxxFCHZXfBpaAmEBFl5yBBNNIEwEACtaDlwvR00zRVFGFnUPQVR6EVo1VwASbUJWcxVwAEBWexBcB2cBFVhHUEAQdA5OXHMpbAJXMyJZRFBKEHM4R2R6KR5ROwMSX0RQDhVwAEBWexBcB2cBFVhHUEAQdA5OXHMpXTVk; _pst=jd_53c836d89d9e0; unick=jd_619237350; pin=jd_53c836d89d9e0; _tp=v3jaNqGkC7JI3eyGwLdKcShMkQUtIh4HZu%2FnFibvd98%3D; pinId=qs7eO3zat2CJ-45-Bvmd6bV9-x-f3wj7; sso.jd.com=030d5ae451fc441da4e09bf99fc9a881; areaId=1; ipLoc-djd=1-2810-4205-0; __jdv=122270672|baidu|-|organic|not set|1504508100622; sid=1fde83069478c42a920d7c693ee4b201; mt_xid=V2_52007VwMXWltaUlMfSxleAmIGFVFYWVRSF0EpCwU1BhIGX1xODhsZGkAAYQMQTg0LWg8DSRlbAzJTRVJUXABTL0oYXAN7AhpOXF1DWhlCG1kOYwUiUG1YYlocShpZA24GEmJdXVRd; _jrda=1; _jrdb=1504519929530; 3AB9D23F7A4B3C9B=SRFBEFEUQOW6A6HQK43UV4IIDN2F3ZNPV2LWJPBJJWDCACNBBMNYPY7ZYPLYE43ZEQGT7BO74O3V3VOUNSDW3C5KPI; __jda=122270672.1497318131364462407999.1497318131.1503489072.1504076573.11; __jdb=122270672.93.1497318131364462407999|11.1504076573; __jdc=122270672; thor=C5767BD8F390A60672C6BCD5C50F151B3080BAE2E8500D26EEF494DD6085C174A2D6A58C330DEC8DB1EC3DEBC4D3674CB7E9D6E55EA1F3585B34B2CBD9537860AC495FEF372BB6ECD10E52207B2A78D9613A3E89759AC135E9AE1A79391ED9E285B3FF61C4DB65771AB7030151C87593A742F673E141BAF8AF7ECDD8593F94CEFFE62218BE142869932D92305D6FC9DBD0D8BC3781853B7E79C3692F81F69D26; __jdu=1497318131364462407999",
    "if-modified-since": "Mon, 04 Sep 2017 10:36:40 GMT",
    "Referer": "https://search.jd.com/Search?keyword=%E7%A4%BC%E7%89%A9&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=4&page=9&s=241&click=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
}
def main():
	sku_num = 0
	for url in open('itemurl.txt'):
		r = requests.get(url.strip(),headers=headers)
		s = BeautifulSoup(r.content,"lxml")
		choose_attrs_tag = s.find('div',attrs={"id":"choose-attrs"})
		dd_tag = choose_attrs_tag.find('div',attrs={"class":"dd"})
		item_tag = dd_tag.find_all('div',attrs={"class":"item"})

		sku_all_list = []
		for item in item_tag:
			sku = item.get('data-sku')#sku
			
			
			sku_value = item.get('data-value')#sku短描述
			
			
			sku_img = item.find('img').get('src')#图片
			
			
			print sku,sku_value,sku_img
			sku_num += 1#sku数量
			sku_all = str(sku)+'|'+sku_value+'|'+sku_img
			sku_all_list.append(sku_all)
			
		with open('re_200.txt',r'a+') as my:
			my.write(url.strip().split('/')[3].replace('.html','')+'|'+str(sku_num)+'|'+"|".join(sku_all_list)+'\n')
			
			
	print sku_num
	
	
if __name__ == '__main__':
	main()
