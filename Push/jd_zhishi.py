#coding:utf-8
import requests,time,re,os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')




def main():
	#删掉yesterday文件
	if os.path.exists('yesterday.txt'):
		os.remove('yesterday.txt')

	
	#把xml中的数据拿下来，并和现有的数据去重后，留下的数据单独放到一个文件，并且追加到所有的url txt里
	url = 'http://yp.jd.com/sitemap/pinpai_0.xml'
	num = 0
	r = requests.get(url)
	zhishi_url = re.findall(r'<loc>(.*?)</loc>',r.content)
	has_push_list = [url.strip() for url in open('all_url.txt')]
	f = open('all_url.txt',r'a+')
	for link in zhishi_url:#多
		if link in has_push_list:
			pass
		else:
			with open('yesterday.txt',r'a+') as my:
				my.write(link+'\n')#把还未推送的url放到单独的文件内
			f.write(link+'\n')#追加到所有的url txt里
			num += 1
	print 'yesterday has %s'%num
	f.close()
	
	print 'crawl done'
	time.sleep(5)
	
	
	#如果昨天发布的文章超过2000，要做下分文件存储
	yesterday_url_list = [y_url.strip() for y_url in open('yesterday.txt')]
	part = 0
	f_push = open('part_%s.txt'%part,r'w+')
	for index,url in enumerate(yesterday_url_list):
		f_push.write(url+'\n')
		if index%2000 == 1999:
			f_push.close()
			part += 1
			f_push = open('part_%s.txt'%part,r'w+')
	f_push.close()
	
	time.sleep(3)
	#开始推送
	print 'push begin'
	for i in range(0,part+1):
		try:
			headers = {'Content-Type':'text/plain'}
			url = 'http://data.zz.baidu.com/urls'
			params = {'site':'www.jd.com','token':''}#,'type':'original'
			r = requests.post(url,params=params,headers=headers,data=open('part_%s.txt'%i,r'rb').read())
			print r.content
		except Exception,e:
			print e
			continue
	print 'Finish!!!'

if __name__ == '__main__':
	main()






