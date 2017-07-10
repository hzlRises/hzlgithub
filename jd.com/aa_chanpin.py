#coding:utf-8
#处理关键词特殊字符
import requests,sys,time,re
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
def getCountnum(kw):
	keyw = kw.split(',')[0]#只取组合后关键词
	print kw
	print keyw
	try:
		url = 'https://search.jd.com/Search?keyword=%s&enc=utf-8'%keyw
		r = requests.get(url)
		s = BeautifulSoup(r.content,'lxml')
		resCount = s.find('span',attrs={'id':'J_resCount'}).get_text()
		if '+' in str(resCount):
			resCount = resCount.replace('+','')
		with open('result_0.txt',r'a+') as my:#结果存放文件
			my.write(kw+','+resCount+'\n')
	except Exception,e:
		with open('fail.txt',r'a+') as my:#异常关键词文件
			my.write(kw+'\n')
		print e 
	
def main():
	for line in open('0.txt'):#
		kw = line.strip()
		w_str=''
		reg = re.compile(r'(\(.*?\))')
		reg2 = re.compile(r'（.*?）')
		reg3 = re.compile(r'(\(.*?）)')
		reg4 = re.compile(r'(（.*?\))')
		kw = re.sub(reg,'',kw)#两边都是英文括号
		kw = re.sub(reg2,'',kw)#两边都是中文括号
		kw = re.sub(reg3,'',kw)#左边英文，右边中文
		kw = re.sub(reg4,'',kw)#左边中文，右边英文
		kw = kw.upper()#小写变大写
		getCountnum(kw)
		time.sleep(1)

if __name__ == '__main__':
	main()
