import xlrd
import xlwt,MySQLdb

'''
上面，id是 26000以后的文章 description字段要统一update（因为分类的原因，先导入的下面部分）

'''


data = xlrd.open_workbook('lwzmx_archives.xlsx')
t1 = data.sheets()[0]#第一张表

rows = t1.nrows#获取行数


conn = MySQLdb.connect('','','','',charset='utf8')#连接
with conn:
	cur = conn.cursor()#让python获得执行sql的权限
	num = 0
	for i in range(1,rows):
		try:
			sql ='''update dede_archives set description='%s' where id='%s' '''%(t1.row_values(i)[26],t1.row_values(i)[0])
			cur.execute(sql)#执行
			conn.commit()#提交
		except Exception,e:
			print e
		num += 1
		print num
		
conn.close()#关闭
