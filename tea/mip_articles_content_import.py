#coding:utf-8
import re
import xlrd
import xlwt,MySQLdb

data = xlrd.open_workbook('daoru_mip_duiying_ziduan.xlsx')
t1 = data.sheets()[1]#第二张表

rows = t1.nrows#获取行数



conn = MySQLdb.connect('0','0','0','0',charset='utf8')#连接
with conn:
	cur = conn.cursor()#让python获得执行sql的权限
	for i in range(1,rows):
		sql = "insert into mip_articles_content (id,content) values('%s','%s')" %(t1.row_values(i)[0],t1.row_values(i)[1])#要执行sql语句
		cur.execute(sql)#执行
		conn.commit()#提交
		break		
		
conn.close()#关闭
