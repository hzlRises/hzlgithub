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
    "Cookie": "ww_sTitle=%E9%80%81%E5%A5%B3%E6%9C%8B%E5%8F%8B; IPLOC=CN1100; SUV=1494858714774900; sct=3; CXID=41ACAA634EC03E664106324C546F4DED; SUID=345748DF2208990A000000005857D960; sw_uuid=4000410243; ssuid=2245000202; dt_ssuid=766539408; SNUID=1278903F51540602DA6535C951608C8D; LSTMV=557%2C73; LCLKINT=4510; cid=websearch2ww; sg_uuid=2943647500; period_s_valid=b10cbd926db9e68bc84ae4e53077ee9d; ld=tZllllllll2BAeK2lllllVuaVD1lllllbDloyZllll9llllljylll5@@@@@@@@@@; ss_cidf=1",
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
			my.write(k+'|'+str(num)+'|'+str(kw_num)+'|'+str(pageNum)+'|'+link.get_text()+'|'+'http://wenwen.sogou.com'+atag.get('href')+'\n')
		pageNum += 1



def main():
	num = 1#关键词id
	for k in open('kw_sogou.txt'):#关键词文件
		try:
			kw_num = 1#每个关键词页数
			for i in range(0,10):#每个关键词请求页数
				url = 'http://wenwen.sogou.com/s/?w=%s&st=4&pg=%s&ch=sp.pt'%(k.strip(),i)
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

