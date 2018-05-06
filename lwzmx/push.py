#coding:utf-8
import requests,time,re#MySQLdb,
import sys,datetime
reload(sys)
sys.setdefaultencoding('utf-8')

#开始推送
print 'push begin'

for i in range(1,8001):
	headers = {'Content-Type':'text/plain'}
	url = 'http://data.zz.baidu.com/urls'
	link = 'http://www.lwzmx.com/article/%s.html'%i
	
	params_zd = {'site':'www.lwzmx.com','token':''}
	r_zd = requests.post(url,params=params_zd,headers=headers,data=link)

	print 'zd_push:'+r_zd.content+link
	
	time.sleep(1)
	
