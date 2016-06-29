#coding:utf-8
import urllib2,re,time
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
url = 'http://home.fang.com/baike/Interface/GetLatestEntryList.aspx?num=1'
#获取最新的词条id，最新id就是所有的词条总数
xml = urllib2.urlopen(urllib2.Request(url)).read().decode('gbk').encode('utf-8')
allKeywordNum = re.search(r'<EntryID>(.*)</EntryID>', xml)
allUrlNum = int(allKeywordNum.group(0).replace('<EntryID>','').replace('</EntryID>',''))
newKeywordNum = allUrlNum - 739#所有的词条数量减去老数据数量
print 'newKeywordNum: '+str(newKeywordNum)
#只请求新的数据，请求数量根据newKeywordNum定
url2 = 'http://home.fang.com/baike/Interface/GetLatestEntryList.aspx?num=%s' %newKeywordNum
xml2 = urllib2.urlopen(urllib2.Request(url2)).read().decode('gbk').encode('utf-8')
pattern = re.compile(r'http://home.fang.com/baike/\d+/')
link = re.findall(pattern, xml2)
included = 0
all = 0
for link in link:
	try:
		data = {'wd':link}
		r = requests.get("http://www.baidu.com/s",params=data)
		if '没有找到该URL' in r.text:
			print 'No included: '+link
		else:
			included += 1
			print 'included :'+link					
	except:
		print 'error...'
	all += 1
print 'all: '+str(all)
print 'included: '+str(included)
print 'percentage: '+'%.1f'%((float(included)/all)*100)+'%'
