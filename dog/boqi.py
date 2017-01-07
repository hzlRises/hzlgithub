#coding:utf-8
import requests,sys,random,time,urllib,re
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
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
		"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
		"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
	]
	newUa = random.choice(uaList) 
	return newUa
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
	"Cache-Control":"max-age=0",
    "Connection": "keep-alive",
	"Host": "www.boqii.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": getUA(), 
}
def callback(blocknum, blocksize, totalsize):  
    '''''回调函数 
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小 
    @totalsize: 远程文件的大小 
    '''  
    percent = 100.0 * blocknum * blocksize / totalsize  
    if percent > 100:  
        percent = 100  
    print "%.2f%%"% percent
	
def writeTxt(link,title):
	r = requests.get(link,headers=headers)
	s = BeautifulSoup(r.content,"lxml")
	artContent = s.find('div',attrs={'class':'article_body'}).findAll('p')
	for p in artContent:	
		with open('%s.txt'%title,r'a+') as my:
			my.write('<p>'+str(p.get_text())+'</p>')#.get_text()
		
def downloadimg(imgurl,title):
	urllib.urlretrieve(imgurl,'img/ %s' %title+'.jpg',callback)
	
def main():
	for i in range(3,653):
		url = 'http://www.boqii.com/baike/dogfd-%s/'%i
		r = requests.get(url,headers=headers)
		s = BeautifulSoup(r.content,"lxml")
		for dt in s.find('div',attrs={'class':'art_list'}).findAll('dt'):
			artLink = dt.find('a').get('href')#文章链接			
			artImglink = dt.find('img').get('src')#文章图片链接
			artTitle = dt.find('img').get('alt')#文章标题		
			writeTxt(artLink,artTitle)#写到txt
			downloadimg(artImglink,artTitle)#下载列表页文章对应的缩略图
		time.sleep(1)
main()	
	
	
	
	
	
	
	
