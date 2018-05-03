#coding:utf-8
import requests,time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def main():
	file_name = 'seo_kw_urls_2018_04_12'
	
	
	part = 0
	
	f = open('part_%s.txt'%part,r'w+')	
	for i,line in enumerate(open('%s.txt'%file_name)):
		try:			
			f.write(line.strip().split(',')[1]+'\n')
		except Exception,e:
			print e
		if i%2000 == 1999:
			f.close()
			part += 1
			f = open('part_%s.txt'%part,r'w+')
	f.close()

	
	print part
	time.sleep(3)
	
	count = 0
	
	for i in range(0,part+1):
		try:
			headers = {'Content-Type':'text/plain'}
			url = 'http://data.zz.baidu.com/urls'
			params = {'site':'','token':''}#,'type':'original'
			r = requests.post(url,params=params,headers=headers,data=open('part_%s.txt'%i,r'rb').read())
			print r.content
		except Exception,e:
			print e
			continue
		
		count += 1
		print count
		time.sleep(3)
		
		
	print 'The data push is complete'

if __name__ == '__main__':
	main()



