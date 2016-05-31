#coding:utf-8
import MySQLdb
import sys
import re,urllib2
'''
python 操作数据库代码范例
http://www.crazyant.net/686.html
'''
'''
插入数据
'''

reload(sys)
sys.setdefaultencoding('utf8')
#获取数据
url = 'http://zhishi.fang.com/sitemap_pc_jiaju_zhishi.xml'
sitemapUrl = urllib2.urlopen(url).read()
regular = r'<loc>(.*?)</loc>'
pattren = re.compile(regular)
link = pattren.findall(sitemapUrl)

#入库
conn = MySQLdb.connect('localhost','root','','test',charset='utf8')#连接
with conn:
	cur = conn.cursor()#让python获得执行sql的权限
	for li in link:
		sql = 'insert into t2 (url) values("%s")' %li#要执行sql语句
		cur.execute(sql)#执行
		conn.commit()#提交
	conn.close()#关闭


'''
查询数据
'''

conn = MySQLdb.connect('localhost','root','','test',charset='utf8')
with conn:
	cur = conn.cursor()
	cur.execute('select * from t1 limit 10')
	data = cur.fetchall()
	for da in data:
		print da

'''
随机查询数据
上面的代码，用来将所有的结果取出，不过打印的时候是每行一个元祖打印，现在取出其中的单个数据并打印
'''
conn = MySQLdb.connect('localhost','root','','test',charset='utf8')
with conn:
	cur = conn.cursor()
	cur.execute('select * from t2 order by rand() limit 5')
	row_num = int(cur.rowcount)# 使用cur.rowcount获取结果集的条数
	for i in range(row_num):
		row = cur.fetchone()
		print row[0],row[1]