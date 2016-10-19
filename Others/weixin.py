# coding:utf-8
'''将微信号放到whhs列表里,采集文章'''
import pycurl,StringIO,json,urllib,urllib2,re,time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

headers = [
	"User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
	"Cookie:RK=EPnrvyKs33; pgv_pvi=9085208576; pac_uid=1_2273358437; noticeLoginFlag=1; ts_uid=864776808; ptcz=5eb5cdef0bba881b5fdad31c18353d40fd0242f5a873f155197343eaec8b3730; pt2gguin=o2273358437; o_cookie=2273358437; tvfe_boss_uuid=1a889f93cefc98b9; pgv_pvid=2616135824",
	]

def Curl(url,headers):
	while 1:
		try:
			c = pycurl.Curl()
			c.setopt(pycurl.REFERER, 'http://weixin.sogou.com/')
			c.setopt(pycurl.FOLLOWLOCATION, True)
			c.setopt(pycurl.MAXREDIRS,5)
			c.setopt(pycurl.CONNECTTIMEOUT, 60)
			c.setopt(pycurl.TIMEOUT,120)
			c.setopt(pycurl.ENCODING, 'gzip,deflate')
			c.fp = StringIO.StringIO()	
			c.setopt(pycurl.URL, url)
			c.setopt(pycurl.HTTPHEADER,headers)
			c.setopt(c.WRITEFUNCTION, c.fp.write)
			c.perform()
			html = c.fp.getvalue()
			if '请输入验证码' in html:
				print u'请输入验证码,等待10分钟'
				time.sleep(600)
			else:
				return html
		except Exception, e:
			print url,'curl(url)',e
			continue 
#通过正则提取元素
def search(req,html):
	text = re.search(req,html)
	if text:
		data = text.group(1)
	else:
		data = 'null'
	return data

def getNameurl(url):
	headers = [
	"User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
	"Cookie:pgv_pvi=8963592192; GOTO=Af21330; SUV=1456054756906267072115443; tv_play_records=%CE%D2%CA%C7%B8%E8%CA%D6%B5%DA%CB%C4%BC%BE:20160129; CXID=A63419EEFE0A92DC0091E498DEBC4A3D; weixinIndexVisited=1; ABTEST=0|1475930230|v1; IPLOC=CN3100; ld=3Zllllllll2g@GUslllllVKDegklllll1f4hrlllllyllllljZlll5@@@@@@@@@@; SNUID=606E37449693A87D8E4A7850973B109A; ad=4lllllllll2gS4vulllllVkRA9UllllltfeQQyllllGlllll9llll5@@@@@@@@@@; SUID=2043E0745809950A54C1FF5700059765; JSESSIONID=aaasb9TwShfl46bCZ3vFv; sct=12; LSTMV=340%2C166; LCLKINT=1866",
	"Host:weixin.sogou.com",
	"Upgrade-Insecure-Requests:1",]
	html = Curl(url,headers)
	nameurl = search('<div target="_blank" href="([\s\S]*?)"',html).replace('&amp;','&')
	return nameurl
#采集公众号相关信息(地址,获取公众号名称、微信号、主体介绍等)及文章
def getNamesInfo(html):
	Imgurl = search('<span class="radius_avatar profile_avatar">[\s\S]*?<img src="(.*?)">[\s\S]*?</span>',html).decode('utf-8','ignore')
	nickname = search('<title>(.*?) </title>',html).decode('utf-8','ignore')
	weixinhao = search('<p class="profile_account">微信号: (.*?)</p>',html).decode('utf-8','ignore')
	nicknamedescription = search('<div class="profile_desc_value" title="(.*?)">',html).decode('utf-8','ignore') 
	zhuti = re.sub('<img class="icon_verify success".*?>','',search('<div class="profile_desc_value">(.*?)</div>',html).decode('utf-8','ignore'))
	return weixinhao,nickname,nicknamedescription,zhuti,Imgurl
# 获取文章urls
def getArticleUrls(html):
	urls = re.findall(r'(/s\?timestamp=.*?signature=.*?=)',html)
	sort_urls = map(lambda x:'http://mp.weixin.qq.com'+x,set(urls))
	return sort_urls
# 获取文章信息
def getArticleInfo(url):
	headers = [
	"User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
	"Cookie:RK=EPnrvyKs33; pgv_pvi=9085208576; pac_uid=1_2273358437; noticeLoginFlag=1; ts_uid=864776808; ptcz=5eb5cdef0bba881b5fdad31c18353d40fd0242f5a873f155197343eaec8b3730; pt2gguin=o2273358437; o_cookie=2273358437; tvfe_boss_uuid=1a889f93cefc98b9; pgv_pvid=2616135824",
]
	html = Curl(url,headers)
	title = search('<title>(.*?)</title>',html).decode('utf-8','ignore')
	datetime = search('<em id="post-date" class="rich_media_meta rich_media_meta_text">(.*?)</em>',html).decode('utf-8','ignore')
	num_url= url.replace('http://mp.weixin.qq.com/s','http://mp.weixin.qq.com/mp/getcomment') +'&&uin=&key=&pass_ticket=&wxtoken=&devicetype=&clientversion=0&x5=0'#获取阅读数/赞数的链接
	num_html = Curl(num_url,headers)
	dict_weixin  = eval(num_html)
	read_num = dict_weixin['read_num']
	like_num = dict_weixin['like_num']
	return title,read_num,like_num,datetime

#写入微信号
wxh = ['dushemeishaonv','baidu_2000','xinyuboss']
for wx_url in wxh:
	url = 'http://weixin.sogou.com/weixin?type=1&query=%s' %wx_url
	nameurl = getNameurl(url)
	html = Curl(nameurl,headers)
	weixinhao,nickname = getNamesInfo(html)[0],getNamesInfo(html)[1]
	ArticleUrls = getArticleUrls(html)
	for line in ArticleUrls:
		line = line.replace('&amp;amp;','&')
		title,read_num,like_num,datetime = getArticleInfo(line)[0],getArticleInfo(line)[1],getArticleInfo(line)[2],getArticleInfo(line)[3]
		open('nickname.txt','a+').write(nickname+' '+weixinhao+' '+title+' '+datetime+' '+str(read_num)+' '+str(like_num)+'\n')
		try:
			print title,read_num,like_num,datetime
		except Exception, e: 
			print e
			continue

