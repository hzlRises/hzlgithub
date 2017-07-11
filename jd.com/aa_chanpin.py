#coding:utf-8
#处理关键词特殊字符
import requests,sys,time,re
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "user-key=365feec0-21fa-42e3-850d-71625187f890; TrackID=1vRTynZ1q9GdFkuo2vZsnu85wIdZ3eUc4EfA7C0AOVwOSonNfRZXKej7bagPQj8UJwt_jWON5AzC5y-Rlg-Tz9Tl8hUg3M3c_3prKdf50h2M; ipLoc-djd=1-2809-51217-0.138636316; _pst=jd_53c836d89d9e0; unick=jd_619237350; pin=jd_53c836d89d9e0; _tp=v3jaNqGkC7JI3eyGwLdKcShMkQUtIh4HZu%2FnFibvd98%3D; unpl=V2_YDNtbUIFSkIlDEdVKxgJB2IBGwkSXkZCcglGXCgbVQJvV0EOclRCFXMUR1NnGlQUZwQZX0RcQhVFCHZXfBpaAmEBFl5yBBNNIEwEACtaDlwJARZcSlNHFHwAT1FLKV8FVwMTbUJSSxN3CE9UeRleAmIGFV5HVkUdfQB2ZHwpbDVjBxpeRFNzFEUJdhYvRVQFYAsQXw9XRh1zCkZdextcB2AGF1pBUkITfQBOZHopXw%3d%3d; cn=0; ipLocation=%u5317%u4EAC; areaId=1; sso.jd.com=78b707765db34986abd088bc2a6044e1; mt_xid=V2_52007VwMXWltaUlMfSxleAmIGFVFYWVRSF0EpXlUwURQCVA9OChYaHEAAYVFCTg5ZBlkDHU4PVW9QG1RVWgAOL0oYXAN7AhROXVlDWhxCGFoOZwMiUm1YYloeSRtaDGcFF2JeWlM%3D; sid=5f9da064a18a494945408f2dddb6f347; dmpjs=dmp-d14163054fd0e8e692416df42a70f3dcdd2bb6b; __jdv=122270672|jd.com|dmp_1528|cpc|dmp_1528_80702_d14163054fd0e8e692416df42a70f3dcdd2bb6b_1499683490|1499683491062; rkv=V0602; xtest=4624.8257.7027.cf6b6759; mx=0_X; __jda=122270672.1497318131364462407999.1497318131.1499689675.1499735099.7; __jdb=122270672.1.1497318131364462407999|7.1499735099; __jdc=122270672; __jdu=1497318131364462407999",
    "Host": "search.jd.com",
    "Referer":"https://www.jd.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",    
}

def getCountnum(kw):
	keyw = kw.split(',')[0]#只取组合后关键词
	print kw
	print keyw
	try:
		url = 'https://search.jd.com/Search?keyword=%s&enc=utf-8'%keyw
		r = requests.get(url,headers=headers)
		s = BeautifulSoup(r.content,'lxml')
		resCount = s.find('span',attrs={'id':'J_resCount'}).get_text()
		if '+' in str(resCount):
			resCount = resCount.replace('+','')
		with open('result_1.txt',r'a+') as my:#结果存放文件
			my.write(kw+','+resCount+'\n')
	except Exception,e:
		with open('fail_1.txt',r'a+') as my:#异常关键词文件
			my.write(kw+'\n')
		print e 
	
def main():
	for line in open('1.txt'):#
		kw = line.strip()
		w_str=''
		reg = re.compile(r'(\(.*?\))')
		reg2 = re.compile(r'（.*?）')
		reg3 = re.compile(r'(\(.*?）)')
		reg4 = re.compile(r'(（.*?\))')
		kw = re.sub(reg,'',kw)#两边都是英文括号
		kw = re.sub(reg2,'',kw)#两边都是中文括号
		kw = re.sub(reg3,'',kw)#左边英文，右边中文
		kw = re.sub(reg4,'',kw)#左边中文，右边英文
		kw = kw.upper()#小写变大写
		getCountnum(kw)
		time.sleep(0.5)

if __name__ == '__main__':
	main()
