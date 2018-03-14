#coding:utf-8
import requests,sys,re,pycurl,StringIO,time,xlrd,xlwt,MySQLdb
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "ww_sTitle=%E4%B9%8C%E9%BE%99%E8%8C%B6%E6%80%8E%E4%B9%88%E6%B3%A1*%E4%B9%8C%E9%BE%99%E8%8C%B6%E7%9A%84%E5%8A%9F%E6%95%88*666; CXID=6245746CC1EB9F1F4CED37FFAFFEF662; SUV=00C039A170232202593FA148825BA998; IPLOC=CN1100; ssuid=6504482916; dt_ssuid=3083555155; pgv_pvi=8396960768; SMYUV=1505188354363970; pex=C864C03270DED3DD8A06887A372DA219231FFAC25A9D64AE09E82AED12E416AC; SUID=1D73266A3765860A593F62470005663C; start_time=1511860571812; wuid=AAH0CXm+HAAAAAqZCDjHkg0AZAM=; fromwww=1; FREQUENCY=1510053108171_69; usid=qlRJs2ZSGpF-Zc9q; ad=Dkllllllll2B5LJ4lllllV$Ax77lllllzAB84yllllwllllljqxlw@@@@@@@@@@@; SNUID=8BDA8CC3AAACCDF0D33AB094AAC22A74; sct=78; sw_uuid=9892656905; sg_uuid=8896691094; ld=eyllllllll2z$269lllllV$oLyylllllzAB8wkllll9lllllRklll5@@@@@@@@@@",
    "Host": "wenwen.sogou.com",
    "Referer":"http://wenwen.sogou.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}

def main():
	conn = MySQLdb.connect('127.0.0.1','root','','tea',charset='utf8')#连接
	with conn:
		cur = conn.cursor()#让python获得执行sql的权限
		countnum = 1
		for k in open('links_sogou.txt'):
			con_str = ''
			try:
				url = k.strip().split('|')[2]
			except Exception,e:
				print e
#			print url
			try:
				r = requests.get(url,headers=headers,timeout=60)
				s = BeautifulSoup(r.content,"lxml")
				content = s.find_all('pre',attrs={'class':'replay-info-txt answer_con'})
			except Exception,e:
				print e
			try:
				if content:#回答
					for c in content:
						c = str(c.get_text().strip())
						con_str += '<p>'+c+'</p>'
						
			except Exception,e:
				print e
			try:
				sql = "insert into t_article (keywords,title,url,content) values('%s','%s','%s','%s')"%(k.strip().split('|')[0],k.strip().split('|')[1],url,con_str)
				cur.execute(sql)
				conn.commit()
			except Exception,e:
				print e
			time.sleep(0.5)
			print countnum
			countnum += 1		
			
	conn.close()#关闭
if __name__ == '__main__':
	main()
