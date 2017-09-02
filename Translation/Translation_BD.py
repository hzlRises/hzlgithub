#coding:utf-8 
_author_ = 'heziliang'
import md5,random,requests,json,sys
reload(sys)
sys.setdefaultencoding("utf-8")
def translate(q,lang):
	appid = ''#自己申请的id
	secretKey = '' #密钥
	myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
	fromLang = 'auto'
	toLang = '%s' %lang
	salt = random.randint(32768, 65536)
	sign = appid+q+str(salt)+secretKey
	m1 = md5.new()
	m1.update(sign)
	sign = m1.hexdigest()
	#好像也不需要urllib.quote(q)
	myurl = myurl+'?appid='+appid+'&q='+q+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
	r = requests.get(myurl)
	jsondata = json.loads(r.content)
	try:
		print jsondata["trans_result"][0]["dst"]
	except Exception,e:
		print e
def chiToeng():
	while 1:
		print u'请输入中文（切换模式输入"0"）: '
		chiWord = raw_input()
		if(chiWord == '0'):
			engTochi()
		translate(chiWord.decode('gbk').encode('utf-8'),'en')
		
		print '-------------------------------------------------'
def engTochi():
	while 1:
		print u'请输入英语（切换模式输入"0"）: ' 
		engWord = raw_input()
		if(engWord == '0'):
			chiToeng()
		translate(engWord.decode('gbk').encode('utf-8'),'zh')
		
		print '-------------------------------------------------'
def main():
	print u'汉译英输入"1"，英译汉输入"2"，切换模式输入"0"'
	print u'选择模式后按回车键...'
	while 1:
		cOre = raw_input('Please Choose: ')
		if(cOre == '1'):
			chiToeng()
		elif(cOre == '2'):
			engTochi()
		elif(cOre == '0'):
			print u'请先选择一种翻译模式'
		else:
			print u'别闹...'
		
main()



'''

#coding:utf-8 
_author_ = 'heziliang'
import md5,random,requests,json,sys
reload(sys)
sys.setdefaultencoding("utf-8")
def translate(q):
	appid = ''#自己申请的id
	secretKey = '' #密钥
	myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
	fromLang = 'auto'
	toLang = 'auto'
	salt = random.randint(32768, 65536)
	sign = appid+q+str(salt)+secretKey
	m1 = md5.new()
	m1.update(sign)
	sign = m1.hexdigest()
	#好像也不需要urllib.quote(q)
	myurl = myurl+'?appid='+appid+'&q='+q+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
	r = requests.get(myurl)
	jsondata = json.loads(r.content)
	print '--------------------------------------------------------------------------------'
	try:
		print jsondata["trans_result"][0]["dst"]
	except Exception,e:
		print e
	print '--------------------------------------------------------------------------------'
def main():
	while 1:
		print u'请输入想要翻译的汉字或英语'
		cOre = raw_input()
		translate(cOre.decode('gbk').encode('utf-8'))
main()

'''
