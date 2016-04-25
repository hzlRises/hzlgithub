#coding:utf-8
#Pycurl通用模板 

import pycurl,StringIO,json
headers = [
	"User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0",
]
#data = json.dumps({
#	
#	})
def getHtml(url,headers):
	c = pycurl.Curl()	#通过curl方法构造一个对象
	#c.setopt(pycurl.REFERER, 'http://qy.m.58.com/')	#设置referer
	c.setopt(pycurl.FOLLOWLOCATION, True)	#自动进行跳转抓取
	c.setopt(pycurl.MAXREDIRS,5)			#设置最多跳转多少次
	c.setopt(pycurl.CONNECTTIMEOUT, 60)		#设置链接超时
	c.setopt(pycurl.TIMEOUT,120)			#下载超时
	c.setopt(pycurl.ENCODING, 'gzip,deflate')	#处理gzip内容，有些傻逼网站，就算你给的请求没有gzip，它还是会返回一个gzip压缩后的网页
	# c.setopt(c.PROXY,ip)	# 代理
	c.fp = StringIO.StringIO()	
	c.setopt(pycurl.URL, url)	#设置要访问的URL
	c.setopt(pycurl.HTTPHEADER,headers)		#传入请求头
#	c.setopt(pycurl.POST, 1)
#	c.setopt(pycurl.POSTFIELDS, data)		#传入POST数据
	c.setopt(c.WRITEFUNCTION, c.fp.write)	#回调写入字符串缓存
	c.perform()
	code = c.getinfo(c.HTTP_CODE)	#返回状态码
	html = c.fp.getvalue()	#返回源代码.
	return code
url = 'http://zhishi.fang.com/jiaju/qg_1444001.html'
http_code = getHtml(url,headers=headers)
print http_code