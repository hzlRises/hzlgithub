#coding=utf8 
_author_ = 'heziliang'
import md5,random,requests,json,sys
reload(sys)
sys.setdefaultencoding("utf-8")
def translate(q,lang):
	appid = '20160809000026521'
	secretKey = 'jrOmXR_CoRvifHhy32fy' 
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
def main():
	print 'Chinses2English Input 1, English2Chinses Input 2,Change Language Input 0'
	while 1:				
		cOre = raw_input('Please Input:1 or 2: ')
		if(cOre == '1'):
			while 1:	
				print 'Please Input Chinses: '
				chiWord = raw_input()
				if(chiWord == '0'):
					break
				translate(chiWord.decode('gbk').encode('utf-8'),'en')
				print '------------------------------------------------------------'
				print 'Input 0 To Reselect language'
		elif(cOre == '2'):
			while 1:
				print 'Please Input English: ' 
				engWord = raw_input()
				if(engWord == '0'):
					break
				translate(engWord.decode('gbk').encode('utf-8'),'zh')
				print '------------------------------------------------------------'
				print 'Input 0 To Reselect language'
		elif(cOre == '0'):
			pass
		else:
			print 'WTF!!!'
	
main()