#coding:utf-8
authon == 'heziliang'
import socket,threading,random,requests,pycurl
from multiprocessing.dummy import Pool as ThreadPool
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
socket.setdefaulttimeout(3)
fuu_list = []
totalThread = 3
def getfuck(i):			
	r = requests.get(fuu_list[i])
	s = BeautifulSoup(r.content,"lxml")
	try:
		for i in s.find('div',attrs={'id':'J_selector'}).find_all('a'):
			if 'javascript' not in i.get('href') and 'cid' in i.get('href'):
				print i.get('href'),i.get_text()
				mutex.acquire()
				f.write(i.get_text()+' , '+i.get('href')+'\n')
				mutex.release()
	except Exception,e:
		print e
		
def main():	
	fuuNum = 0
	fuuNum_list = []
	for url in open('urlid_duo.txt'):
		url = url.strip()	
		fuu_list.append(url)
		fuuNum_list.append(fuuNum)
		fuuNum += 1
	pool = ThreadPool(totalThread)
	pool.map(getfuck, fuuNum_list)
	pool.close()
	pool.join()
f = open('result_duo.txt',r'a+')
mutex = threading.Lock()
main()
f.close()
