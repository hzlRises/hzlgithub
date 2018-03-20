#coding:utf-8
import requests,sys,re,pycurl,StringIO,time,xlrd,xlwt,MySQLdb
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "UM_distinctid=16101ada415525-0d24551773a595-454c092b-100200-16101ada416307; bdshare_firstime=1516151612749; Hm_lvt_4752611d874ab431605fa080036e93af=1520843961,1520843964,1520844038,1521013704; _haicha=27385bdeafead0ba20027b78e7485476; CNZZDATA2903449=cnzz_eid%3D881119266-1516147207-null%26ntime%3D1521529684",
    "Host": "www.puercn.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",    
}

def main():
	conn = MySQLdb.connect('127.0.0.1','root','','tea',charset='utf8')#连接
	with conn:
		cur = conn.cursor()#让python获得执行sql的权限
		countnum = 1
		for k in open('qingcha_url.txt'):			
			try:
				url = k.strip()#获取文件中的url，具体根据txt里字段定
			except Exception,e:
				print e
				
			
			#抓正文规则
			
			try:
				r = requests.get(url,headers=headers,timeout=60)
				s = BeautifulSoup(r.content,"lxml")
				title = s.find('h1').get_text()				
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
