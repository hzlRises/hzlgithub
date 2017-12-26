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

'''
#coding:utf-8
import requests,json,sys,time,re
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
filename = 'jiage_Sxzh'

f = open('z_result_%s.txt'%filename,r'a+')

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
	"Cache-Control":"max-age=0",
    "Connection": "keep-alive",
	"Cookie":"**",
    "Host": "custom.p-search.jd.local",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
}


num = 0
for line in open('%s.txt'%filename):
	time.sleep(0.1)
	kw = line.strip().split(',')[3]
	try:
		url = '**'
		load = {
		'**':'%s'%kw,
		'**':'**',
		'**':'**',
		'**':'**',
		'**':'**'
		}
		r = requests.get(url,params=load,headers=headers)
#		j_data = json.loads(r.content.decode('gbk').encode('utf-8'))
	except Exception,e:
		print e
		with open('z_error.txt',r'a+') as my:
			my.write(kw.strip()+'\n')
		continue
	#解析
	try:
		wareid_list = re.findall('**',r.content)
				
	except Exception,e:
		print e
		with open('z_error.txt',r'a+') as my:
			my.write(kw.strip()+'\n')
		break#错误则跳出循环
	#写入
	try:
		f.write(line.strip()+','+str(len(wareid_list))+'\n')
	except Exception,e:
		print e
		with open('z_error.txt',r'a+') as my:
			my.write(kw.strip()+'\n')
	num += 1
	print num
f.close()
		

'''
