#coding:utf-8
from bs4 import BeautifulSoup

import requests,sys,time
reload(sys)
sys.setdefaultencoding('utf-8')
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "cache-control": "max-age=0",
    "Cookie": "_med=dw:1366&dh:768&pw:1366&ph:768&ist:0; UM_distinctid=15e03ff55456c9-0a08f812197fc3-3a3e5e06-100200-15e03ff5546875; sm4=110100; _m_h5_tk=6ec8b3869fb0ac3291542d7179df0e7b_1504838188888; _m_h5_tk_enc=4579a494752efd4b1b6d9b4c167ecda8; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTcCimdD2B%2Fog%3D%3D&lng=zh_CN&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&existShop=false&cookie21=WqG3DMC9Fb5mPLIQoVXj&tag=8&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0; uc3=nk2=rUtN8NCAvpa%2Bmi%2BnpHjysYllru6v&id2=UonSfP0AoD7etw%3D%3D&vt3=F8dBzWffmKIs7ohjEBw%3D&lg2=UtASsssmOIJ0bQ%3D%3D; tracknick=%5Cu6211%5Cu4EEC%5Cu597D%5Cu50CF%5Cu5728%5Cu54EA%5Cu513F%5Cu89C1%5Cu8FC7789; _l_g_=Ug%3D%3D; unb=1896194991; lgc=%5Cu6211%5Cu4EEC%5Cu597D%5Cu50CF%5Cu5728%5Cu54EA%5Cu513F%5Cu89C1%5Cu8FC7789; cookie1=UUkM9AANVzvixHpP11xkekixJNHJkYrApK%2F7iwUTtGM%3D; login=true; cookie17=UonSfP0AoD7etw%3D%3D; cookie2=159767ea39cc92b86126078e0d01c004; _nk_=%5Cu6211%5Cu4EEC%5Cu597D%5Cu50CF%5Cu5728%5Cu54EA%5Cu513F%5Cu89C1%5Cu8FC7789; sg=913; t=f034c3f576a67b06ef415958ba769083; _tb_token_=e9e88e033e398; cq=ccp%3D0; swfstore=146220; x=__ll%3D-1%26_ato%3D0; tt=tmall-main; cna=nS/GEeUDnl8CAW/KlDHqsN4X; pnm_cku822=090%23qCQXk4X2X2PXPXi0XXXXXQkOIHp7kG9cfQnZO6hiAGBpBoO7hnUn%2BldOIHR1H9Gt3vQXi679XvDtXvXQ0ZsNLKQiXiqTftnb8UkGZTvzLv7WGuGngH93XvXPceEUFDMuYwwkXvXuLWQ5HfDW%2F4QXU6hnXXa3HoQCh9kvKx73OlZeG%2Fi8HYVmO%2BhnDug3Ho3%2Bh9kvKx73O7h%2FXvXuTPu2AQIj; res=scroll%3A1349*5454-client%3A1349*638-offset%3A1349*5454-screen%3A1366*768; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; whl=-1%260%260%260; isg=Anh4lx51VWMM47kWhRmxzoR6SSYA4c3hb5JuiLLpxLNmzRi3WvGs-47v8fMG",
    "referer":"https://www.tmall.com/?spm=a220o.1000855.0.0.5c90c348cacB8C",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
}
#https://list.tmall.com/search_product.htm?&smAreaId=110100&smToken=d5ab69fafe104a119d1b68cf5dee8e2b&smSign=tynCTnJ2%2BacN%2F4nGJImRRQ%3D%3D
def main():
	for kw in open('kw_tmall.txt'):
		for page in range(5):
			page = page * 60
			url = 'https://list.tmall.com/search_product.htm'
			payload = {
			'q':'%s'%kw.strip(),
			's':'%s'%page,
			'spm':'a220m.1000858.0.0.4c637810i4favJ',
			'sort':'d',
			'smToken':'d5ab69fafe104a119d1b68cf5dee8e2b',
			'cat':'50036568',
			'style':'g',
			'from':'mallfp..pc_1_searchbutton',
			'smAreaId':'110100',
			'smSign':'tynCTnJ2%2BacN%2F4nGJImRRQ%3D%3D',
			}
			r = requests.get(url,params=payload,headers=headers,timeout=60)
			s = BeautifulSoup(r.content,"lxml")
			divtag = s.find_all('div',attrs={'class':'product-iWrap'})
			for at in divtag:
				sku = at.find('a').get('href')#商品链接
				if at.find('img').get('src'):#这块应该是图片延时加载，导致img标签属性不一致，需要判断
					img = at.find('img').get('src')
				else:
					img = at.find('img').get('data-ks-lazyload')
				price = at.find('em').get('title')#价格
				title = at.find('p',attrs={"class":"productTitle"}).find('a').get('title')
				print sku,img,price,title
			break
		break


	
if __name__ == '__main__':
	main()
