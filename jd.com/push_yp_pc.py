#coding:utf-8
import requests,time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

print 'The file is being generated.'
num = 0
f = open('%s.txt' %num,r'a+')
for i,line in enumerate(open('url_pc.txt')):	
	f.write(line.strip()+'\n')
	if i % 100 == 99:
		f.close()
		num += 1
		f = open('%s.txt' %num,r'a+')
f.close()
print 'The file generation is complete,Please wait 3 seconds.'
time.sleep(3)
print 'Pushing data.'
for i in range(0,num+1):
	try:
		headers = {'Content-Type':'text/plain'}
		url = 'http://data.zz.baidu.com/urls'
		params = {'site':'yp.jd.com','token':'****','type':'original'}
		r = requests.post(url,params=params,headers=headers,data=open('%s.txt'%i,r'rb').read())
		print r.content
	except Exception,e:
		print e
		continue
	time.sleep(30)
print 'The data push is complete'
