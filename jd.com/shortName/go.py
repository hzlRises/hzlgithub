#coding:utf-8
import requests,json,sys,time,re
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')



def get_page_count(catid):
	try:
		url = 'https://list.jd.com/list.html?cat=%s'%catid
		r = requests.get(url)
		s = BeautifulSoup(r.content,"lxml")
		page_num = s.find('span',attrs={"class":"p-skip"}).find('b').get_text()	
		if page_num:
			return int(page_num)
		else:
			return 1
	except Exception,e:
		print e



	
def get_skuid_list(catid,page_count):
	f_sku = open('%s_sku.txt'%catid,r'a+')
	headers_list = {	
		"authority":"list.jd.com",
		"method":"GET",
		"path":"/list.html?cat=%s"%catid,
		"scheme":"https",		
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"accept-encoding": "gzip, deflate, sdch",
		"accept-language": "zh-CN,zh;q=0.8",
		"cache-control":"no-cache",
		"Connection": "keep-alive",
		"Cookie":'''_pst=jd_53c836d89d9e0; unick=jd_619237350; _tp=v3jaNqGkC7JI3eyGwLdKcShMkQUtIh4HZu%2FnFibvd98%3D; TrackID=1dviQbWV6fLjUaiQizqbPMPwDP3y53vyu83iDt---YttiZXiFUm-bvF5Hq7m8HGgzSo8vfubNW7DUkW9gVGcuyw; npin=jd_53c836d89d9e0; webp=1; visitkey=10958189661304086; shshshfpb=0b85bae258668a37d8a91d6827a2848cb92e6844470d9dfe259faf9a61; shshshfpa=af6cd036-c183-c03e-aabf-0893a7477a2e-1516775001; mba_muid=1497318131364462407999; __tru=ba4888a1-5ad4-4fb2-a1a4-0318a4dc619d; __tra=122270672.15169311067501171870213.1516931107.1516931107.1516931142.1; logintype=qq; pin=jd_53c836d89d9e0; _AIRLINE_VALUE_="z8PDxSyxsb6pLDIwMTgtMDQtMDgsMSxPVw=="; query_history=%5B%7B%22arrCity%22%3A%22%E6%B3%89%E5%B7%9E%22%2C%22arrDate%22%3A%222018-04-05%22%2C%22depCity%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22depDate%22%3A%222018-04-05%22%2C%22lineType%22%3A%22OW%22%2C%22price%22%3A%22501%22%2C%22queryTime%22%3A%222018-03-28+12%3A34%3A41%22%2C%22userPin%22%3A%22jd_53c836d89d9e0%22%7D%2C%7B%22arrCity%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22arrDate%22%3A%222018-04-08%22%2C%22depCity%22%3A%22%E5%8E%A6%E9%97%A8%22%2C%22depDate%22%3A%222018-04-08%22%2C%22lineType%22%3A%22OW%22%2C%22price%22%3A%221191%22%2C%22queryTime%22%3A%222018-03-28+12%3A20%3A50%22%2C%22userPin%22%3A%22jd_53c836d89d9e0%22%7D%2C%7B%22arrCity%22%3A%22%E5%8E%A6%E9%97%A8%22%2C%22arrDate%22%3A%222018-04-05%22%2C%22depCity%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22depDate%22%3A%222018-04-05%22%2C%22lineType%22%3A%22OW%22%2C%22price%22%3A%22704%22%2C%22queryTime%22%3A%222018-03-28+12%3A19%3A35%22%2C%22userPin%22%3A%22jd_53c836d89d9e0%22%7D%2C%7B%22arrCity%22%3A%22%E5%8E%A6%E9%97%A8%22%2C%22arrDate%22%3A%222018-04-08%22%2C%22depCity%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22depDate%22%3A%222018-04-04%22%2C%22lineType%22%3A%22RT%22%2C%22price%22%3A%221112%22%2C%22queryTime%22%3A%222018-03-15+17%3A28%3A48%22%2C%22userPin%22%3A%22jd_53c836d89d9e0%22%7D%2C%7B%22arrCity%22%3A%22%E5%8E%A6%E9%97%A8%22%2C%22arrDate%22%3A%222018-04-08%22%2C%22depCity%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22depDate%22%3A%222018-04-04%22%2C%22lineType%22%3A%22RT%22%2C%22price%22%3A%221112%22%2C%22queryTime%22%3A%222018-03-15+17%3A06%3A30%22%2C%22userPin%22%3A%22jd_53c836d89d9e0%22%7D%5D; intlIpLbsCountrySite=jd; cid=9; intlIpLbsCountryIp=111.202.148.58; TrackerID=jQjgcdfkdXBpbJb8rns7ka9OwIYv5knB-n3bEx693zLFj59EL78FWdcy095h-KTqedZQdtn8_5mw1I_TWrWrUZhWZMt8Nb-5CogvTz2lB7tP93Y_UtA3PbgLA6O9SIJ__CNUDf3NuH4grnEMlbHtAw; pt_key=AAFa0BSpADA8i6v-BisMFWOSEsgXSvbGKrgsV2HsgB5Dc5uLf4QaK9K6AUyFY2oJ70Nr2xcPWb8; pt_pin=jd_53c836d89d9e0; pt_token=80c83i7c; pwdt_id=jd_53c836d89d9e0; sc_width=375; wq_ufc=5cd489527e6f4cc9c2d5ad1549d4a929; mainSkuCount=1; cartNum=1; kplTitleShow=1; wq_logid=1524566273_1804289383; jdAddrId=1_2810_51081_0; jdAddrName=%u5317%u4EAC_%u5927%u5174%u533A_%u4EA6%u5E84%u7ECF%u6D4E%u5F00%u53D1%u533A_; addrId_1=138453223; addrType_1=1; wq_addr=138453223%7C1_2810_51081_0%7C%u5317%u4EAC_%u5927%u5174%u533A_%u4EA6%u5E84%u7ECF%u6D4E%u5F00%u53D1%u533A_%7C%u5317%u4EAC%u5927%u5174%u533A%u4EA6%u5E84%u7ECF%u6D4E%u5F00%u53D1%u533A%u4EAC%u4E1C%u96C6%u56E2%u603B%u90E8-%u79D1%u521B%u5341%u4E00%u885718%u53F7%u9662B%u5EA713%u5C42%7C116.56342%2C39.7869; mitemAddrId=1_2810_51081_0; mitemAddrName=%u5317%u4EAC%u5927%u5174%u533A%u4EA6%u5E84%u7ECF%u6D4E%u5F00%u53D1%u533A%u4EAC%u4E1C%u96C6%u56E2%u603B%u90E8-%u79D1%u521B%u5341%u4E00%u885718%u53F7%u9662B%u5EA713%u5C42; cn=0; retina=1; __wga=1524566414513.1524566219149.1523586225098.1516774999596.10.7; user-key=c6d3b35c-6303-4ce4-ae20-3a0c62924542; PCSYCityID=1; mobilev=html5; unpl=V2_ZzNtbRAAQhJ1XRRUeh1aV2ILGglKBRYXJl8VVC4dXVJjBxpdclRCFXwUR1BnGF4UZwIZWUpcQxRFCEJkexhdBGcBF1hAUnMlRQtGZHwYbAViCxRfQl5DF3UKQVF%2bHl8AZgUaVUpncxx0OHZUch9VA2cLGlleUkQVdwlDZHopXTVmM1kzQxpDEH0ORFRyGV4FZQQXWEVURhRzAE5cSx1UA2QDF21B; shshshfp=7b80ddf52c74d0bcb24a6e6ec35b624e; areaId=1; ipLoc-djd=1-2809-51217-0; ipLocation=%u5317%u4EAC; mt_xid=V2_52007VwMXWltaUlMfSxleAmIGFVFYWVRSF0EpWwJiBRBVCFpOWUgdHEAAYlYVTg5ZVV8DGx8MA2AHElEIDAJaL0oYXAx7AhZOXF5DWhZCHVkOZgoiUm1YYl8bQRBYB1cBFlNf; dmpjs=dmp-d3079847ae3e2541f8604521993c59c723b7a49; _jrda=108; wlfstk_smdl=edbbbyqm5ctnysq59a77qbfu328ai21x; pinId=qs7eO3zat2CJ-45-Bvmd6bV9-x-f3wj7; 3AB9D23F7A4B3C9B=SRFBEFEUQOW6A6HQK43UV4IIDN2F3ZNPV2LWJPBJJWDCACNBBMNYPY7ZYPLYE43ZEQGT7BO74O3V3VOUNSDW3C5KPI; erp1.jd.com=BD79457848F94AAB1C79963B41FA577B9BFA9401A5E4F9732BF1034DCAB1A3949F550FECD04FE915FB58A30B1D1EA23EA3EC2B3EDED0C89EC7DC77A81E09990E4DBF8844F254146AD466B9A4E9DD1A24; sso.jd.com=1838192095264c4d8599eb9fb91b0f93; __jdv=122270672|baidu|-|organic|not set|1525746437750; _rdCube=%7B%22p1009484%22%3A%22%2C7109904%22%7D; __tak=0c5187d2d5f791e99193cf969e42aae539b52ade99dcfa382b087c30ed36f6bf5c8e60496bded4217c84ed34dfd1d7e33f87210eccd36f80aa483c1bea33542dec80858c5171b011810462e047cd1512; __jdc=122270672; __jda=122270672.1497318131364462407999.1497318131.1525749044.1525759777.379; listck=6189b18e8cf9de74cc2ae96aeafc9567; book_city_code=200; book_city_name=%E5%8C%97%E4%BA%AC; book_city_custom=bj; tuniuuser_citycode=MjAw; __jdu=1497318131364462407999; list_sa=FALSE; __jdb=122270672.132.1497318131364462407999|379.1525759777; thor=CACC4FECD01D35074CAC503AF6E9FFDDF62B3122E6F200D4C446D0DEB91B382B2D1E3293134D4D41B45E9D569E41720721DA22C0051B4938BFA58EAE45CA72CC26252D7AC8B5C2782781E5A61C0CD3A28313D07995F5D604F29A59CE5A390E5094D7D6D146486119F8324111E9A9627BB9444966DDF542C497858D2C3C854C25245A27F72A7FBC84B1436D42BF0D8C1C59E3DD454367CD0310156078AD952BC4''',
		"pragma": "no-cache",
		"Upgrade-Insecure-Requests": "1",
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
	}	
	skuid_list = []
	for i in range(1,page_count+1):
		try:
			url = 'https://list.jd.com/list.html?cat=%s&page=%s&sort=sort_commentcount_desc&trans=1&JL=4_5_0#J_main'%(catid,i)
			r = requests.get(url,headers=headers_list,timeout=60)
			s = BeautifulSoup(r.content,"lxml")
			p_img = s.find_all('div',attrs={"class":"p-img"})			
		except Exception,e:
			print e 
		try:
			for p in p_img:
				atag = p.find('a').get('href')
				atag_str = re.search(r'\d+',atag)
				skuid = atag_str.group(0)
				
				f_sku.write(skuid+'\n')
				print catid+','+str(page_count)+','+str(i)+';'+'writed:'+skuid
				skuid_list.append(skuid)
		except Exception,e:
			print e
	f_sku.close()
	return skuid_list



	
def get_short_name(catid,skuid_list):
	f = open('%s_sku_shorName.txt'%catid,r'a+')
	headers_question = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Encoding": "gzip, deflate, sdch",
		"Accept-Language": "zh-CN,zh;q=0.8",
		"Cache-Control":"no-cache",
		"Connection": "keep-alive",
		"Cookie":'''_pst=jd_53c836d89d9e0; unick=jd_619237350; _tp=v3jaNqGkC7JI3eyGwLdKcShMkQUtIh4HZu%2FnFibvd98%3D; TrackID=1dviQbWV6fLjUaiQizqbPMPwDP3y53vyu83iDt---YttiZXiFUm-bvF5Hq7m8HGgzSo8vfubNW7DUkW9gVGcuyw; npin=jd_53c836d89d9e0; webp=1; visitkey=10958189661304086; shshshfpb=0b85bae258668a37d8a91d6827a2848cb92e6844470d9dfe259faf9a61; shshshfpa=af6cd036-c183-c03e-aabf-0893a7477a2e-1516775001; mba_muid=1497318131364462407999; __tru=ba4888a1-5ad4-4fb2-a1a4-0318a4dc619d; __tra=122270672.15169311067501171870213.1516931107.1516931107.1516931142.1; logintype=qq; pin=jd_53c836d89d9e0; _AIRLINE_VALUE_="z8PDxSyxsb6pLDIwMTgtMDQtMDgsMSxPVw=="; query_history=%5B%7B%22arrCity%22%3A%22%E6%B3%89%E5%B7%9E%22%2C%22arrDate%22%3A%222018-04-05%22%2C%22depCity%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22depDate%22%3A%222018-04-05%22%2C%22lineType%22%3A%22OW%22%2C%22price%22%3A%22501%22%2C%22queryTime%22%3A%222018-03-28+12%3A34%3A41%22%2C%22userPin%22%3A%22jd_53c836d89d9e0%22%7D%2C%7B%22arrCity%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22arrDate%22%3A%222018-04-08%22%2C%22depCity%22%3A%22%E5%8E%A6%E9%97%A8%22%2C%22depDate%22%3A%222018-04-08%22%2C%22lineType%22%3A%22OW%22%2C%22price%22%3A%221191%22%2C%22queryTime%22%3A%222018-03-28+12%3A20%3A50%22%2C%22userPin%22%3A%22jd_53c836d89d9e0%22%7D%2C%7B%22arrCity%22%3A%22%E5%8E%A6%E9%97%A8%22%2C%22arrDate%22%3A%222018-04-05%22%2C%22depCity%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22depDate%22%3A%222018-04-05%22%2C%22lineType%22%3A%22OW%22%2C%22price%22%3A%22704%22%2C%22queryTime%22%3A%222018-03-28+12%3A19%3A35%22%2C%22userPin%22%3A%22jd_53c836d89d9e0%22%7D%2C%7B%22arrCity%22%3A%22%E5%8E%A6%E9%97%A8%22%2C%22arrDate%22%3A%222018-04-08%22%2C%22depCity%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22depDate%22%3A%222018-04-04%22%2C%22lineType%22%3A%22RT%22%2C%22price%22%3A%221112%22%2C%22queryTime%22%3A%222018-03-15+17%3A28%3A48%22%2C%22userPin%22%3A%22jd_53c836d89d9e0%22%7D%2C%7B%22arrCity%22%3A%22%E5%8E%A6%E9%97%A8%22%2C%22arrDate%22%3A%222018-04-08%22%2C%22depCity%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22depDate%22%3A%222018-04-04%22%2C%22lineType%22%3A%22RT%22%2C%22price%22%3A%221112%22%2C%22queryTime%22%3A%222018-03-15+17%3A06%3A30%22%2C%22userPin%22%3A%22jd_53c836d89d9e0%22%7D%5D; intlIpLbsCountrySite=jd; cid=9; intlIpLbsCountryIp=111.202.148.58; TrackerID=jQjgcdfkdXBpbJb8rns7ka9OwIYv5knB-n3bEx693zLFj59EL78FWdcy095h-KTqedZQdtn8_5mw1I_TWrWrUZhWZMt8Nb-5CogvTz2lB7tP93Y_UtA3PbgLA6O9SIJ__CNUDf3NuH4grnEMlbHtAw; pt_key=AAFa0BSpADA8i6v-BisMFWOSEsgXSvbGKrgsV2HsgB5Dc5uLf4QaK9K6AUyFY2oJ70Nr2xcPWb8; pt_pin=jd_53c836d89d9e0; pt_token=80c83i7c; pwdt_id=jd_53c836d89d9e0; sc_width=375; wq_ufc=5cd489527e6f4cc9c2d5ad1549d4a929; mainSkuCount=1; cartNum=1; kplTitleShow=1; wq_logid=1524566273_1804289383; jdAddrId=1_2810_51081_0; jdAddrName=%u5317%u4EAC_%u5927%u5174%u533A_%u4EA6%u5E84%u7ECF%u6D4E%u5F00%u53D1%u533A_; addrId_1=138453223; addrType_1=1; wq_addr=138453223%7C1_2810_51081_0%7C%u5317%u4EAC_%u5927%u5174%u533A_%u4EA6%u5E84%u7ECF%u6D4E%u5F00%u53D1%u533A_%7C%u5317%u4EAC%u5927%u5174%u533A%u4EA6%u5E84%u7ECF%u6D4E%u5F00%u53D1%u533A%u4EAC%u4E1C%u96C6%u56E2%u603B%u90E8-%u79D1%u521B%u5341%u4E00%u885718%u53F7%u9662B%u5EA713%u5C42%7C116.56342%2C39.7869; mitemAddrId=1_2810_51081_0; mitemAddrName=%u5317%u4EAC%u5927%u5174%u533A%u4EA6%u5E84%u7ECF%u6D4E%u5F00%u53D1%u533A%u4EAC%u4E1C%u96C6%u56E2%u603B%u90E8-%u79D1%u521B%u5341%u4E00%u885718%u53F7%u9662B%u5EA713%u5C42; cn=0; retina=1; __wga=1524566414513.1524566219149.1523586225098.1516774999596.10.7; user-key=c6d3b35c-6303-4ce4-ae20-3a0c62924542; PCSYCityID=1; mobilev=html5; unpl=V2_ZzNtbRAAQhJ1XRRUeh1aV2ILGglKBRYXJl8VVC4dXVJjBxpdclRCFXwUR1BnGF4UZwIZWUpcQxRFCEJkexhdBGcBF1hAUnMlRQtGZHwYbAViCxRfQl5DF3UKQVF%2bHl8AZgUaVUpncxx0OHZUch9VA2cLGlleUkQVdwlDZHopXTVmM1kzQxpDEH0ORFRyGV4FZQQXWEVURhRzAE5cSx1UA2QDF21B; shshshfp=7b80ddf52c74d0bcb24a6e6ec35b624e; areaId=1; ipLoc-djd=1-2809-51217-0; ipLocation=%u5317%u4EAC; mt_xid=V2_52007VwMXWltaUlMfSxleAmIGFVFYWVRSF0EpWwJiBRBVCFpOWUgdHEAAYlYVTg5ZVV8DGx8MA2AHElEIDAJaL0oYXAx7AhZOXF5DWhZCHVkOZgoiUm1YYl8bQRBYB1cBFlNf; dmpjs=dmp-d3079847ae3e2541f8604521993c59c723b7a49; _jrda=108; wlfstk_smdl=edbbbyqm5ctnysq59a77qbfu328ai21x; pinId=qs7eO3zat2CJ-45-Bvmd6bV9-x-f3wj7; 3AB9D23F7A4B3C9B=SRFBEFEUQOW6A6HQK43UV4IIDN2F3ZNPV2LWJPBJJWDCACNBBMNYPY7ZYPLYE43ZEQGT7BO74O3V3VOUNSDW3C5KPI; erp1.jd.com=BD79457848F94AAB1C79963B41FA577B9BFA9401A5E4F9732BF1034DCAB1A3949F550FECD04FE915FB58A30B1D1EA23EA3EC2B3EDED0C89EC7DC77A81E09990E4DBF8844F254146AD466B9A4E9DD1A24; sso.jd.com=1838192095264c4d8599eb9fb91b0f93; __jdv=122270672|baidu|-|organic|not set|1525746437750; _rdCube=%7B%22p1009484%22%3A%22%2C7109904%22%7D; __tak=0c5187d2d5f791e99193cf969e42aae539b52ade99dcfa382b087c30ed36f6bf5c8e60496bded4217c84ed34dfd1d7e33f87210eccd36f80aa483c1bea33542dec80858c5171b011810462e047cd1512; __jdc=122270672; __jda=122270672.1497318131364462407999.1497318131.1525749044.1525759777.379; book_city_code=200; book_city_name=%E5%8C%97%E4%BA%AC; book_city_custom=bj; tuniuuser_citycode=MjAw; __jdu=1497318131364462407999; thor=CACC4FECD01D35074CAC503AF6E9FFDDF62B3122E6F200D4C446D0DEB91B382B2D1E3293134D4D41B45E9D569E41720721DA22C0051B4938BFA58EAE45CA72CC26252D7AC8B5C2782781E5A61C0CD3A28313D07995F5D604F29A59CE5A390E5094D7D6D146486119F8324111E9A9627BB9444966DDF542C497858D2C3C854C25245A27F72A7FBC84B1436D42BF0D8C1C59E3DD454367CD0310156078AD952BC4; __jdb=122270672.133.1497318131364462407999|379.1525759777''',
		"Host": "question.jd.com",
		"Pragma": "no-cache",
		"Upgrade-Insecure-Requests": "1",
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
	}
	try:
		for k,id in enumerate(skuid_list):
			url = 'getQuestionAnswerList.action?page=1&productId=%s'%id
			r = requests.get(url,headers=headers_question,timeout=60)
			j_data = json.loads(r.content)
			shortName = j_data["skuInfo"]["shortName"]
			brandId = j_data["skuInfo"]["brandId"]
			brandName = j_data["skuInfo"]["brandName"]			
			f.write(id+'||'+shortName+'||'+str(brandId)+'||'+brandName+'\n')
			print catid+','+str(len(skuid_list))+','+str(k)
	except Exception,e:
		print e
	f.close()
	
def main():
	for line in open('cat_id.txt'):
		global catid	
		catid = line.strip()
		
		f_id = line.strip().split(',')[0]
		s_id = line.strip().split(',')[1]
		t_id = line.strip().split(',')[2]		
		#获取每个三级类目有多少页
		page_count = get_page_count(catid)	
		
		
		#获取每个三级类目下的sku返回list		
		skuid_list = get_skuid_list(catid,page_count)
		
		
		#获取每个sku的短标题		
		get_short_name(catid,skuid_list)
		
		break

if __name__ == '__main__':
	main()

	


	
	
'''
https://list.jd.com/list.html?cat=1319,1527,1559&page=1&sort=sort_commentcount_desc&trans=1&JL=4_5_0#J_main

'''
