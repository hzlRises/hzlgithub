#coding:utf-8
_author_ = 'heziliang'
import re,requests,sys,json
import smtplib
from email.mime.text import MIMEText
from email.header import Header
reload(sys)
sys.setdefaultencoding("utf-8")

mail_host = 'smtp.163.com'
mail_user = '****'
mail_pass = '****'
mail_to = '****'

#请求数据
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
	
#分析数据
def getItem(jsondata):
	result_list = []
	#查询词
	print '**************************************************************************'
	print 'query: '+jsondata["query"]
	query = jsondata["query"]
	result_list.append(jsondata["query"])
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
				result_list.append(item)
			except:
				pass
		result_list.append('---------------')
	except:
		#print 'No translation for: %s' %jsondata["query"]
		print 'None'
	#网络释义
	print '-------------------------------web-------------------------------------'
	try:			
		for key in range(3):#三个联想词
			try:
				print str(key+1)+' '+jsondata["web"][key]["key"]
				result_list.append(jsondata["web"][key]["key"])
			except:
				pass			
			for value in jsondata["web"][key]["value"]:#三个联想词对应的释义
				try:
					print value
					result_list.append(value)
				except:
					pass			
			print '\n'
			result_list.append('---------------')
	except:
		pass
	print '**************************************************************************'	
	result = '\n'.join(result_list)
	sendMail(query,result)

#发邮件
def sendMail(sub,content):
	msg = MIMEText(content,'plain','utf-8')
	msg['Subject'] = Header(sub,'utf-8')  #主题	
	msg['From'] = mail_user#
	msg['To'] = mail_to#
	s = smtplib.SMTP()
	s.connect(mail_host)
	s.login(mail_user, mail_pass)
	s.sendmail(mail_user,mail_to, msg.as_string())
	s.close()

def main():
	while 1:
		print 'Please input keyword,input "over" to exit'
		word = raw_input()
		if word == 'over':
			sys.exit()		
		keyword = word.decode('gbk').encode('utf-8')			
		getItem(getJson(keyword))
main()
