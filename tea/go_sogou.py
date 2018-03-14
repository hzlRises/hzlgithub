#coding:utf-8
import requests,sys,re,pycurl,StringIO,time,random
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')


def getUA():
	uaList = [
		'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1;+.NET+CLR+1.1.4322;+TencentTraveler)',
		'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1;+.NET+CLR+2.0.50727;+.NET+CLR+3.0.4506.2152;+.NET+CLR+3.5.30729)',
		'Mozilla/5.0+(Windows+NT+5.1)+AppleWebKit/537.1+(KHTML,+like+Gecko)+Chrome/21.0.1180.89+Safari/537.1',
		'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1)',
		'Mozilla/5.0+(Windows+NT+6.1;+rv:11.0)+Gecko/20100101+Firefox/11.0',
		'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+SV1)',
		'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+GTB7.1;+.NET+CLR+2.0.50727)',
		'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+KB974489)',
		'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
		'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
		"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
		"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	]
	newUa = random.choice(uaList) 
	return newUa


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "ww_sTitle=%E4%B9%8C%E9%BE%99%E8%8C%B6%E6%80%8E%E4%B9%88%E6%B3%A1*%E4%B9%8C%E9%BE%99%E8%8C%B6%E7%9A%84%E5%8A%9F%E6%95%88*666; CXID=6245746CC1EB9F1F4CED37FFAFFEF662; SUV=00C039A170232202593FA148825BA998; IPLOC=CN1100; ssuid=6504482916; dt_ssuid=3083555155; pgv_pvi=8396960768; SMYUV=1505188354363970; pex=C864C03270DED3DD8A06887A372DA219231FFAC25A9D64AE09E82AED12E416AC; SUID=1D73266A3765860A593F62470005663C; start_time=1511860571812; wuid=AAH0CXm+HAAAAAqZCDjHkg0AZAM=; fromwww=1; FREQUENCY=1510053108171_69; usid=qlRJs2ZSGpF-Zc9q; ad=Dkllllllll2B5LJ4lllllV$Ax77lllllzAB84yllllwllllljqxlw@@@@@@@@@@@; SNUID=8BDA8CC3AAACCDF0D33AB094AAC22A74; sct=78; sw_uuid=9892656905; sg_uuid=8896691094; ld=eyllllllll2z$269lllllV$oLyylllllzAB8wkllll9lllllRklll5@@@@@@@@@@",
    "Host": "wenwen.sogou.com",
    "Referer":"http://wenwen.sogou.com/s/?w=%E9%80%81%E5%A5%B3%E6%9C%8B%E5%8F%8B&st=4&pg=2&ch=sp.pt",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}


def getHtml(k,url,num,kw_num):#获取单页链接
	pageNum = 1#每页中的排名
	r = requests.get(url,headers=headers)
	s = BeautifulSoup(r.content,"lxml")
	ask_all = s.find_all('h3',attrs={'class':'result-title sIt_title'})
	for link in ask_all:
		atag = link.find('a')
		with open('links_sogou.txt',r'a+') as my:#结果保存文件
			#关键词、关键词id、页数、排名、标题、详情页链接.decode('utf8')
			#my.write(k+'|'+str(num)+'|'+str(kw_num)+'|'+str(pageNum)+'|'+link.get_text()+'|'+'http://wenwen.sogou.com'+atag.get('href')+'\n')
			my.write(k+'|'+link.get_text()+'|'+'http://wenwen.sogou.com'+atag.get('href')+'\n')
		pageNum += 1



def main():
	num = 1#关键词id
	for k in open('kw_sogou.txt'):#关键词文件
		time.sleep(0.5)
		try:
			kw_num = 1#每个关键词页数
			for i in range(0,1):#每个关键词请求页数
				url = 'http://wenwen.sogou.com/s/?w=%s&st=4&pg=%s&ch=sp.pt'%(k.strip(),i)
				getHtml(k.strip(),url,num,kw_num)
				time.sleep(1)
				kw_num += 1
				i += 1
		except Exception,e:
			print e
		print num
		num += 1
		
if __name__ == '__main__':
	main()

	
	
	
