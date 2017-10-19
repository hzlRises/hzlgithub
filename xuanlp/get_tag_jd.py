#coding:utf-8
import requests,json,csv,re

headers = {
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"accept-encoding":"gzip, deflate",
	"accept-language":"zh-CN,zh;q=0.8",
	"cache-control":"max-age=0",
	"Connection":"keep-alive",
	"Cookie":'**',
	"Host":"club.jd.com",
	"upgrade-insecure-requests":"1",
	"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
}

def main():
	csvfile = open('res.csv','wb')
	write = csv.writer(csvfile)
	write.writerow(('link','tags'))
	for link in open('sku.txt'):
		proid = link.strip().split('.')[2].split('/')[1]
		print proid
		try:
			url = '**'
			payload = {
			'callback':'fetchJSON_comment98vv1484',
			'productId':'%s'%proid,
			'score':'0',
			'sortType':'5',
			'page':'1',
			'pageSize':'1',
			'isShadowSku':'0',
			'fold':'1',
			}
			r = requests.get(url,params=payload,timeout=60,headers=headers)
			if r.status_code:
				tags = re.findall(r'"name":"(.*?)"',r.content)
				write.writerow((link.strip(),'|'.join(tags)))
			
			
		except Exception,e:
			print e
			with open('fail.txt',r'a+') as f:
				f.write(link.strip()+'\n')
if __name__ == '__main__':
		main()
