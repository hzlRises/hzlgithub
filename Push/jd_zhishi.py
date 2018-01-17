#coding:utf-8
import requests,time,re,os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')




def main():
#	删掉yesterday文件
#	if os.path.exists('yesterday.txt'):
#		os.remove('yesterday.txt')

	
	#把xml中的数据拿下来，并和现有的数据去重后，留下的数据单独放到一个文件，并且追加到所有的url txt里
	zhishi_url = []
	
	for i in range(0,2):
		url = 'http://yp.jd.com/sitemap/zhishi_%s.xml'%i
		r = requests.get(url)
		zhishi_url_ = re.findall(r'<loc>(.*?)</loc>',r.content)
		for url in zhishi_url_:
			zhishi_url.append(url)
	
	
	has_push_list = [url.strip() for url in open('all_url.txt')]
	f = open('all_url.txt',r'a+')#所有的url
	f_ytd = open('yesterday_0.txt',r'w+')#昨天发布的文章url
	f_ytd_m = open('yesterday_m_0.txt',r'w+')#昨天发布的文章url(m)
	
	num = 0
	txt_index = 0
	for link in zhishi_url:#多
		if link in has_push_list:
			pass
		else:
			f.write(link+'\n')#追加到所有的url txt里
			f_ytd.write(link+'\n')#把还未推送的url放到单独的文件内
			f_ytd_m.write(link.replace('www','m')+'\n')#把还未推送的url放到单独的文件内(m)
			
			if num%2000 == 1999:
				f_ytd.close()
				txt_index += 1
				f_ytd = open('yesterday_%s.txt'%txt_index,r'w+')
				f_ytd_m = open('yesterday_m_%s.txt'%txt_index,r'w+')
			num += 1
				
	f.close()
	f_ytd.close()
	f_ytd_m.close()
	print 'yesterday has %s'%num
	print 'crawl done'
	
	time.sleep(5)

	#开始推送
	print 'push begin'
	for i in range(0,txt_index+1):
		try:
			headers = {'Content-Type':'text/plain'}
			url = 'http://data.zz.baidu.com/urls'
			params = {'site':'www.jd.com','token':'00'}#,'type':'original'
			r = requests.post(url,params=params,headers=headers,data=open('yesterday_%s.txt'%i,r'rb').read())
			
			#m
			params_m = {'site':'m.jd.com','token':'00'}#,'type':'original'
			r_m = requests.post(url,params=params_m,headers=headers,data=open('yesterday_m_%s.txt'%i,r'rb').read())
			
			#熊掌号
			params_xzh = {'appid':'1584638868980905','token':'99XYR1EO50dhybGu','type':'realtime'}
			r_xzh = requests.post(url,params=params_m,headers=headers,data=open('yesterday_m_%s.txt'%i,r'rb').read())
			
			
			print 'PC:'+r.content+','+'M:'+r_m.content+','+'XZH:'+r_xzh.content
			
			
			
		except Exception,e:
			print e
			continue
	print 'Finish!!!'

if __name__ == '__main__':
	while True:
		current_time = time.localtime(time.time())
		if((current_time.tm_hour == 18) and (current_time.tm_min == 0) and (current_time.tm_sec == 0)):
			main()




