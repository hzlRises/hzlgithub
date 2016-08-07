#coding:utf-8
import urllib,random,socket,threading,random
from multiprocessing.dummy import Pool as ThreadPool
socket.setdefaulttimeout(3)
ip_list = []
def getIp(i):			
	proxy_host = "http://"+ip_list[i]
	proxy_temp = {"http":proxy_host}			
	try:				
		html = urllib.urlopen('http://www.baidu.com/',proxies=proxy_temp).read()
		mutex.acquire()	
		print ip_list[i]		
		f.write(ip_list[i]+'\n')		
		mutex.release()	
	except Exception,e:
#		print ip_list[i],e	
		pass
def main():	
#	global ipNum
	ipNum = 0
	ipNum_list = []
	for ip in open('ip.txt'):
		ipNum_list.append(ipNum)
		ip = ip.strip()
		ip_list.append(ip)
		ipNum += 1
	pool = ThreadPool(10)
	pool.map(getIp, ipNum_list)
	pool.close()
	pool.join()
	
f = open('availableip.txt',r'w')	
mutex = threading.Lock()
main()
f.close()
