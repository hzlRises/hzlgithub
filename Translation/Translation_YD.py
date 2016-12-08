#coding:utf-8
_author_ = 'heziliang'
import re,requests,sys,json
reload(sys)
sys.setdefaultencoding("utf-8")
def getJson(keyword):
	url = 'http://fanyi.youdao.com/openapi.do'
	payload = {
	'q':'%s' %keyword,
	'keyfrom':'',
	'key':'',
	'type':'data',
	'doctype':'json',
	'version':'1.1',
	'only':'dict'
	}
	r = requests.get(url,params=payload)
	jsondata = json.loads(r.content)	
	return jsondata
def getItem(jsondata):
	#查询词
	print '**************************************************************************'
	print 'query: '+jsondata["query"]
	#发音
	try:
		print 'phonetic: '+jsondata["basic"]["phonetic"].encode('gbk')
	except:
		pass
	#基本释义
	print '-------------------------------basic-----------------------------------'
	try:
		for item in jsondata["basic"]["explains"]:
			try:
				print item
			except:
				pass
	except:
		#print 'No translation for: %s' %jsondata["query"]
		print 'None'
	#网络释义
	print '-------------------------------web-------------------------------------'
	try:	
		for key in range(3):
			try:
				print str(key+1)+' '+jsondata["web"][key]["key"]
			except:
				pass
			for value in jsondata["web"][key]["value"]:
				try:
					print value
				except:
					pass				
			print '\n'
	except:
		pass
	print '**************************************************************************'
def main():
	while 1:
		print 'Please input keyword,Input "over" to exit'
		word = raw_input()
		if word == 'over':
			sys.exit()
		keyword = word.decode('gbk').encode('utf-8')	
		getItem(getJson(keyword))
main()
