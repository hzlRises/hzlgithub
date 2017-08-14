#coding:utf-8
import requests,sys,re,pycurl,StringIO,time,xlrd,xlwt,MySQLdb
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "ww_sTitle=%E9%80%81%E5%A5%B3%E6%9C%8B%E5%8F%8B*%E7%A4%BC%E5%93%81*%E5%85%AC%E5%8F%B8%E5%BC%80%E4%B8%9A%E9%80%81%E4%BB%80%E4%B9%88%E7%A4%BC%E7%89%A9%E5%A5%BD; IPLOC=CN1100; SUV=1494858714774900; CXID=41ACAA634EC03E664106324C546F4DED; SUID=345748DF2208990A000000005857D960; sw_uuid=4000410243; ssuid=2245000202; dt_ssuid=766539408; SNUID=1278903F51540602DA6535C951608C8D; sg_uuid=2943647500; sct=5; ld=dlllllllll2B6b0nlllllVuSmGclllllWTmSOyllll9lllllRklll5@@@@@@@@@@",
    "Host": "wenwen.sogou.com",
    "Referer":"http://wenwen.sogou.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}

def main():
	conn = MySQLdb.connect('localhost','root','','lwzmx',charset='utf8')#连接
	with conn:
		cur = conn.cursor()#让python获得执行sql的权限
		countnum = 1
		for k in open('links_sogou.txt'):
			con_str = ''
			url = k.split('|')[2]
#			print url
			try:
				r = requests.get(url,headers=headers,timeout=60)
				s = BeautifulSoup(r.content,"lxml")
				content = s.find_all('pre',attrs={'class':'replay-info-txt answer_con'})
			except Exception,e:
				print e
			try:
				if content:#回答
					for c in content:
						c = str(c.get_text().strip())
						con_str += '<p>'+c+'</p>'
			except Exception,e:
				print e
			try:
				sql = 'insert into article (keywords,title,content) values("%s","%s","%s")' %(k.split('|')[0],k.split('|')[1],con_str)#要执行sql语句
				cur.execute(sql)#执行
				conn.commit()#提交
			except Exception,e:
				print e
			time.sleep(1.5)
			print countnum
			countnum += 1
			
	conn.close()#关闭
if __name__ == '__main__':
	main()


'''
def main():
	data = xlrd.open_workbook('xuanlp.xlsx')
	table = data.sheets()[3]#第三个表
	nrows = table.nrows#获取行数
	wb = xlwt.Workbook()
	sheet = wb.add_sheet('baidu')
	
	for i in range(nrows):
		print table.row_values(i)[2]#第三列
		r = requests.get(table.row_values(i)[2],headers=headers)
		s = BeautifulSoup(r.content,"lxml")
		best_content = s.find('pre',attrs={'class':'best-text mb-10'})
		if best_content:
			sheet.write(i,3,best_content.get_text().strip()+'|')
		other_answer = s.find_all('span',attrs={'class':'con'})
#		if other_answer:
#			for ot in other_answer:
#				sheet.write(i,3,ot.get_text().strip()+'|')
			
if __name__ == '__main__':
	main()
'''
