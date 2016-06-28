#coding:utf-8
import MySQLdb
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf8')
conn = MySQLdb.connect('localhost','root','','heziliang',charset='utf8')
data = xlrd.open_workbook('keyword.xlsx')
sheet1 = data.sheets()[0]#第一个表
rows = sheet1.nrows#行数
with conn:
	cur = conn.cursor()
	for i in range(rows):		
		sql = 'insert into t_keyword (keyword) value ("%s")' %(sheet1.row_values(i)[0])
		cur.execute(sql)
		conn.commit()
conn.close()