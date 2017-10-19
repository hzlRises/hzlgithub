#coding:utf-8
import requests,json,csv,re
#http://club.jd.com/comment/productPageComments.action?
#callback=fetchJSON_comment98vv327299&productId=526831&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1


def main():
	csvfile = open('res_tmall.csv','wb')
	write = csv.writer(csvfile)
	write.writerow(('link','tags'))
	for link in open('sku_tmall.txt'):
		headers = {
			"accept":"*/*",
			"accept-encoding":"gzip, deflate, br",
			"accept-language":"zh-CN,zh;q=0.8",
			"Cookie":'UM_distinctid=15e03ff55456c9-0a08f812197fc3-3a3e5e06-100200-15e03ff5546875; x=__ll%3D-1%26_ato%3D0; _m_h5_tk=aeb3ffcd2bb8db0d137004ac0f22d544_1507883132787; _m_h5_tk_enc=0c25e05d6ef6b3d3401192093e6fc758; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; hng=CN%7Czh-CN%7CCNY%7C156; uss=UNljYfO%2BdGww77oeZiTuaJBn5ppsqF4c3zeBVWlRyVhQXbkOtOaCNc%2FnGWA%3D; t=f034c3f576a67b06ef415958ba769083; uc3=sg2=VFR3W3YngVWo6EVLMplQohZOFvMt0e%2FDjHxHYrXA8AE%3D&nk2=&id2=&lg2=; _tb_token_=58f34b33b5331; cookie2=1965a37ca73af7c21be92f524be2c217; JSESSIONID=7F8CC0FE9F2BBF7A52D375C24715AD92; cna=nS/GEeUDnl8CAW/KlDHqsN4X; isg=Aisr7ONv9pr4Nipvahgy9yOruk8fQC6TATSl9p2ogGrEPEmeJRPbEpPa4kqp',
			"referer":"%s"%link.strip(),
			"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
		}
		proid = link.strip().split('=')[1]
		print proid
		try:
			url = 'https://rate.tmall.com/listTagClouds.htm'
			payload = {
			'itemId':'%s'%proid,
			'isAll':'true',
			'isInner':'true',
			't':'1508397490861',
			'_ksTS':'1508397490862_1297',
			'callback':'jsonp1298',
			}
			r = requests.get(url,params=payload,timeout=60,headers=headers)
			print r.url
			if r.status_code:
				tags = re.findall(r'"tag":"(.*?)"',r.content)
				write.writerow((link.strip(),'|'.join(tags)))
			
			
		except Exception,e:
			print e
			with open('fail.txt',r'a+') as f:
				f.write(link.strip()+'\n')
if __name__ == '__main__':
		main()
