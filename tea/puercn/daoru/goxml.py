#coding:utf-8
import re
import xlrd
import xlwt,MySQLdb
import xml.dom.minidom

wb = xlwt.Workbook()#新建一个excel表格对象
sheet = wb.add_sheet('sheet1')#指定table名称sheet1


# 打开xml文档
dom = xml.dom.minidom.parse('t_article.xml')

# 得到文档元素对象
root = dom.documentElement

id = dom.getElementsByTagName('id')
keywords = dom.getElementsByTagName('keywords')
title = dom.getElementsByTagName('title')
url = dom.getElementsByTagName('url')
content = dom.getElementsByTagName('content')

for i in range(0,20226):	
	sheet.write(i,0, id[i].firstChild.data)
	sheet.write(i,1, keywords[i].firstChild.data)
	sheet.write(i,2, title[i].firstChild.data)
	sheet.write(i,3, url[i].firstChild.data)
	sheet.write(i,4, content[i].firstChild.data)	
	
wb.save("result.xls")
