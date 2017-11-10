#coding:utf-8
import requests,json,sys,time
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')

f_num = 4

headers = {
 }
f = open('z_count_re_%s.txt'%f_num,r'a+')
num = 0
for kw in open('kw_jd.txt'):
	time.sleep(0.1)
	try:
		url = ''
		load = {''}#,'enc_url_gbk':'yes'
		r = requests.get(url,params=load,headers=headers)
		j_data = json.loads(r.content.decode('gbk').encode('utf-8'))
	except Exception,e:
		print e
		with open('z_error_%s.txt'%f_num,r'a+') as my:
			my.write(kw.strip()+'\n')
		continue
		
		
	keyword = kw.strip()
	sku_name = []
	for i in range(0,100):
		try:
			if j_data["Paragraph"][i]["Content"]["warename"]:
				warename = j_data["Paragraph"][i]["Content"]["warename"]
				sku_name.append(warename)
			else:
				pass
		except Exception,e:
			print e
			break

	num += 1
	try:
		f.write(keyword.decode('gbk').encode('utf8')+','+str(len(sku_name))+'\n')
	except Exception,e:
		print e
	print num
#	if num == 100000:
#		break
f.close()
