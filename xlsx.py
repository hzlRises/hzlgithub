#coding:utf-8
import re
import xlrd
import xlwt
data = xlrd.open_workbook('ceshi.xlsx')
t1 = data.sheets()[1]#第二张表
rows = t1.nrows#获取行数
with open('xlsx.txt',r'w') as myText:
	for i in range(rows):
		for line in range(4):
#			print t1.row_values(i)[line]#第i行的第二列
			myText.write(str(t1.row_values(i)[line])+' ')
		myText.write('\n')
print rows
