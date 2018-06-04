#coding:utf-8
import requests,time,re#MySQLdb,
import sys,datetime
reload(sys)
sys.setdefaultencoding('utf-8')

#开始推送
print 'push begin'
link_list = []
for i in range(30000,32000):
	link = 'http://www.lwzmx.com/article/%s.html'%i	
	headers = {'Content-Type':'text/plain'}
	url = 'http://data.zz.baidu.com/urls'	
	params_zd = {'site':'www.lwzmx.com','token':''}
	r_zd = requests.post(url,params=params_zd,headers=headers,data=link)

	print 'zd_push:'+r_zd.content,i
	
