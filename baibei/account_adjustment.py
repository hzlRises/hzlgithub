#coding:utf-8

#先下载xlrd  xlwt这两个模块，用于读、写excel
import xlrd
import xlwt


def main():
	data = xlrd.open_workbook('xy.xlsx')#打开excel
	t1 = data.sheets()[0]#第一张表	
	rows = t1.nrows#获取行数	
		
	cost_name_unsort = [t1.row_values(i)[0] for i in range(1,rows)]	#获得所有费用名称，未去重
	cost_name = []
	
	#对费用名称去重
	for i in cost_name_unsort:
		if i not in cost_name:
			cost_name.append(i)
			
			
			
	#新建一个excel
	workbook = xlwt.Workbook()
	sheet = workbook.add_sheet('result')
	sheet.write(0,0,'name')#第0行第0列，写入name
	sheet.write(0,1,'money')
	sheet.write(0,2,'count')
	
	
	
	for index,name in enumerate(cost_name):#enumerate函数：获取列表中每个元素的索引和值
		account_adjustment_money = 0#每个费用名称调账金额初始值为0
		account_adjustment_count = 0#每个费用名称调账次数初始值为0
		
		for i in range(1,rows):
			#将xy.xlsx   excel里每一行的费用名称和去重后的cost_name比较，看是否相等
			
			if t1.row_values(i)[0] == name:#如果相同
				account_adjustment_money += t1.row_values(i)[1]#调账金额相加
				account_adjustment_count += t1.row_values(i)[2]#调账次数相加		
		
	
		sheet.write(index+1,0,name)#想想这里index为什么要+1
		sheet.write(index+1,1,account_adjustment_money)
		sheet.write(index+1,2,account_adjustment_count)
		
	#想想这两个循环，总共运行了多少次
	
	workbook.save('result.xls')#保存


if __name__ == '__main__':
	main()
