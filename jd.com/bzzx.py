#coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
def gettxt(id,title,pubDate,headline,QuestionacceptedAnswer):
	_str = '''
	<div style="display:none;font-size:0;"><script type="application/ld+json">{
			"@context": "https://ziyuan.baidu.com/contexts/cambrian.jsonld",
			"@id": "%s",
			"appid": "",
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
									"contentUrl": "",
									"scale": "5:2"
							}
					],
					"Author": [
							{
									"name": "京东",                                
									"jobTitle": [
											"京东官方帮助中心"
									],
									"headPortrait": ""
							}
					]
					
			}
	}</script></div>
	'''%(id,title,pubDate,headline,QuestionacceptedAnswer)
	
	return _str

num = 0
for line in open('data.txt'):
	num += 1
	id = line.strip().split('!')[0]
	title = line.strip().split('!')[1]
	pubDate = '2018-03-07T12:00:00'
	headline = line.strip().split('!')[2]
	QuestionacceptedAnswer = line.strip().split('!')[3]
	
	with open('%s_%s.txt'%(num,title.decode('utf-8')),r'a+') as my:
		my.write(gettxt(id,title,pubDate,headline,QuestionacceptedAnswer))
	
	
	


#id,title,pubdate,headline,QuestionacceptedAnswer

#2018-03-07T16:00:01

	

