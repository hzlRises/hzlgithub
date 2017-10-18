#coding:utf-8
import requests,json,csv,sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')
headers = {
	"Accept":"application/json, text/javascript, */*; q=0.01",
	"Accept-Encoding":"gzip, deflate",
	"Accept-Language":"zh-CN,zh;q=0.8",
	"Connection":"keep-alive",
	"Content-Length":"43",
	"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
	"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
	"Cookie":'',
	"Host":"",
	"Origin":"",
	"Referer":"",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
	"X-Requested-With":"XMLHttpRequest",
}

def main():
	cfile = open('result.csv','wb')
	write = csv.writer(cfile)
	write.writerow(('moneyBpRate','name','price','productId','skuId','sortId','created','bp',))
	try:
		for i in range(600):
			url = 'http://**/web/youli/product/getList'
			data = {
			"goodsTitle":"",
			"pageNo":"",
			"pageSize":"",
			"searchKey":"",
			}
			r = requests.post(url,headers=headers,data=data)
	#		print json.loads(r.content)["success"]
			if json.loads(r.content)["success"]:
				for j in range(15):
					moneyBpRate = json.loads(r.content)["result"]["datas"][j]["moneyBpRate"]
					name = json.loads(r.content)["result"]["datas"][j]["name"]
					price = json.loads(r.content)["result"]["datas"][j]["price"]
					productId = json.loads(r.content)["result"]["datas"][j]["productId"]
					skuId = json.loads(r.content)["result"]["datas"][j]["skuId"]
					sortId = json.loads(r.content)["result"]["datas"][j]["sortId"]
					created = json.loads(r.content)["result"]["datas"][j]["created"]
					bp = json.loads(r.content)["result"]["datas"][j]["bp"]
					write.writerow((moneyBpRate,name,price,productId,skuId,sortId,created,bp))
					print i,j
	except Exception,e:
		print 'errrrrrr....'
		with open('err.txt',r'a+') as f:
			f.write(i+','+j+'\n')
	cfile.close()
	
if __name__ == '__main__':
	main()
