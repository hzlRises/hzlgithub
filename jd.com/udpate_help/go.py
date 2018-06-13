#coding:utf-8

import requests,json,xlwt,xlrd

def get_header():
	headers = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
		"Cache-Control": "no-cache",
		"Connection": "keep-alive",		
		"Cookie": '''''',
		"Host": "",
		"Pragma": "no-cache",
		"Upgrade-Insecure-Requests": "1",
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
	}
	return headers
	
	
	
def ana_json(j_data):
	wb = xlwt.Workbook()
	sheet = wb.add_sheet('sheet1')
	sheet.write(0,0,'id')
	sheet.write(0,1,'contentID')
	sheet.write(0,2,'title')
	sheet.write(0,3,'categoryID')
	sheet.write(0,4,'tags')
	sheet.write(0,5,'source')
	sheet.write(0,6,'author')
	sheet.write(0,7,'summary')
	sheet.write(0,8,'md5')
	sheet.write(0,9,'right_sunmmary')
	sheet.write(0,10,'content')
	sheet.write(0,11,'content_include_json')
	
	
	if j_data["message"] == 'success':
		for index,info in enumerate(j_data["info"]):
			id = info["id"]
			contentID = info["contentID"]
			title = info["title"]
			categoryID = info["categoryID"]
			tags = info["tag"]
			source = info["source"]
			author = info["author"]
			summary = info["summary"]
			md5 = info["md5"]
			#content = info["contentID"]
			sheet.write(index+1,0,id)
			sheet.write(index+1,1,contentID)
			sheet.write(index+1,2,title)
			sheet.write(index+1,3,categoryID)
			sheet.write(index+1,4,tags)
			sheet.write(index+1,5,source)
			sheet.write(index+1,6,author)
			sheet.write(index+1,7,summary)		
			sheet.write(index+1,8,md5)	
			print index
		wb.save("result.xls")
	
def main():	
	payload = {
		'pageIndex': '1',
		'pageSize': '3000',
		'categoryID': '148',
		'status': '1',
		'recommend':'',
		'type': '',
		'title': ''	
	}
	url = ''
	r = requests.get(url,params=payload,headers=get_header())
	j_data = json.loads(r.content)
	ana_json(j_data)
	
if __name__ == '__main__':
	main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
