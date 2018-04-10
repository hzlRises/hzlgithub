#coding:utf-8
import requests,sys,re,pycurl,StringIO,time,xlrd,xlwt,MySQLdb,HeaderData
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
	conn = MySQLdb.connect('127.0.0.1','root','','tea',charset='utf8')#连接
	with conn:
		cur = conn.cursor()#让python获得执行sql的权限
		countnum = 1
		for k in open('help.jd.com_index_detail_url.txt'):			
			try:
				url = k.strip()#获取文件中的url，具体根据txt里字段定
			except Exception,e:
				print e
				
			
			#抓正文规则
			
			try:
				r = requests.get(url,headers=HeaderData.get_header(),timeout=60)
				s = BeautifulSoup(r.content,"lxml")
				title = s.find('div',attrs={"class":"help-tit1 flk06"}).get_text()				
				content = [soup.extract() for soup in s('img')]#删除文章里的img标签
				content = [soup.extract() for soup in s('a')]#删除文章里的img标签
				content = str(s.find('td')).replace('<td>','').replace('</td>','').replace('div','p')#替换掉td和div	
					
			except Exception,e:
				print e
			# try:									
			# except Exception,e:
				# print e
			#
			#入库
			try:
				sql = "insert into t_article (keywords,title,url,content) values('%s','%s','%s','%s')"%('青茶',title,url,content)
				cur.execute(sql)
				conn.commit()
			except Exception,e:
				print e
			time.sleep(0.5)
			print countnum
			countnum += 1	
			
			
	conn.close()#关闭
if __name__ == '__main__':
	main()
