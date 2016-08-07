# coding:utf-8
author = 'heziliang'
'''
关键词保存在kw.txt，utf-8编码
cmd运行python fengchao.py
结果保存在result.txt
异常词保存在fail.txt
'''
import pycurl,random,urllib,StringIO,json,sys,threading,time
from multiprocessing.dummy import Pool as ThreadPool
reload(sys)
sys.setdefaultencoding('utf-8')
#更新COOKIE和TOKEN
COOKIE = 'BAIDUID=D095FB08E006A9403A79F0EE0B687930:FG=1; BIDUPSID=D095FB08E006A9403A79F0EE0B687930; PSTM=1470556111; H_PS_PSSID=1451_17945_12097_20705; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a02205688055; uc_login_unique=876229554d4b9cafc0fd835c59cd751c; __cas__st__3=a3d7336d133d73935cd12601ef62874b5d93ddbe52f3a7d37b5675e95b34e15e31c9dc78e646767f0e608de8; __cas__id__3=8048066; __cas__rn__=220568805; SAMPLING_USER_ID=8048066'
TOKEN = 'a3d7336d133d73935cd12601ef62874b5d93ddbe52f3a7d37b5675e95b34e15e31c9dc78e646767f0e608de8'
USERID = '8048066'
totalThread = 3
keyword_list = []
#availableip_list = []
#def getAvailableIp():
#	for ip in open('availableip.txt'):
#		ip = ip.strip()
#		availableip_list.append(ip)
#def getRandomAlbIp():
#	ip = random.choice(availableip_list)
#	return ip
def getUA():#随机取ua
    uaList = [
        'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1;+.NET+CLR+1.1.4322;+TencentTraveler)',
        'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1;+.NET+CLR+2.0.50727;+.NET+CLR+3.0.4506.2152;+.NET+CLR+3.5.30729)',
        'Mozilla/5.0+(Windows+NT+5.1)+AppleWebKit/537.1+(KHTML,+like+Gecko)+Chrome/21.0.1180.89+Safari/537.1',
        'Mozilla/5.0 (Windows NT 6.1; rv:44.0) Gecko/20100101 Firefox/44.0',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    ]
    newUa = random.choice(uaList)
    return newUa
def getKeyword(i):#获取json
	try:
		time.sleep(1)			
		headers = [	
		'Host:fengchao.baidu.com',
		'User-Agent: %s' %getUA(),
		'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		'Accept-Encoding: gzip, deflate',
		'Referer: http://fengchao.baidu.com/nirvana/main.html?userid=8048066',
		'Connection: keep-alive',
		'COOKIE:%s' %COOKIE,
		]
		post = urllib.urlencode({
			'params': '{"entry":"kr_station","query":"%s","querytype":1,"pageNo":1,"pageSize":300}' % keyword_list[i],
			'path': 'jupiter/GET/kr/word',
			'token': TOKEN,
			'userid': USERID,
		})
		url = 'http://fengchao.baidu.com/nirvana/request.ajax?path=jupiter/GET/kr/word'
		c = pycurl.Curl()
#		c.setopt(pycurl.PROXY, getRandomAlbIp())							
		c.setopt(pycurl.URL, url)					
		c.setopt(pycurl.FOLLOWLOCATION, True)		
		c.setopt(pycurl.MAXREDIRS,5)				
		c.setopt(pycurl.CONNECTTIMEOUT, 20)			
		c.setopt(pycurl.TIMEOUT,20)					
		c.setopt(pycurl.ENCODING, 'gzip,deflate')	
		c.fp = StringIO.StringIO()					
		c.setopt(pycurl.HTTPHEADER,headers)			
		c.setopt(pycurl.POST, 1)				
		c.setopt(pycurl.POSTFIELDS, post)			
		c.setopt(c.WRITEFUNCTION, c.fp.write)		
		c.perform()
#		mutex.acquire()#加锁
		jsonData = c.fp.getvalue()				
		analyseJsonData(i,jsonData)
#		mutex.release()#开锁
	except Exception,e:
		print e
		pass
def analyseJsonData(i,jsonData):#分析json数据
	if json.loads(jsonData)['status'] == 200:
		try:
			for group in json.loads(jsonData)['data']['group']:
				count = 0
				for line in group['resultitem']:
					count += 1
					mutex.acquire()					
					myFile.write(line['word'].encode('utf-8')+' '+str(line['pv'])+'\n')					
					mutex.release()
				print keyword_list[i]+' '+str(count)
		except Exception,e:
			print e
	else:
		print 'The request has been rejected..'	
		fail.write(keyword_list[i]+'\n')	
		
def main():	#主函数
	global totalThread
#	getAvailableIp()#读取可用ip	
	keywordNum = 0
	keywordNum_list = []
	for kw in open('kw.txt'):#读取关键词
		kw = kw.strip()
		keyword_list.append(kw)	
		keywordNum_list.append(keywordNum)
		keywordNum += 1
	pool = ThreadPool(totalThread)
	pool.map(getKeyword, keywordNum_list)
	pool.close() 
	pool.join()
	'''
	gap = keywordNum/totalThread
	thread_list = []
	for line in range(0,keywordNum,gap):#10,5
		t = threading.Thread(target=getRange,args=(line,line+gap))
		t.start()#循环开
		thread_list.append(t)
	for tt in thread_list:#循环挂起
		tt.join()
	'''
start = time.clock()
mutex = threading.Lock()
myFile = open('result.txt',r'w+')
fail = open('fail.txt',r'w+')
main()
myFile.close()
fail.close()
end = time.clock()
print "runtime: %1.fs" % (end - start)



