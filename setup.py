#coding:utf-8
from distutils.core import setup
import py2exe
setup(console = ['Calculate.py'])
'''
python setup.py py2exe


pyinstaller  C:\Users\heziliang\tianwei\go.py 
'''



'''
1、关键词和对应的url放到kwAndUrl.txt，英文逗号隔开，utf-8编码：

成都楼盘,http://house.leju.com/sc/search/

2、cookie放到cookie.txt,从下面的地址获取cookie

https://www.baidu.com/s?wd=666tn=json&rn=50

3、双击go.exe执行


4、关键词对应的url有排名的会保存在result.txt

5、page:3,rank:2

代表第三页，第二名，只查询前5页


#coding:utf-8
import requests,time,json,sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
	cookie = open('cookie.txt',r'r').readline()
#	kw_list = [kw.strip().split(',')[0] for kw in open('kwAndUrl.txt')]
#	kw_list = [kw.strip().split(',')[1] for kw in open('kwAndUrl.txt')]
	headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "%s"%cookie,
    "Host": "www.baidu.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",    
	}
	for line in open('kwAndUrl.txt'):
		time.sleep(1)	
		print line.strip().split(',')[0].decode('utf-8')
		url = 'https://www.baidu.com/s?wd=%s&tn=json&rn=50'%line.strip().split(',')[0]
		r = requests.get(url,headers=headers)
		j_data = json.loads(r.content)
		try:
			for i in range(50):
				serpUrl = str(j_data["feed"]["entry"][i]["url"])				
				page = i/10+1
				page_rank = i%10+1
				#print page,page_rank
				if serpUrl in line.strip().split(',')[1]:					
					with open('result.txt',r'a+') as my:
						my.write(line.strip().split(',')[0]+','+line.strip().split(',')[1]+','+'page:%s'%page+','+'rank:%s'%page_rank+'\n')						
		except Exception,e:
			pass
			
		
		
		


if __name__ == '__main__':
	main()


'''
