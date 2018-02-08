#coding:utf-8
import requests,re,time,sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')
for url in  open('url_1.txt'):
	url = url.strip()	
	r = requests.get(url)
	link = re.findall(r'item.jd.com/\d+.html',r.content)
	
#	print link.group(0)#item.jd.com/3133847.html

	count = 0
	try:
		for item_url in link:			
			r2 = requests.get('http://'+item_url,allow_redirects=False)
			count += 1
			if r2.status_code == 200:
				s = BeautifulSoup(r2.content,"lxml")
				f_name = s.find('a',attrs={'clstag':'shangpin|keycount|product|mbNav-1'}).get_text()
				f_url = s.find('a',attrs={'clstag':'shangpin|keycount|product|mbNav-1'}).get('href')
				
				
				s_name = s.find('a',attrs={'clstag':'shangpin|keycount|product|mbNav-2'}).get_text()
				s_url = s.find('a',attrs={'clstag':'shangpin|keycount|product|mbNav-2'}).get('href')
				
				t_name = s.find('a',attrs={'clstag':'shangpin|keycount|product|mbNav-3'}).get_text()
				t_url = s.find('a',attrs={'clstag':'shangpin|keycount|product|mbNav-3'}).get('href')
					
				
				with open('rank_item_1.txt',r'a+') as my:
					my.write(url+'|'+f_name+'|'+s_name+'|'+t_name+'|'+f_url+'|'+s_url+'|'+t_url+'\n')
				
				break
	except Exception,e:
		print e
#		with open('error_1.txt',r'a+') as my:	
#			my.write(url+'\n')
		
	if count%2 == 0:
		with open('error_1.txt',r'a+') as my:
			my.write(url+','+str(count)+'\n')
		
	print url+'-----'+str(count)

	
