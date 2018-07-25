#coding:utf-8
import xlrd,xlwt,re
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def chuli(content):
	content = str(content)
	_str = re.sub(r'<img[\s\S]*?>','',content)
	return _str.decode('utf-8')

def main():
	data = xlrd.open_workbook('importTemlate.xlsx')
	sheet1 = data.sheets()[0]#第一个表
	rows = sheet1.nrows#行数
	print rows	
	
	wb = xlwt.Workbook()#新建一个excel表格对象
	sheet = wb.add_sheet('sheet1')#指定table名称sheet1	
	for i in range(0,rows):		
		sheet.write(i,0, sheet1.row_values(i)[0] )
		sheet.write(i,1, sheet1.row_values(i)[1])
		sheet.write(i,2, sheet1.row_values(i)[2])
		sheet.write(i,3, sheet1.row_values(i)[3])
		sheet.write(i,4, chuli(sheet1.row_values(i)[4]))	
		print i
	wb.save("no_img.xls")	

if __name__ == "__main__":
	main()
