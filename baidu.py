#coding:utf-8
import json
import pycurl
import StringIO
import re
import random
import threading
from time import sleep,ctime
#从uaList中随机获取一个ua
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
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
    ]
    newUa = random.choice(uaList)
    return newUa
#获取关键词对应的返回json数据
def getWant(line):	
	headers = [
		"Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Encoding:gzip, deflate, br",
		"Accept-Language:zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
		"Connection:keep-alive",
		"Host:www.baidu.com",
		"User-Agent:%s" % getUA()
	]
	keyword = keyword_list[line]
	url = url_list[line]#获取每个索引号为line的对应值
	c = pycurl.Curl()
	c.setopt(pycurl.URL, url)
	c.setopt(pycurl.FOLLOWLOCATION,True)
	c.setopt(pycurl.MAXREDIRS,3)
	c.setopt(pycurl.CONNECTTIMEOUT,60)
	c.setopt(pycurl.TIMEOUT,120)
	c.setopt(pycurl.ENCODING,'gzip,deflate')
	c.setopt(pycurl.HTTPHEADER,headers)
#	c.setopt(pycurl.POST, 1)#需要post数据时使用
#	c.setopt(pycurl.POSTFIELDS, data)#需要post数据时使用
	c.fp =StringIO.StringIO()	
	c.setopt(c.WRITEFUNCTION, c.fp.write)
	c.perform()
	html = c.fp.getvalue()
	mutex.acquire()#创建锁
	
	hiturl = re.findall(r'home.fang.com\\/zhishi\\/',html)#暂时还没想出来计数的好方法
	jsondata = json.loads(html)	#转换为python的字典格式
	f.write(keyword+' ')
	if (hiturl):
		f.write('yes'+'\n')
	else:
		f.write('no'+'\n')
		
	for line in range(10):		
		serpUrl = jsondata["feed"]["entry"][line]["url"]#遍历jsondata中url键的键值
		f.write(serpUrl+'\n')#url写入文件		
	mutex.release()#释放锁

#每个线程处理一个空间
def getRange(line,r):
	for i in range(line,r):#起初写成了for i in (line,r) WTF...又栽到这个函数了
		getWant(i)

#Begin>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print 'begin:%s'% ctime()
f = open('result.txt',r'w')
totalThread  = 3	#设置线程数,线程数小于等于关键词数
keyword_list = []#初始化所有关键词列表
url_list =[]#初始化关键词拼接后的url列表
mutex = threading.Lock()#threading.Lock()方法添加互斥锁
sum = 0
for line in open('kw.txt'):
	line = line.strip()
	keyword_list.append(line)
	sum += 1#计算关键词个数

#拼接url并保存在url_list列表里
for line in keyword_list:
	line = line.strip()
	url = 'http://www.baidu.com/s?wd=%s&rn=10&tn=json'%line
	url_list.append(url)
#f.writelines(line+'\n' for line in url_list)
gap = sum/totalThread #每个线程要处理的url
for i,j in enumerate(url_list):
	lastIndex = i#获取最后一个url的索引号
for line in range(0,lastIndex,gap):
	t = threading.Thread(target=getRange,args=(line,line+gap))
	t.start()
print '正在计算,等待5秒....'
sleep(5)
hitnum = 0
for line in open('result.txt',r'r'):
	line = line.strip()
	yesOrNo = re.findall(r'yes',line)
	if(yesOrNo):
		hitnum += 1
	else:
		hitnum = hitnum
print 'all:%s'%sum
print 'hitsum:%s'%hitnum
print '%s'% str(float(hitnum)/sum*100)+'%'
print 'end:%s'%ctime()
