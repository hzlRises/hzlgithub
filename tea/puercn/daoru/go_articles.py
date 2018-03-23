#coding:utf-8
import re
import xlrd
import xlwt,MySQLdb

data = xlrd.open_workbook('daoru_mip_duiying_ziduan.xlsx')
t1 = data.sheets()[0]#第一张表

rows = t1.nrows#获取行数



conn = MySQLdb.connect('bdm257248278.my3w.com','bdm257248278','hzlxy0202','bdm257248278_db',charset='utf8')#连接
with conn:
	cur = conn.cursor()#让python获得执行sql的权限
	num = 0
	for i in range(1,rows):
		try:
			sql = "insert into mip_articles (id,uuid,cid,uid,title,views,create_time,edit_time,is_recommend,comments,version,publish_time,collect,mip_post_num,content_id,url_name,img_url,keywords,link_tags,description,site_id,mip_push_num,amp_push_num,xzh_push_num,link_push_num,yc_push_num,baidu_spider_num,google_spider_num,so_spider_num,sm_spider_num,sogou_spider_num,baidu_spider_time,google_spider_time,so_spider_time,sm_spider_time,sogou_spider_time) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(t1.row_values(i)[0],t1.row_values(i)[1],t1.row_values(i)[2],t1.row_values(i)[3],t1.row_values(i)[4],t1.row_values(i)[5],t1.row_values(i)[6],t1.row_values(i)[7],t1.row_values(i)[8],t1.row_values(i)[9],t1.row_values(i)[10],t1.row_values(i)[11],t1.row_values(i)[12],t1.row_values(i)[13],t1.row_values(i)[14],t1.row_values(i)[15],t1.row_values(i)[16],t1.row_values(i)[17],t1.row_values(i)[18],t1.row_values(i)[19],t1.row_values(i)[20],t1.row_values(i)[21],t1.row_values(i)[22],t1.row_values(i)[23],t1.row_values(i)[24],t1.row_values(i)[25],t1.row_values(i)[26],t1.row_values(i)[27],t1.row_values(i)[28],t1.row_values(i)[29],t1.row_values(i)[30],t1.row_values(i)[31],t1.row_values(i)[32],t1.row_values(i)[33],t1.row_values(i)[34],t1.row_values(i)[35])#要执行sql语句
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