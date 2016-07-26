#coding:utf-8
import requests
#curl -H 'Content-Type:text/plain' --data-binary @urls.txt "http://data.zz.baidu.com/urls?site=home.fang.com&token=Did6Hw3NtVVJxzYg&type=original" 
headers = {'Content-Type':'text/plain'}
url = 'http://data.zz.baidu.com/urls'
params = {'site':'home.fang.com','token':'Did6Hw3NtVVJxzYg','type':'original'}
with open('urls.txt',r'rb') as file:	
	r = requests.post(url,params=params,headers=headers,data=''.join(file.readlines()))
	print r.content
