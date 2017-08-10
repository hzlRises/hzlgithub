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
    "Cookie": "test_cookie_enable=null; __huid=11fLOCYKfI7yc9K3U1Ak0lDb84Oo2kkMluRVM%2FyBBOGtU%3D; WDTKID=4de6f3776bb93bb3; __guid=9114931.3320779488070234600.1502284698135.6213; __autoShowTip=show; test_cookie_enable=null; erules=p1-64%7Cecl-14%7Cp4-61%7Cp2-5%7Cp3-10%7Cecr-1; count=24; monitor_count=24; search_last_sid=d27cebfefdd0413d4609e671011c7cf8; search_last_kw=%u9001%u5973%u670B%u53CB; smidV2=20170809211948108d549b4da606ddf3a9fc7fbcd4c122a217d54ee3b37d4a0; __gid=9114931.81433310.1502284698438.1502285322882.91; __sid=9114931.4564531316956008000.1502284698436.8765",
    "Host": "wenda.so.com",
    "Referer":"http://wenda.so.com/search/?q=%E9%80%81%E5%A5%B3%E6%9C%8B%E5%8F%8B&src=tab_www&filt=20&pn=1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": getUA(),
}


def getHtml(k,url,num,kw_num):#获取单页链接
	pageNum = 1#每页中的排名
	r = requests.get(url,headers=headers)
	s = BeautifulSoup(r.content,"lxml")
	ask_all = s.find_all('div',attrs={'class':'qa-i-hd'})
	for link in ask_all:
		atag = link.find('a')
		with open('links_360.txt',r'a+') as my:#结果保存文件
			#关键词、关键词id、页数、排名、标题、详情页链接.decode('utf8')
			my.write(k+'|'+str(num)+'|'+str(kw_num)+'|'+str(pageNum)+'|'+link.get_text()+'|'+'http://wenda.so.com'+atag.get('href')+'\n')
		pageNum += 1



def main():
	num = 1#关键词id
	for k in open('kw_360.txt'):#关键词文件
		try:
			kw_num = 1#每个关键词页数
			for i in range(0,10):#每个关键词请求页数
				url = 'http://wenda.so.com/search/?q=%s&src=tab_www&pn=%s&filt=20'%(k.strip(),i)
				getHtml(k.strip(),url,num,kw_num)
				time.sleep(1)
				kw_num += 1
				i += 1
		except Exception,e:
			print e
		num += 1
		print num
if __name__ == '__main__':
	main()

	
	
	
	
	
	
'''
def getContent(link):
	print link
	headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "BAIDUID=60C4EC61A25A4925BF326DC1939844BE:FG=1; PSTM=1494748917; BIDUPSID=B1C0B1801A9916C109EC6119661AB803; IK_CID_82=2; IK_CID_85=2; __cfduid=d84c32890f009080e7ac9ddd7f14ea19e1495369334; IK_CID_95=2; FP_UID=a989f29df4088cc692c1dcf977476a99; IK_CID_81=5; IK_CID_79=1; IK_CID_1031=10; IK_CID_83=7; IK_CID_78=1; IK_CID_80=5; IK_CID_1=13; IK_60C4EC61A25A4925BF326DC1939844BE=129; IK_CID_74=81; PSINO=2; H_PS_PSSID=1423_13550_21091_17001_20929; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1501332758,1501509384,1501765796,1502116577; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1502117404",
    "Host": "zhidao.baidu.com",
    "Referer":"https://zhidao.baidu.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
	}
	c = pycurl.Curl()
#	c.setopt(pycurl.PROXY, getRandomAlbIp())
	c.setopt(pycurl.URL, link)
	c.setopt(pycurl.FOLLOWLOCATION, True)
	c.setopt(pycurl.MAXREDIRS,5)
	c.setopt(pycurl.CONNECTTIMEOUT, 20)
	c.setopt(pycurl.TIMEOUT,60)
	c.setopt(pycurl.ENCODING, 'gzip,deflate')
	c.fp = StringIO.StringIO()
#	c.setopt(pycurl.HTTPHEADER,headers)
#	c.setopt(pycurl.POST, 1)
#	c.setopt(pycurl.POSTFIELDS, post)
	c.setopt(c.WRITEFUNCTION, c.fp.write)
	c.perform()
	html = c.fp.getvalue()
	print html
#	r_question = requests.get(link,headers=headers)
#	s_question = BeautifulSoup(r_question.content,"lxml")
#	answerContent = s_question.finf_all('span',attrs={'class':'con'})
#	print answerContent
#	for c in answerContent:
#		print c.get_text()
	
	


'''

