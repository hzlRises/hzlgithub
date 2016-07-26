#coding:utf-8
import requests
#curl -H 'Content-Type:text/plain' --data-binary @urls.txt "http://data.zz.baidu.com/urls?site=domain&token=yourtoken&type=original" 
headers = {'Content-Type':'text/plain'}
url = 'http://data.zz.baidu.com/urls'
params = {'site':'domain','token':'yourtoken','type':'original'}
with open('urls.txt',r'rb') as file:	
	r = requests.post(url,params=params,headers=headers,data=''.join(file.readlines()))
	print r.content
