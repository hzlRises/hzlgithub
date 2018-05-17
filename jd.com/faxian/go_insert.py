#coding:utf-8

import requests,json,xlwt,xlrd,time
	
def main():
	filename = raw_input('input filename:')
	data = xlrd.open_workbook('%s.xlsx'%filename)
	t1 = data.sheets()[0]#第一张表
	rows = t1.nrows#获取行数
	for i in range(1,rows):
		url = 'http://yp-admin.jd.com/articleManager/submitAdd'		
		payload={
		"title":"%s"%t1.row_values(i)[0],
		"categoryID":"%s"%int(t1.row_values(i)[1]),
		"tags":"%s"%t1.row_values(i)[2],
		"source":"%s"%t1.row_values(i)[3],
		"author":"%s"%t1.row_values(i)[4],
		"summary":"%s"%t1.row_values(i)[5],
		"content":"%s"%t1.row_values(i)[6],
		}#%(t1.row_values(i)[0],t1.row_values(i)[1],t1.row_values(i)[2],t1.row_values(i)[3],t1.row_values(i)[4],t1.row_values(i)[5],t1.row_values(i)[6],t1.row_values(i)[9],t1.row_values(i)[11])
		headers = {
			"Accept": "*/*",
			"Accept-Encoding": "gzip, deflate",
			"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
			"Cache-Control": "no-cache",
			"Connection": "keep-alive",		
			"Content-Length": "",		
			"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",		
			"Cookie": '''''',
			"Host": "yp-admin.jd.com",
			"Origin": "http://yp-admin.jd.com",
			"Pragma": "no-cache",
			"Referer": "",
			"Upgrade-Insecure-Requests": "1",
			"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
		}		
		try:
			r = requests.post(url,data=payload,headers=headers,timeout=60)		
		except Exception,e:
			print e
		print i
		#time.sleep(0.1)
		# if i == 100:
			# break
	
	
if __name__ == '__main__':
	main()
	
'''
title	categoryID	tags	source	author	summary	content

'''
	
	
	
