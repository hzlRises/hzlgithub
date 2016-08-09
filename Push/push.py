#coding:utf-8
import requests,pycurl,StringIO
#curl
curl -H 'Content-Type:text/plain' --data-binary @urls.txt "http://data.zz.baidu.com/urls?site=domain&token=yourtoken&type=original" 

#requests
headers = {'Content-Type':'text/plain'}
url = 'http://data.zz.baidu.com/urls'
params = {'site':'domain','token':'yourtoken','type':'original'}
r = requests.post(url,params=params,headers=headers,data=open('urls.txt',r'rb').read())
print r.content

#pycurl
url = 'http://data.zz.baidu.com/urls?site=domain&token=yourtoken'
c = pycurl.Curl()
c.setopt(c.URL,url)
c.setopt(pycurl.HTTPHEADER,['Content-Type:text/plain'])
c.setopt(c.POST,1)
c.setopt(c.POSTFIELDS,open('urls.txt',r'rb').read())
b = StringIO.StringIO()
c.setopt(c.WRITEFUNCTION, b.write)
c.perform()
info = b.getvalue()
print info



