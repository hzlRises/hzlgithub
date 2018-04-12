#coding:utf-8
import xlwt,xlrd,sys
from xlutils.copy import copy

reload(sys) 
sys.setdefaultencoding('utf8')
def generate_json(id,title,pubDate,headline,QuestionacceptedAnswer):		
	json_str = '''
		<div style="display:none;font-size:0;"><script type="application/ld+json">{
				"@context": "https://ziyuan.baidu.com/contexts/cambrian.jsonld",
				"@id": "%s",
				"appid": "0",
				"title": "%s",        
				"pubDate": "%s",  
				"data": {
						"WebPage": {
								"headline": "%s",                        
								"fromSrc": "京东",
								"domain": "购物",
								"category": [
										"问答"
								]
						},
						"Question": [
								{
									"acceptedAnswer": "%s"
								}
						],
						"ImageObject": [
								{
										"contentUrl": "http://img30.360buyimg.com/jdsurvey/jfs/t17149/81/1536083007/113160/6f45338a/5acebd8aN7e9de1dd.png",
										"scale": "5:2"
								}
						],
						"Author": [
								{
										"name": "京东",                                
										"jobTitle": [
												"京东官方帮助中心"
										],
										"headPortrait": "http://img30.360buyimg.com/jdsurvey/jfs/t19627/297/391967938/15921/8ec4f397/5a73c7a9Nebc3d1d6.jpg"
								}
						]
						
				}
		}</script></div>
	'''%(id,title,pubDate,headline,QuestionacceptedAnswer)
	return json_str


def main():
	data = xlrd.open_workbook('result.xls')
	t0 = data.sheets()[0]#第一张表
	rows = t0.nrows
	pubDate = '2018-04-12T12:00:00'
	
	
	json_xls = copy(data)
	table = json_xls.get_sheet(0)
	
	for i in range(1,rows):#行
		id,title,headline,QuestionacceptedAnswer = '','','',''
		for j in range(11):#列
			if j == 7:
				id = 'https://m.jd.com/phb/zhishi/'+t0.row_values(i)[j]+'.html'				
			elif j == 8:
				title = t0.row_values(i)[j]
				headline = t0.row_values(i)[j]				
			elif j == 9:
				QuestionacceptedAnswer = t0.row_values(i)[j]
			
		_str = generate_json(id,title,pubDate,headline,QuestionacceptedAnswer)
		
		if len(t0.row_values(i)[10]+_str) < 32767:
			table.write(i,11,t0.row_values(i)[10]+_str)
		else:
			table.write(i,11,'String longer than 32767 characters')
		print i
		
	json_xls.save('result.xls')
	
	
	'''
	
	for value in values:
		table.write(row, 0, value) # xlwt对象的写方法，参数分别是行、列、值
		table.write(row, 1, "haha")
		table.write(row, 2, "lala")
		row += 1
	
	json_xls.save('result.xls')
	'''
	
if __name__ == '__main__':
	main()
