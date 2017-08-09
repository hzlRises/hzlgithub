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
    "Cookie": "BAIDUID=60C4EC61A25A4925BF326DC1939844BE:FG=1; PSTM=1494748917; BIDUPSID=B1C0B1801A9916C109EC6119661AB803; bdshare_firstime=1494775741101; __cfduid=d84c32890f009080e7ac9ddd7f14ea19e1495369334; BDSFRCVID=TFKsJeCAa4jaOuJZiI0ZKwtqQ2KK0gOTH6KFE3GqpqS7ivCVtVSMjXLZtx8g0Kubasm7ogKK0gOTH65P; H_BDCLCKID_SF=tJADoIIMtC-3JRnYb-Qoq4D_MfOtetJyaR3nKqvbWJ5TEJDmM4Qc5fIlMtujXfnfbT6Ioqvctn3cShPCyUjpDU-LKhQgt-cq0acJ-fOz2fndo4b9e-t2ynLV-qbLt-RMW20j0h7mWILhVKcnK4-Xjjb3eHQP; PS_REFER=1; PSINO=2; H_PS_PSSID=1423_13550_21091_17001_20929; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_46c8852ae89f7d9526f0082fafa15edd=1500811702,1500902946,1502116714,1502290447; Hm_lpvt_46c8852ae89f7d9526f0082fafa15edd=1502290810",
    "Host": "jingyan.baidu.com",
    "Referer":"https://jingyan.baidu.com/search?word=%E4%B8%83%E5%A4%95%E9%80%81%E7%94%B7%E6%9C%8B%E5%8F%8B%E4%BB%80%E4%B9%88%E7%A4%BC%E7%89%A9",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}


def getHtml(k,url,num,kw_num):#获取单页链接
	pageNum = 1#每页中的排名
	r = requests.get(url,headers=headers)
	s = BeautifulSoup(r.content,"lxml")
	ask_all = s.find_all('a')
	
	for link in ask_all:
		if 'article' in link.get('href'):
			with open('links_jingyan.txt',r'a+') as my:
				#关键词、关键词id、页数、排名、标题、详情页链接.decode('utf8')
				my.write(k+'|'+str(num)+'|'+str(kw_num)+'|'+str(pageNum)+'|'+link.get_text()+'|'+'http://jingyan.baidu.com'+link.get('href')+'\n')
			pageNum += 1



def main():
	num = 1#关键词id
	for k in open('kw_jingyan.txt'):
		try:
			kw_num = 1#每个关键词页数
			for i in range(0,10):#每个关键词请求页数
				url = 'https://jingyan.baidu.com/search?word=%s&lm=0&pn=%s'%(k.strip(),i*10)
				getHtml(k.strip(),url,num,kw_num)
				time.sleep(1)
				kw_num += 1
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

