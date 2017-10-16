#coding:utf-8

import requests,json,csv,sys
reload(sys)
sys.setdefaultencoding('utf-8')

csvfile = open('result.csv',r'wb')
writer = csv.writer(csvfile)
writer.writerow(('link','allcom','good','general','poor'))
for link in open('get_com_sku.txt'):
	sku = link.strip().split('.')[2].split('/')[1]
	try:
		url = 'http://*****?referenceIds=%s' %sku
		r = requests.get(url)
		
		j_data = json.loads(r.content)
		allcom = j_data['CommentsCount'][0]['CommentCount']
		goodcom = j_data['CommentsCount'][0]['GoodCount']
		generalcom = j_data['CommentsCount'][0]['GeneralCount']
		poorcom = j_data['CommentsCount'][0]['PoorCount']
		writer.writerow((link.strip(),allcom,goodcom,generalcom,poorcom))
		print link.strip(),allcom,goodcom,generalcom,poorcom
	
	except Exception,e:
		print e
		with open('get_com_sku_fail.txt',r'a+') as my:
			my.write(link.strip()+'\n')
csvfile.close()
