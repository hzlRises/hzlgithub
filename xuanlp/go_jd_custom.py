#coding:utf-8
import requests,sys,re,pycurl,StringIO,time,xlrd,xlwt,MySQLdb,json
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "**2",
    "Host": "**",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
}
def main():
	conn = MySQLdb.connect('localhost','root','','lwzmx',charset='utf8')
	with conn:
		cur = conn.cursor()
		for kw in open('kw_jd.txt'):
			url = '**'
			load = {'key':'%s'%kw.strip(),'pagesize':'**','client':'**','sort_type':'**'}#,'enc_url_gbk':'**'
			try:
				r = requests.get(url,params=load,headers=headers)
				j_data = json.loads(r.content.decode('gbk').encode('utf-8'))
			except Exception,e:
				print e
			num = 0
			for i in range(0,**):
				keyword = kw.strip()
				if j_data["Paragraph"][i]["wareid"]:
					wareid = j_data["Paragraph"][i]["wareid"]
				else:
					wareid = ''
				if j_data["Paragraph"][i]["Content"]["warename"]:
					warename = j_data["Paragraph"][i]["Content"]["warename"]
				else:
					warename = ''
				if j_data["Paragraph"][i]["dredisprice"]:
					dredisprice = j_data["Paragraph"][i]["dredisprice"]
				else:
					dredisprice = ''
				if j_data["Paragraph"][i]["Content"]["imageurl"]:
					imageurl = j_data["Paragraph"][i]["Content"]["imageurl"]
				else:
					imageurl = ''
#				try:
#					sql = 'insert into t_jd_custom(keyword,wareid,warename,dredisprice,imageurl) values ("%s","%s","%s","%s","%s")' %(keyword,str(wareid),str(warename),str(dredisprice),imageurl)
#					cur.execute(sql)
#					conn.commit()
#				except Exception,e:
#					print e
				try:
					with open('re_custom.txt',r'a+') as my:
						my.write(keyword+'|'+str(wareid)+'|'+str(warename.encode('gbk'))+'|'+str(dredisprice)+'|'+str(imageurl)+'\n')
				except Exception,e:
					print e
				num += 1
				print kw,num
				
			time.sleep(0.5)
	conn.close()
if __name__ == '__main__':
	main()
	
	
	
	
	
	
	
