#coding:utf-8
import xlwt,xlrd,sys
from xlutils.copy import copy
from bs4 import BeautifulSoup

reload(sys)  
sys.setdefaultencoding('gbk')
def main():
	data = xlrd.open_workbook('insert_all.xlsx')
	t0 = data.sheets()[0]#第一张表
	rows = t0.nrows
	
	json_xls = copy(data)
	table = json_xls.get_sheet(0)
	
	for i in range(1,rows):#行
		s = BeautifulSoup(t0.row_values(i)[6],"lxml")
		img_tag = s.find_all('img')
		for img in img_tag:			
			img["alt"] = t0.row_values(i)[2]
			img["title"] = t0.row_values(i)[2]
		table.write(i,7,str(s).decode('utf-8'))
		break
	json_xls.save('insert_all_alt.xls')
	
if __name__ == '__main__':
	main()
	
	
'''
title	categoryID	tags	source	author	summary	content

'''
