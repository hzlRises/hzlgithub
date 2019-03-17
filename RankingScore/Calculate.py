#coding:utf-8
import threading
import json
import pycurl
import StringIO
import MySQLdb
from time import sleep
from urlparse import urlparse
import xlrd
import xlwt
import sys
import subprocess
import os
#http://my.oschina.net/guol/blog/95699
'''
最终会生成:
result.xls	存放最终计算结果...
t_keyword.txt 存放异常关键词...
'''
reload(sys)
sys.setdefaultencoding('utf8')
def switchCase(rank):#排名第一得十分，排名第十得一分，前十没排名得零分...
	if(rank == 1):
		return 10
	elif(rank == 2):
		return 9
	elif(rank == 3):
		return 8
	elif(rank == 4):
		return 7
	elif(rank == 5):
		return 6
	elif(rank == 6):
		return 5
	elif(rank == 7):
		return 4
	elif(rank == 8):
		return 3
	elif(rank == 9):
		return 2
	elif(rank == 10):
		return 1
	else:
		return 0


domain_list = []
for line in open('last.txt'):
	line = line.strip()
	domain = line.split('>')[0]
	domain_list.append(domain)

'''
测试用...
domain_list = ['home.fang.com','www.jiatx.com','home.focus.cn']
'''
sleep(3)

wb = xlwt.Workbook()#新建一个excel表格对象
sheet = wb.add_sheet('sheet1')#指定table名称sheet1
sheet.write(0,0,'domain')#域名写入第一列...
sheet.write(0,1,'score')#该域名最终得分写入第二列...

conn = MySQLdb.connect('localhost','root','','rank',charset='utf8')

with conn:
	domainNum = 1 #初始化去重后域名数量
	cur3 = conn.cursor()
	cur3.execute('select max(id) from t_keyword')
	conn.commit()
	data = cur3.fetchall()
	for row in data:
		maxId = row[0]
	for domain in domain_list:		
		id = 0
		allscore = 0#初始化每一个域名总得分		
		for id in range(maxId+1):#有多少关键词就循环多少次
			id += 1
			cur = conn.cursor()
			sql = 'select keyword,searchnum from t_keyword where id = %s' %id #从数据库表t_keyword依次查询id号对应的关键词	
			cur.execute(sql)
			conn.commit()
			rowNum = int(cur.rowcount)
			'''
			调试用...
			print domain
			print "t_keyword_rowNum:"+str(rowNum)
			'''
			if(rowNum == 1):#如果从数据库表t_keyword可以查到id(数据库中id不一定连续)，即影响行数为1
				for keyword in range(rowNum):
					row = cur.fetchone()
					cur2 = conn.cursor()
					#根据从t_keyword查到的关键词作为条件，从表t_rank_copy中查询该关键词对应的排名前十url、具体排名...			
					sql2 = 'select keyword,url,pcrank from t_rank_copy where keyword = "%s"' %row[0]
					cur2.execute(sql2)
					conn.commit
					rowNum2 = int(cur2.rowcount)
					'''
					调试用...
					print "t_rank_copy_rowNum:"+str(rowNum2)
					'''
					if(rowNum2 != 0):#如果影响行数不为0...						
						row2_list = []#初始化每个url、每个关键词在t_rank_copy查询到的十个url列表
						for data in range(rowNum2):
							row2 = cur2.fetchone()
							'''
							调试用...
							print row2[0],urlparse(row2[1]).netloc,row2[2]	
							'''
							row2_list.append(urlparse(row2[1]).netloc)#十个域名写入row2_list中
							if domain in row2_list:#如果二级域名在列表中，说明查询该关键词时，说明前十有排名
								'''
								调试用...
								print type(row[1]),row[1]
								print type(row2[2]),row2[2]
								'''	
								score = int(row[1])*(switchCase(int(row2[2])))
								print domain+' '+str(row[0])+' '+'pagerank: '+str(row2[2])+' '+'score: '+str(score)								
								'''
								调试用...
								print score	
								'''					
								break#一旦域名匹配，结束循环
							else:
								score = 0						
						allscore = allscore + score
					else:
						print 'Not taken from t_rank_copy where keyword = %s............................' %row[0]#会有很少量的情况，从t_keyword取到关键词，但是在t_rank_copy匹配不到，费解...
						with open('t_keyword.txt',r'a+') as my:#将有问题的关键词写入t_keyword.txt
							my.write(domain+' '+row[0]+'\n')#
			elif(rowNum == 0):#若查不到id...
				pass			
			else:#受影响行数只能是1或0...sql执行不成功返回-1
				print 'error............................'
		print domain+' score: '+str(allscore)
		sheet.write(domainNum,0,domain)#域名写入第一列...
		sheet.write(domainNum,1,allscore)#该域名最终得分写入第二列...
		domainNum += 1
		wb.save("result.xls")#保存excel
conn.close()#关闭
