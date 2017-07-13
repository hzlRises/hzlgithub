#coding:utf-8
#处理关键词特殊字符
import requests,sys,time,re
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
author = 'TSBC'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "__jda=122270672.1496654831191591020064.1496654831.1499329155.1499908086.30; __jdu=1496654831191591020064; ipLoc-djd=1-72-4137-0; areaId=1; __jdv=122270672|baidu|-|organic|not set|1498616240066; xtest=2217.8731.604.cf6b6759; mx=0_X; ipLocation=%u5317%u4EAC; __jdb=122270672.2.1496654831191591020064|30.1499908086; __jdc=122270672; rkv=V0000",
    "Host": "search.jd.com",
	"Referer":"https://www.jd.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
}
successNUm = 0
failNum = 0
def getCountnum(kw):
	global successNUm
	global failNum
	keyw = kw.split(',')[0]#只取组合后关键词
	try:
		url = 'https://search.jd.com/Search?keyword=%s&enc=utf-8'%keyw
		r = requests.get(url,headers=headers)
		s = BeautifulSoup(r.content,'lxml')
		resCount = s.find('span',attrs={'id':'J_resCount'}).get_text()
		if '+' in str(resCount):
			resCount = resCount.replace('+','')
		with open('result_2.txt',r'a+') as my:#结果存放文件
			my.write(kw+','+resCount+'\n')
		successNUm += 1
	except Exception,e:
		with open('fail_2.txt',r'a+') as my:#异常关键词文件
			my.write(kw+'\n')
		failNum += 1
		print e 
	print 'successNUm,failNum:'+successNUm+','+failNum
	
def main():
	for line in open('2.txt'):#
		kw = line.strip()
		reg = re.compile(r'(\(.*?\))')
		reg2 = re.compile(r'（.*?）')
		reg3 = re.compile(r'(\(.*?）)')
		reg4 = re.compile(r'(（.*?\))')
		reg5 = re.compile(r'\&')
		kw = re.sub(reg,'',kw)#两边都是英文括号
		kw = re.sub(reg2,'',kw)#两边都是中文括号
		kw = re.sub(reg3,'',kw)#左边英文，右边中文
		kw = re.sub(reg4,'',kw)#左边中文，右边英文
		kw = re.sub(reg5,'',kw)#&符号
		kw = kw.upper()#小写变大写
		getCountnum(kw)
		time.sleep(0.1)

if __name__ == '__main__':
	main()
