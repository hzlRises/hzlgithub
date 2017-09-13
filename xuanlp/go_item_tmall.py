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
    "Cookie": "UM_distinctid=15e03ff55456c9-0a08f812197fc3-3a3e5e06-100200-15e03ff5546875; sm4=110100; _m_h5_tk=6ec8b3869fb0ac3291542d7179df0e7b_1504838188888; _m_h5_tk_enc=4579a494752efd4b1b6d9b4c167ecda8; swfstore=292431; x=__ll%3D-1%26_ato%3D0; pnm_cku822=090%23qCQX%2FTX2X2QXPXi0XXXXXQkOIHp7k9m%2Bf%2FXMOe5rAGB3zzQosxphAwsP3Hu1j9hc3vQXi679Xvg%2FXvXuCVHkRwiPwvQXQNq4X4i20hLf5qJLyHwr9Rhw%2F4QXU6hnXXa3HoQCh9kvKx73OlZeG%2Fi8HYVmO%2BhnDug3Ho3%2Bh9kvKx73O7JkXvXuLWQ5HfDWH4QXaOXTs7wtUHJcq4QXius%2BSbQ%3D; cq=ccp%3D1; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTcCimcLtku6Q%3D%3D&lng=zh_CN&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&existShop=false&cookie21=V32FPkk%2FgihF%2FS5nrepr&tag=8&cookie15=WqG3DMC9VAQiUQ%3D%3D&pas=0; uc3=nk2=rUtN8NCAvpa%2Bmi%2BnpHjysYllru6v&id2=UonSfP0AoD7etw%3D%3D&vt3=F8dBzWffl3KjHiSOjlk%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; tracknick=%5Cu6211%5Cu4EEC%5Cu597D%5Cu50CF%5Cu5728%5Cu54EA%5Cu513F%5Cu89C1%5Cu8FC7789; _l_g_=Ug%3D%3D; unb=1896194991; lgc=%5Cu6211%5Cu4EEC%5Cu597D%5Cu50CF%5Cu5728%5Cu54EA%5Cu513F%5Cu89C1%5Cu8FC7789; cookie1=UUkM9AANVzvixHpP11xkekixJNHJkYrApK%2F7iwUTtGM%3D; login=true; cookie17=UonSfP0AoD7etw%3D%3D; cookie2=159767ea39cc92b86126078e0d01c004; _nk_=%5Cu6211%5Cu4EEC%5Cu597D%5Cu50CF%5Cu5728%5Cu54EA%5Cu513F%5Cu89C1%5Cu8FC7789; sg=913; t=f034c3f576a67b06ef415958ba769083; _tb_token_=e9e88e033e398; cna=nS/GEeUDnl8CAW/KlDHqsN4X; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; whl=-1%260%260%260; isg=AjY2XRKuczj9DAesN0-XZHaUh2wyV2sbnUxwkqAffJm049Z9COfKoZzTj4l0",
    "referer":"https://www.tmall.com/?spm=a220o.1000855.0.0.5c90c348cacB8C",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
}
def main():
	num = 0
	for item in open('re_tmall.txt'):
		skunum = 0
		time.sleep(0.5)
		try:
			url = 'http:'+item.strip().split('|')[1].split('&')[0]
			r = requests.get(url,headers=headers,timeout=60)
			s = BeautifulSoup(r.content,"lxml")
		except Exception,e:
			print e
		try:
			urltag = s.find('ul',attrs={"class":"tm-clear J_TSaleProp tb-img     "}).find_all('li')
			for li in urltag:
				skunum += 1
		except Exception,e:
			print e
		
		sku_list = []
		try:
			yulan = s.find('ul',attrs={"id":"J_UlThumb"}).find_all('img')

			for img in yulan:
				imgurl = img.get('src')
				sku_list.append(imgurl)
		except Exception,e:
			print e
		try:
			with open('re_tmall_skunum_imgurl.txt',r'a+') as my:
				my.write(item.strip()+'|'+str(skunum)+'|'+",".join(sku_list)+'\n')
		except Exception,e:
			print e
		num += 1
		print num,skunum
		break
	
	
if __name__ == '__main__':
	main()
