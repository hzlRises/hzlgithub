#coding:utf-8
author = 'heziliang'
import socket,threading,random,requests,pycurl
from multiprocessing.dummy import Pool as ThreadPool
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
socket.setdefaulttimeout(3)
#以上，引用必需的模块
fuu_list = []
totalThread = 10
def getFuck(i):	#请求页面并解析、写到本地txt		
	r = requests.get(fuu_list[i])#这个参数i是fuuNum_list列表的值。
	s = BeautifulSoup(r.content,"lxml")
	try:
		for i in s.find('div',attrs={'id':'J_selector'}).find_all('a'):
			if 'javascript' not in i.get('href') and 'cid' in i.get('href'):
				print i.get('href'),i.get_text()
				mutex.acquire()#加锁
				f.write(i.get_text()+' , '+i.get('href')+'\n')
				mutex.release()#开锁
	except Exception,e:
		print e
		
def main():	
	fuuNum = 0
	fuuNum_list = []
	for url in open('urlid_duo.txt'):
		url = url.strip()	
		fuu_list.append(url)
		#把0、1、2...自然数，存到一个fuuNum_list里
		#同时，遍历源url文件以后，把url放到fuu_list里
		#fuuNum_list的第一个索引位置的值：0，对应fuu_list中第一个索引的值，即源url文件的第一个url
		#可以认为fuuNum_list的第一个索引位置的值0，是fuu_list中第一个索引序号。
		#二营长总感觉这块能简化一些，哪位大神看到了，请联系我哈~~
		fuuNum_list.append(fuuNum)
		fuuNum += 1
	pool = ThreadPool(totalThread)
	pool.map(getFuck, fuuNum_list)#map函数将fuuNum_list里的值（自然数）均发给getFuck这个函数
	pool.close()
	pool.join()
f = open('result_duo.txt',r'a+')
mutex = threading.Lock()#设置锁
main()
f.close()
