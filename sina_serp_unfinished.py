#coding:utf-8
import pycurl
import re
import StringIO
import threading
'''
关键词放在kw.txt中，kw.txt文件需要用notepad++转换为ANSI编码
结果保存在result.txt中，示例：
http://finance.sina.com.cn/roll/2016-04-25/doc-ifxrprek3287200.shtml报告称首季大陆企业海外并购交易额超以往任何年度 中国新闻网 2016-04-25 16:56:17

headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        #"Accept-Encoding":"gzip, deflate, sdch",
        "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control":"no-cache",
        "Connection":"keep-alive",
        "Cookie":"__cfduid=d786e5231652fb8d70822bc8264b83aab1448613293; MSA_WH=1305_706; BIDUPSID=4B0DC2F54860625BA83681F98C507951; PSTM=1450324015; BDUSS=Hp-RmRmZVJDYndpejFnNTlZTmliUnZoMm1NZmJ-NGFjbEpxd3NzLWlpbzJzYnBXQVFBQUFBJCQAAAAAAAAAAAEAAADLTBsKYTYzMTM4MTcwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADYkk1Y2JJNWW; BAIDUID=7984EC799411C607B48D0B4AB78B653F:FG=1; ispeed_lsm=2; MCITY=-%3A; locale=zh; BDSFRCVID=uFKsJeCCxG3R4IT4lZCjVRY5LvCwjeFp3e4p3J; H_BDCLCKID_SF=tbkD_C-MfIvhDRTvhCTjh-FSMgTBKI62aKDsLqbp-hcqEpO9QTbCjMTWjhA8XRbp0bTI0xjEMtQdJMoHQ-bMDUThjG0Ot60ftR3BL6rEa4OMHt-k-PnVenIVQlbZKxJmMgkebqubJKbWbtJx-l64jx50ypQuh4kOMIvAaCOFfD8bhDKmD5A35tCthUIX5-70KK0XBJ-8Kb7VbnA6Lnbkbftd2-teQj3ZJbnQobnPBK-hSb6nhJ6-XbkwQtO2-TJZfJFjVIK2JKD3j4Kkhtc55-_3qxby26nxbGReaJ5n0-nnhUo8DTtMhM4AKpOIbqJdJe3D24TSfPnJOqIRy6CajTcQjautq-JXbPoEBnjO-nT_KROvhjRhQxPyyxom3bvxtauJax-2aUcTjxQ-Wjod5xtWMxolbTJ-JT4eaDcJ-J8XMD_6j67P; BDRCVFR[ltbVPlNi2ac]=mk3SLVN4HKm; BAIDUVERIFY=608CB602B786A81630CF1E1E474CC9F8CF1CD8E00418F1747728AAAE1A2AC6E5A13455180B50F78DA15BB7B7F3B033C327C8CAFA2C7FED03AE4E46E43640F4C5F0C0:1455340720:13fac53de9399599; BDRCVFR[skC-pcPB0g_]=mbxnW11j9Dfmh7GuZR8mvqV; BD_CK_SAM=1; H_PS_PSSID=18285_1446_17710_18241_12826_18134_17000_17073_15864_12098_18086; BD_UPN=123253; H_PS_645EC=7eb54YN%2FWvivDDctjDeHAGXAb%2FoYHhBUUr12tj9Rs76OsaIcOP%2Ft%2Bb8%2FTls; sug=3; sugstore=1; ORIGIN=0; bdime=21110",
        "Host":"www.baidu.com",
        "Pragma":"no-cache",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36",
        }
'''
#获取网页代码
'''
def getHtml(line):
	url = url_list[line]#获取每个索引号为line的对应值
	c = pycurl.Curl()
	c.setopt(pycurl.FOLLOWLOCATION,True)
	c.setopt(pycurl.MAXREDIRS,3)
	c.setopt(pycurl.CONNECTTIMEOUT,60)
	c.setopt(pycurl.ENCODING,'gzip,deflate')
	c.fp =StringIO.StringIO()
	c.setopt(pycurl.URL, url)
	c.setopt(c.WRITEFUNCTION, c.fp.write)
	c.perform()
	html = c.fp.getvalue()	
	return html	
'''
#获取搜索结果页链接和标题

def getWant(line):
	url = url_list[line]#获取每个索引号为line的对应值
	c = pycurl.Curl()
	c.setopt(pycurl.FOLLOWLOCATION,True)
	c.setopt(pycurl.MAXREDIRS,3)
	c.setopt(pycurl.CONNECTTIMEOUT,60)
	c.setopt(pycurl.ENCODING,'gzip,deflate')
	c.fp =StringIO.StringIO()
	c.setopt(pycurl.URL, url)
	c.setopt(c.WRITEFUNCTION, c.fp.write)
	c.perform()
	html = c.fp.getvalue()	
	pattern = re.compile('<h2><a href="(.*)</h2>')
	htmlContent = pattern.findall(html)
	htmlContentListToStr = ','.join(htmlContent)#列表转换为字符串，以逗号分割
	#替换掉没用的字符
	htmlContentListToStr = htmlContentListToStr.replace('" target="_blank">','').replace('<span style="color:#C03">','').replace('</span>','').replace('<span class="fgray_time">','').replace('</span>','').replace('</a>','')
	#字符串再转换为列表，方便写入文件换行
	htmlContentStrToList = htmlContentListToStr.split(',')
	mutex.acquire()#创建锁	
	f.writelines(line+'\n' for line in htmlContentStrToList)
#	return htmlContentStrToList
	mutex.release()#释放锁
#每个线程处理一个区间
def getRange(line,r):
    for i in range(line,r):
        getWant(line)
mutex = threading.Lock()#threading.Lock()方法添加互斥锁
totalThread = 9#设置3个线程
url_list = []#初始化关键词列表
num = 0#初始化关键词文本中的关键词数量
for line in open('kw.txt'):	
	num += 1#计算关键词数量
	keyword = line.strip()
	url = 'http://search.sina.com.cn/?q=%s&sort=time&sort=time&range=title&c=news&from=channel&page=1'%keyword
	url_list.append(url)#将关键词保存在url_list列表中
gap = num / totalThread#gap:9/3=3，每个线程需要处理的url数量
for i,j in enumerate(url_list):#enumerate获取列表索引号
	lastIndex = i#获取最后一个索引的索引号
f = open('result1.txt',r'w')
for line in range(0,lastIndex,gap):
	t = threading.Thread(target=getRange,args=(line,line+gap))#循环创建线程，args传参
	t.start()
