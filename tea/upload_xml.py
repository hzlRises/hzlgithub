#coding:utf-8
import MySQLdb,requests,paramiko,time 
import sys,datetime
reload(sys)
sys.setdefaultencoding('utf-8')

f = open('fk_sitemap.xml',r'w+')
f.write('<?xml version="1.0" encoding="utf-8"?>'+'\n')
f.write('<urlset>'+'\n')
conn = MySQLdb.connect('0','0','0','0',charset='utf8')
with conn:
	cur = conn.cursor()#让python获得执行sql的权限	
	sql = "select uuid,edit_time from mip_articles where cid!=0"	
	cur.execute(sql)#执行
	conn.commit()#提交
	data = cur.fetchall()
	for uuid,edit_time in data:
		print uuid,edit_time
			# f.write(' '+'<url>'+'\n')
			# f.write('  '+'<loc>http://heziliang.cn/article/'+uuid+'.html</loc>'+'\n')
			# f.write('  '+'<lastmod>'+str(datetime.date.today())+'</lastmod>'+'\n')
			# f.write('  '+'<changefreq>daily</changefreq>'+'\n')
			# f.write('  '+'<priority>1.0</priority>'+'\n')
			# f.write(' '+'</url>'+'\n')	
			# with open('uuid_%s.txt'%str(datetime.date.today()),r'a+') as my:
				# my.write('http://heziliang.cn/article/'+uuid+'.html'+'\n')
conn.close()#关闭
f.write('</urlset>')
f.close()


time.sleep(2)

print 'fk_sitemap.xml has been generated'

print 'upload...'


t = paramiko.Transport(('0',22))

t.connect(username='0',password='0',allow_agent=False,look_for_keys=False)

sftp = paramiko.SFTPClient.from_transport(t)

sftp.put('D:\anaconda\demo\cha\fk_sitemap.xml','/htdocs/sitemap/')#


t.close()




#print 'uuid_%s.txt has been generated'%str(datetime.date.today())
# print 'push begin...'


# url = 'http://data.zz.baidu.com/urls'
# params = {'site':'heziliang.cn','token':'0'}#,'type':'original'
# r = requests.post(url,params=params,data=open('uuid_%s.txt'%str(datetime.date.today()),r'rb').read())

# print r.content
