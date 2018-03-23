#coding:utf-8
import MySQLdb,requests,time,re
import sys,datetime
reload(sys)
sys.setdefaultencoding('utf-8')

#把xml中的数据拿下来，根据lastmod判断是否是昨天发布的文章
url_item_list = []#url和/url之间的字符
yesterday_url_list = []#仅昨天发布的文章url列表
today = time.strftime("%Y-%m-%d",time.localtime(time.time()))
#today = '2018-02-28'
print today
for i in range(1,30):#xml文件索引数值		
	url = 'http://heziliang.cn/xml/%s.xml'%i	
	r = requests.get(url)
	url_item_list = re.findall(r'<url>([\s\S]*?)</url>',r.content)#*后面的?是关键
	if len(url_item_list) == 0:
		pass
	else:
		print '------------%s------------'%i
		for item in url_item_list:
			if today in item:
				yesterday_url = re.findall(r'<loc>(.*?)</loc>',item)
				yesterday_url_list.append(yesterday_url[0])

				
f_ytd = open('yesterday_0.txt',r'w+')#昨天发布的文章url


num = 0

txt_index = 0


for link in yesterday_url_list:
	f_ytd.write(link+'\n')#把昨天的url放到单独的文件内
	
	if num % 2000 == 1999:
		f_ytd.close()
		txt_index += 1
		f_ytd = open('yesterday_%s.txt'%txt_index,r'w+')
		
	num += 1
	

	
	
	
f_ytd.close()


time.sleep(1)


#开始推送
print 'push begin'

for i in range(0,txt_index+1):
	headers = {'Content-Type':'text/plain'}
	url = 'http://data.zz.baidu.com/urls'
	
	time.sleep(1)
	#主动推送
	
	params_zd = {'site':'heziliang.cn','token':'Did6Hw3NtVVJxzYg'}
	r_zd = requests.post(url,params=params_zd,headers=headers,data=open('yesterday_%s.txt'%i,r'rb').read())
	
	
	
	#mip
	params = {'site':'heziliang.cn','token':'Did6Hw3NtVVJxzYg','type':'mip'}
	r = requests.post(url,params=params,headers=headers,data=open('yesterday_%s.txt'%i,r'rb').read())
	
	
	#amp
	params_m = {'site':'heziliang.cn','token':'Did6Hw3NtVVJxzYg','type':'amp'}
	r_m = requests.post(url,params=params_m,headers=headers,data=open('yesterday_%s.txt'%i,r'rb').read())
	

	print 'zd_push:'+r_zd.content
	print 'mip_push:'+r.content
	print 'amp_push:'+r_m.content


'''
#熊掌号
params_xzh = {'appid':'1584638868980905','token':'99XYR1EO50dhybGu','type':'realtime'}
r_xzh = requests.post(url,params=params_xzh,headers=headers,data=open('yesterday_m_%s.txt'%i,r'rb').read())


UPDATE `mip_articles` SET `publish_time`=1521811786  WHERE `id` > 9824
UPDATE `mip_articles` SET `cid` = 13 WHERE  id > 9824 and id < 13824

'''


