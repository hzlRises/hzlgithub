#coding:utf-8
_author_ = 'heziliang'
import re,requests,sys,json
reload(sys)
sys.setdefaultencoding("utf-8")
def getJson(keyword):
	url = 'http://fanyi.youdao.com/openapi.do'
	payload = {
	'q':'%s' %keyword,
	'keyfrom':'heziliang',
	'key':'648806865',
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
		print 'None'
	print '**************************************************************************'
def main():
	while 1:
		print 'Please input keyword,input "over" to exit'
		word = raw_input()
		if word == 'over':
			sys.exit()
		keyword = word.decode('gbk').encode('utf-8')	
		getItem(getJson(keyword))
main()
	
#....................不忍直视....................
# def is_chinese(word):	
# 	if word>=u'\u4e00' and word<=u'\u9fa5':
# 		return True
# 	else:
# 		return False
# def is_over():
# 	sys.exit()
# while 1:
# 	print 'please input word...'  
# 	word = raw_input()
# 	if word == 'over':
# 		is_over()
# 	url="http://dict.youdao.com/search" 
# 	payload = {
# 	'tab':'chn',
# 	'keyfrom':'dict.top',
# 	'q':'%s' %word.decode('gbk').encode('utf-8')
# 	}
# 	r = requests.get(url,params=payload)
# 	soup = BeautifulSoup(r.content,"lxml")
# 	trans = soup.find(id="phrsListTab")
# 	if is_chinese(word.decode('gbk').encode('utf-8')):
# 		print 'hanzi'
# 	else:#英语或者数字,并且输入无语法错误
# 			if trans:
# 				li = re.findall(r'<li>(.*?)</li>', str(trans))	
# 				print '.................................'
# 				for li in li:
# 					print li.decode('utf-8')
# 				print '.................................'
# 			else:#英语或者数字输入有语法错误，有联想词
# 				try:
# 					s = BeautifulSoup(r.content,"lxml")
# 					result = s.find("div",attrs={"class":"error-typo"}).get_text()			
# 					if result:
# 						print '>>>>>>>>>>>>>>>>>>>>>>'
# 						print result
# 						print '>>>>>>>>>>>>>>>>>>>>>>'
# 				except:#英语或者数字输入有语法错误，无联想词
# 					print 'No such word like this: %s' %word