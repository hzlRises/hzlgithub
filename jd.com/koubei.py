#coding:utf-8
author = 'heziliang'
import socket,threading,random,requests,pycurl
from multiprocessing.dummy import Pool as ThreadPool
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
socket.setdefaulttimeout(6)
#以上，引用必需的模块

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
	"Cache-Control":"max-age=0",
    "Connection": "keep-alive",
	"Cookie":'',
    "Host": "club.jd.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
}




fuu_list = []
totalThread = 10
success_num = 0
fail_num = 0
def getFuck(i):	
	global success_num
	global fail_num
	try:
		r = requests.get(fuu_list[i],headers=headers,timeout=6)
		if r.status_code == 200 and 'inner_top' in r.content:
			mutex.acquire()#加锁
			success_num += 1
			f.write(fuu_list[i]+'\n')
			mutex.release()#开锁
		else:
			pass				
	except Exception,e:
		print e
		with open('error.txt',r'a+') as you:
			you.write(fuu_list[i]+'\n')
			fail_num += 1		
					
	print 'success_num:'+str(success_num)+','+'fail_num:'+str(fail_num)
		
def main():	
	fuuNum = 0
	fuuNum_list = []
	for url in open('c.csv'):
		url = url.strip()
		link = 'http://club.jd.com/koubei/%s.html'%url
		fuu_list.append(link)	
		fuuNum_list.append(fuuNum)
		fuuNum += 1
	pool = ThreadPool(totalThread)
	pool.map(getFuck, fuuNum_list)
	pool.close()
	pool.join()
	
f = open('result_duo.txt',r'a+')
mutex = threading.Lock()
main()
f.close()
