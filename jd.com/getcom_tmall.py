#coding:utf-8

import requests,json,csv,sys,re
reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"accept-encoding":"gzip, deflate, br",
	"accept-language":"zh-CN,zh;q=0.8",
	"cache-control":"max-age=0",
	"cookie":"UM_distinctid=15e03ff55456c9-0a08f812197fc3-3a3e5e06-100200-15e03ff5546875; x=__ll%3D-1%26_ato%3D0; _m_h5_tk=aeb3ffcd2bb8db0d137004ac0f22d544_1507883132787; _m_h5_tk_enc=0c25e05d6ef6b3d3401192093e6fc758; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTcBz3MDo4dAg%3D%3D&lng=zh_CN&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&existShop=false&cookie21=VFC%2FuZ9aiKCaj7AzMpJs&tag=8&cookie15=UtASsssmOIJ0bQ%3D%3D&pas=0; uc3=sg2=VFR3W3YngVWo6EVLMplQohZOFvMt0e%2FDjHxHYrXA8AE%3D&nk2=rUtN8NCAvpa%2Bmi%2BnpHjysYllru6v&id2=UonSfP0AoD7etw%3D%3D&vt3=F8dBzLBCKqrQEJErdJ8%3D&lg2=W5iHLLyFOGW7aA%3D%3D; tracknick=%5Cu6211%5Cu4EEC%5Cu597D%5Cu50CF%5Cu5728%5Cu54EA%5Cu513F%5Cu89C1%5Cu8FC7789; _l_g_=Ug%3D%3D; ck1=; unb=1896194991; lgc=%5Cu6211%5Cu4EEC%5Cu597D%5Cu50CF%5Cu5728%5Cu54EA%5Cu513F%5Cu89C1%5Cu8FC7789; cookie1=UUkM9AANVzvixHpP11xkekixJNHJkYrApK%2F7iwUTtGM%3D; login=true; cookie17=UonSfP0AoD7etw%3D%3D; cookie2=1bc8498b14ab7287071d7d592f8547b7; _nk_=%5Cu6211%5Cu4EEC%5Cu597D%5Cu50CF%5Cu5728%5Cu54EA%5Cu513F%5Cu89C1%5Cu8FC7789; t=f034c3f576a67b06ef415958ba769083; uss=UNljYfO%2BdGww77oeZiTuaJBn5ppsqF4c3zeBVWlRyVhQXbkOtOaCNc%2FnGWA%3D; skt=0a67b1eb5791043a; _tb_token_=e31e193a37658; JSESSIONID=E3C837A6F3658A4A68051A5AFD4C0FE3; cna=nS/GEeUDnl8CAW/KlDHqsN4X; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; whl=-1%260%260%260; isg=Ak9PkuWtSqNNqU5ztkwegyen3uNTdLLHhagBCmFc5b7FMG8yaUQz5k1oRlZ1",
	"upgrade-insecure-requests":"1",
	"user-agent":"ozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",



}

csvfile = open('result_tmall.csv',r'wb')
writer = csv.writer(csvfile)
writer.writerow(('link','allcom'))
for link in open('get_com_sku_tmall.txt'):
	sku = link.strip().split('=')[1]
	print sku
	try:
		url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=%s&spuId=%s&sellerId=%s' %(sku,sku,sku)
		r = requests.get(url,headers=headers)
		total_ = re.search('"total":(\d+)',r.content)
		ttl = total_.group(0).replace('"','').replace(':','').replace('total','')
		writer.writerow((link.strip(),ttl))
	except Exception,e:
		print e
		with open('get_com_sku_fail_tmall.txt',r'a+') as my:
			my.write(link.strip()+'\n')

			
csvfile.close()
