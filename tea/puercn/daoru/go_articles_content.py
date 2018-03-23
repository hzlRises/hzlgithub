#coding:utf-8
import re
import xlrd
import xlwt,MySQLdb

data = xlrd.open_workbook('daoru_mip_duiying_ziduan.xlsx')
t1 = data.sheets()[1]#第二张表

rows = t1.nrows#获取行数



conn = MySQLdb.connect('','','','',charset='utf8')#连接
with conn:
	cur = conn.cursor()#让python获得执行sql的权限
	num = 0
	for i in range(1,rows):
		try:
			sql = "insert into mip_articles_content (id,content) values('%s','%s')" %(t1.row_values(i)[0],t1.row_values(i)[1])#要执行sql语句
			cur.execute(sql)#执行
			conn.commit()#提交
		except Exception,e:
			print e
		num += 1
		print num
		
conn.close()#关闭










# with open('xlsx.txt',r'w') as myText:
	# for i in range(rows):
		# for line in range(4):
			#print t1.row_values(i)[line]#第i行的第二列
			# myText.write(str(t1.row_values(i)[line])+' ')
		# myText.write('\n')
# print rows
