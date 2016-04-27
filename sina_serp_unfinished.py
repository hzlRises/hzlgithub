#coding:utf-8
import pycurl
import re
import StringIO
import threading
import random
from time import ctime,sleep
'''
关键词放在kw.txt中，kw.txt文件需要用notepad++转换为ANSI编码
结果保存在result.txt中，示例：
http://finance.sina.com.cn/roll/2016-04-25/doc-ifxrprek3287200.shtml报告称首季大陆企业海外并购交易额超以往任何年度 中国新闻网 2016-04-25 16:56:17
'''
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
#获取搜索结果页链接和标题
def getWant(line):
	headers = [
		"Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Encoding:gzip, deflate, br",
		"Accept-Language:zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
		"Connection:keep-alive",
		"Host:www.baidu.com",
		"User-Agent:%s" %getUA()
	]
	url = url_list[line]#获取每个索引号为line的对应值

	c = pycurl.Curl()
	c.setopt(pycurl.URL, url)
	c.setopt(pycurl.FOLLOWLOCATION,True)
	c.setopt(pycurl.MAXREDIRS,3)
	c.setopt(pycurl.CONNECTTIMEOUT,60)
	c.setopt(pycurl.ENCODING,'gzip,deflate')
#	c.setopt(pycurl.HTTPHEADER,headers)
#	c.setopt(pycurl.POST, 1)
#	c.setopt(pycurl.POSTFIELDS, data)
	c.fp =StringIO.StringIO()	
	c.setopt(c.WRITEFUNCTION, c.fp.write)
	c.perform()
	html = c.fp.getvalue()
	#----------获取网页结束----------
	
	#----------正则提取开始----------	
	pattern = re.compile('<h2><a href="(.*)</h2>')
	htmlContent = pattern.findall(html)	
	htmlContentListToStr = ','.join(htmlContent)#列表转换为字符串，以逗号分割
	#替换掉没用的字符
	htmlContentListToStr = htmlContentListToStr.replace('" target="_blank">','').replace('<span style="color:#C03">','').replace('</span>','').replace('<span class="fgray_time">','').replace('</span>','').replace('</a>','')
	htmlContentStrToList = htmlContentListToStr.split(',')#字符串再转换为列表，方便写入文件换行
	#----------正则提取结束----------
	mutex.acquire()	#创建锁
	print 'begin:%s'% ctime()	
	f.writelines(line+'\n' for line in htmlContentStrToList)
	print '%s done'% url_list[line]
	print 'end:%s'% ctime()
	mutex.release()	#释放锁
#	sleep(1)
	
#每个线程处理一个区间
def getRange(line,r):
    for i in range(line,r):
        getWant(i)#这个函数传参起初写成了line，导致...fuck...不知道该咋说，把线程数设置成1这种极限情况就能重现bug
totalThread = 1		#设置线程数
url_list = []		#初始化关键词列表
num = 0				#初始化关键词文本中的关键词数量
for line in open('kw.txt'):	
	num += 1		#计算关键词数量
	keyword = line.strip()
	url = 'http://search.sina.com.cn/?q=%s&sort=time&sort=time&range=title&c=news&from=channel&page=1'%keyword
	url_list.append(url)#将关键词保存在url_list列表中
gap = num / totalThread#每个线程需要处理gap个url
for i,j in enumerate(url_list):#enumerate获取列表索引号
	lastIndex = i#获取最后一个索引的索引号
mutex = threading.Lock()#threading.Lock()方法添加互斥锁
f = open('result1.txt',r'w')
for line in range(0,lastIndex,gap):
	t = threading.Thread(target=getRange,args=(line, line+gap,))#循环创建线程，args传参
	t.start()
