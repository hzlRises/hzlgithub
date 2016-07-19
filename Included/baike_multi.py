#coding:utf-8
import urllib2,re,time,threading
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
#link =['http://home.fang.com/baike/1346/','http://home.fang.com/baike/1345/','http://home.fang.com/baike/1344/','http://home.fang.com/baike/1343/','http://home.fang.com/baike/1342/','http://home.fang.com/baike/1341/']
included = 0
def caclute(index):	
	global included
	data = {'wd':link[index]}
	r = requests.get("http://www.baidu.com/s",params=data)	
	mutex.acquire()	
	if '没有找到该URL' in r.text:
		print 'No>>>>'+link[index]
	else:
		included += 1
		print 'Yes>>>'+link[index]		
	mutex.release()
def getRange(line,li):
	for i in range(line,li):
		caclute(i)
totalThread = 10
mutex = threading.Lock()
gap = newKeywordNum/totalThread#607/10=60
totalSelect = totalThread*gap#60*10=600

thread_list = []
for i in range(0,totalSelect,gap):
	t = threading.Thread(target=getRange,args=(i,i+gap))
	t.start()
	thread_list.append(t)

for thread in thread_list:
	thread.join()

print 'newKeywordNum: '+str(newKeywordNum)
print 'totalSelect：'+str(totalSelect)
print 'included: '+str(included)
print 'percentage: '+'%.1f'%((float(included)/newKeywordNum)*100)+'%'