# coding:utf-8
import urllib
import pycurl
import StringIO
import json
import random
'''
文件需打开并更新其中的COOKIE, TOKEN和USERID
'''
COOKIE = 'BAIDUID=2E98DE41EE30256713329930B5EB3EFF:FG=1; BIDUPSID=2E98DE41EE30256713329930B5EB3EFF; PSTM=1464002284; BDUSS=WRqNDNwckMxaVozRHdyaERLYUVjczN2UUVRdDktcDYzcXluNH5QUlE4bVh6V3RYQVFBQUFBJCQAAAAAAAAAAAEAAABh7s8nxLDErGxpZmUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJdARFeXQERXM; __cfduid=d1632abe19091880dc75d9b8696d1f1171464092485; H_PS_PSSID=19637_20145_1428_17942_19860_17001_15471_11787_20011; BDRCVFR[en5Q-dJqX6n]=mbxnW11j9Dfmh7GuZR8mvqV; BDRCVFR[FhauBQh29_R]=mbxnW11j9Dfmh7GuZR8mvqV; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a02141940599; uc_login_unique=10319896e6b1bd87aaec210874b8c16a; __cas__st__3=c05272b195a3ae7884259d02742e7752f3bdb8fa62d6ca766d7ac8f765381dbfaa47bfb056d9bb351a1909ad; __cas__id__3=8048066; __cas__rn__=214194059; SAMPLING_USER_ID=8048066'
TOKEN = 'c05272b195a3ae7884259d02742e7752f3bdb8fa62d6ca766d7ac8f765381dbfaa47bfb056d9bb351a1909ad'
USERID = '8048066'
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
f = open('resultssss.txt',r'w')
fi = open('resultsssss.txt',r'w')
for line in open('kw.txt'):
	kw = line.strip()
	print kw

	# 指定POST的内容
	post = urllib.urlencode({
		'params': '{"entry":"kr_tools","query":"%s","logid":-1,"querytype":1}' % kw,
		'path': 'jupiter/GET/kr/word',
		'token': TOKEN,
		'userid': USERID,
	})
	headers = [
		'Host: fengchao.baidu.com',
		'User-Agent: %s' %getUA(),
		'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		'Accept-Encoding: gzip, deflate',
		'Referer: http://fengchao.baidu.com/nirvana/main.html?userid=8048066',
		'Connection: keep-alive',
		'COOKIE:%s' %COOKIE,
		'TOKEN:%s' %TOKEN,
		'USERID:%s'%USERID,
	]
	url = 'http://fengchao.baidu.com/nirvana/request.ajax?path=jupiter/GET/kr/word'	
	c = pycurl.Curl()
	c.setopt(pycurl.URL, url)
	c.setopt(pycurl.ENCODING, 'gzip,deflate')
	c.fp = StringIO.StringIO()
	c.setopt(pycurl.HTTPHEADER,headers) 
	c.setopt(pycurl.POST, 1)
	c.setopt(pycurl.POSTFIELDS, post)
	c.setopt(c.WRITEFUNCTION, c.fp.write)
	c.perform()
	data = c.fp.getvalue()
	jsondata = json.loads(data)
	for group in json.loads(data)['data']['group']:
		if(group['resultitem'][0]['word'].encode('utf-8') == kw):
			print >>f, '%s %s %s' % (group['resultitem'][0]['word'].encode('utf-8'),group['resultitem'][0]['pv'],group['resultitem'][0]['wordid'])
		else:
			for line in group['resultitem']:
				print >>fi, '%s\t%d' % (line['word'].encode('utf-8'), line['pv'])
f.close
fi.close
'''
异常情况可以这样写
	if 'wordid' not in data:
		print data
		continue
'''
