#coding:utf-8
import json
import pycurl
import StringIO
import re
#拼接URL
def getUrl(keyword):
	url = 'http://www.baidu.com/s?wd=%s&rn=10&tn=json'%keyword
	return url
#判断前百度前十名是否有我站url
def getIfMatch(getjson):	
	pattern = re.compile(r'zhishi.fang.com\\/jiaju\\/')
	zhishiurl = pattern.findall(getjson)
	bool = zhishiurl
	return bool
#获取关键词对应的返回json数据
def getJson(url):	
	c = pycurl.Curl();#创建实例	
	c.setopt(pycurl.CONNECTTIMEOUT, 60)#设置链接超时60
	c.setopt(pycurl.TIMEOUT,120)#下载超时	
	c.setopt(pycurl.ENCODING, 'gzip,deflate')#处理gzip内容	
	c.setopt(pycurl.URL, url)#设置要访问的URL
	c.fp = StringIO.StringIO()	
	c.setopt(c.WRITEFUNCTION, c.fp.write)#回调写入字符串缓
	c.perform()
	jsonData = c.fp.getvalue()
	return jsonData

#打开文件
f = open('result.txt',r'w')
#初始化关键词数量
keywordnum = 0
#初始化可以匹配到的关键词数量
num = 0
for line in open('kw.txt'):
	#获取关键词个
	keywordnum += 1
	#去除换行
	keyword = line.strip().replace(' ','')
	#将拼接的url赋值给geturl
	geturl = getUrl(keyword)
	#将百度返回该关键词对应的json数据赋值给getjson
	getjson = getJson(geturl)#getjson是字符串类型<type 'str'>
#	f.write(getjson)	
	#判断在获取的getjson数据中是否匹配到函数getIfMatch的正则
	if (getIfMatch(getjson)):
		#若匹配到，num自增
		num += 1
	else:
		#若没匹配到，num值不变
		num = num #刚开始逻辑写成了num = 0，打脸...
	jsondata = json.loads(getjson)#为了方便从getjson取数据，将getjson转变为python的字典格式<type 'dict'>
#	print type(jsondata)	
	f.write('%s baiduTopten url>>>>>>>>>>>>>>>>>>>>>>>>'%keyword+'\n')
	#将百度排名前十url写入文件
	for line in range(0,10):
		serpUrl = jsondata["feed"]["entry"][line]["url"]#遍历jsondata中url键的键值	
		f.write('%s'%serpUrl+'\n')
	print '%s,done'%keyword
print 'ALL:%s'%keywordnum
print 'HIT:%s'%num
print 'PERCENT:'+str((float(num)/keywordnum*100))+'%'
#关闭文件
f.close()
