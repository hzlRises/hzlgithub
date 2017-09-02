#coding:utf-8
import requests,sys,time,re,MySQLdb
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')


def main():
	conn = MySQLdb.connect('localhost','root','','lwzmx',charset='utf8')
	with conn:
		cur = conn.cursor()#让python获得执行sql的权限
		num = 0
		for url in open('aurl.txt'):
			num += 1
			
			time.sleep(1)
			headers = {
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Encoding": "gzip, deflate, sdch",
			"Accept-Language": "zh-CN,zh;q=0.8",
			"Connection": "keep-alive",
			"Cookie": "real_ipd=116.243.92.212; ECS_ID=2acbdce1d0d33b9d3ba99285d74a7d75833799f8; ECS[visit_times]=2; LXB_REFER=www.baidu.com; ECS[display]=grid; nTalk_CACHE_DATA={uid:kf_9746_ISME9754_guest1B28BDFA-6412-1D,tid:1504332333474143}; NTKF_T2D_CLIENTID=guest1B28BDFA-6412-1D60-5CCA-C770DDF38AFC; Hm_lvt_5dd4e9f0f9f64e70ce27e21fcf3b6dce=1502289649,1504332334; Hm_lpvt_5dd4e9f0f9f64e70ce27e21fcf3b6dce=1504333915",
	#		":authority": "www.lovenus.cn",
	#		":method":"GET",
	#		":path":"/gift/article_cat-174-%s.html"%i,
	#		":scheme":"https",
			"Referer":"https://www.lovenus.cn/gift/article_cat-174-2.html",
			"Upgrade-Insecure-Requests": "1",
			"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
			}
			url = url.strip()
			try:
				r = requests.get(url,headers=headers)
			except Exception,e:
				print e
			try:
				s = BeautifulSoup(r.content,"lxml")
				arcon = s.find('div',attrs={"id":"zoom"})
				con = re.findall('<p>.*</p>',str(arcon))
				concon = ''
				for c in con:
					aaa = re.sub('<a.*?>','',c)
					aaa = re.sub('</a>','',aaa)
					aaa = re.sub('<span.*?>','',aaa)
					aaa = re.sub('</span>','',aaa)
					concon += aaa
	#				with open('re_con.txt',r'a+') as my:
	#					my.write(aaa+'\n')
			except Exception,e:
				print e
			try:
				sql = 'insert into t_lovenus (arturl,artcon) values("%s","%s")' %(url,concon)#要执行sql语句
				cur.execute(sql)#执行
				conn.commit()#提交
			except Exception,e:
				print e
			print num
	conn.close()
			
if __name__ == '__main__':
	main()
	
