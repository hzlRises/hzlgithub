#coding:utf-8
import requests
#curl -H 'Content-Type:text/plain' --data-binary @urls.txt "http://data.zz.baidu.com/urls?site=domain&token=yourtoken&type=original" 
headers = {'Content-Type':'text/plain'}
url = 'http://data.zz.baidu.com/urls'
params = {'site':'domain','token':'yourtoken','type':'original'}
r = requests.post(url,params=params,headers=headers,data=open('urls.txt',r'rb'))
print r.content
