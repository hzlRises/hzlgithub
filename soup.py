#coding:utf-8
from bs4 import BeautifulSoup
import random
import pycurl
import StringIO
import urllib2
import re
from time import sleep
cookie = 'BAIDUID=3FDC61543A692A14C6665C6C6BAF8DAB:FG=1; H_WISE_SIDS=106833_102567_102065_100039_100331_100289_106530_102728_106665_106924_104341_106323_106702_104000_106927_106064_107042_104611_104637_106599_106795; BDSVRTM=117; BDSVRBFE=Go; __bsi=16820914715565837297_31_0_I_R_0_0303_C02F_Y_I_I_0referer:https://m.baidu.com/?from=844b&vit=fps'

def getUa():
	uaList = [
		'Mozilla/5.0 (iPod; U; CPU iPhone OS 3_1_3 like Mac OS X; zh-cn) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7E18 Safari/528.16,gzip(gfe)',
		'Mozilla/5.0 (Linux; U; Android 1.6; zh-cn; HTC Dream Build/DRC83) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/ 525.20.1,gzip(gfe)',
   		'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_3 like Mac OS X; zh-cn) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7E18 Safari/528.16,gzip(gfe)', 
		'Mozilla/5.0 (Linux; U; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
		'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/47.0.2526.70 Mobile/13C71 Safari/601.1.46',
		'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
		'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36'
	]
	ua = random.choice(uaList)
	return ua
headers = [
	"host:m.baidu.com",
	"version:HTTP/1.1",
	"accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"accept-encoding:gzip, deflate, sdch",
	"accept-language:zh-CN,zh;q=0.8",
	"User-Agent:%s"  %getUa(),
	"cookie:%s" %cookie,	
]
file = open('bbb.txt',r'r')
for line in file:
	line = line.strip()	
	url = 'http://m.baidu.com/s?word=%s' %line
	c = pycurl.Curl()
	c.setopt(c.URL,url)
	c.setopt(c.ENCODING,'gzip,deflate')
	c.setopt(pycurl.HTTPHEADER,headers)
	b = StringIO.StringIO()
	c.setopt(c.WRITEFUNCTION,b.write)
	c.perform()#括号别忘了
	html = b.getvalue()
	s = BeautifulSoup(html,"lxml")
	relativewords = s.find(id="relativewords")
	rela = str(relativewords)
	word = re.findall(r'<a[\s\S]*?>(.*?)</a>',rela)
	if word:
		with open('ccc.txt',r'a+') as a:
			a.write(line+'\n')
			print line+'you'
			for key in word:
				print key
				a.write(key+'\n')
	else:
		with open('ddd.txt',r'a+') as b:
			print line+'meiyou'
			b.write(line+'\n')
#	sleep(1)		
		
		

'''
req = urllib2.Request(url)
respon = urllib2.urlopen(req)
page = respon.read()
with open('df.txt',r'w') as my:
	my.write(page)
'''
