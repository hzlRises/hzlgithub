#coding:utf-8
import re
import xlrd
import xlwt,MySQLdb

data = xlrd.open_workbook('lwzmx_tagindex.xlsx')
t1 = data.sheets()[0]#第一张表

rows = t1.nrows#获取行数


conn = MySQLdb.connect('','','','',charset='utf8')#连接
with conn:
	cur = conn.cursor()#让python获得执行sql的权限
	num = 0
	for i in range(1,rows):
		try:
			sql ='''insert into dede_tagindex (id,tag,typeid,count,total,weekcc,monthcc,weekup,monthup,addtime) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')'''%(t1.row_values(i)[0],t1.row_values(i)[1],t1.row_values(i)[2],t1.row_values(i)[3],t1.row_values(i)[4],t1.row_values(i)[5],t1.row_values(i)[6],t1.row_values(i)[7],t1.row_values(i)[8],t1.row_values(i)[9])
			cur.execute(sql)#执行
			conn.commit()#提交
		except Exception,e:
			print e
		num += 1
		print num
		# if num > 5:
			# break
		
		
conn.close()#关闭
