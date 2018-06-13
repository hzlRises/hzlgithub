#coding:utf-8
import requests,sys,re,pycurl,StringIO,time,xlrd,xlwt,HeaderData,md5,json
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver
reload(sys) 
sys.setdefaultencoding('utf-8')	

headers = {
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
		"cache-control": "no-cache",
		"cookie": "Hm_lvt_6557398d368c2c5d56b4ebf03da843a7=1528106371; Hm_lvt_7905279f5e0979a49bdc161dbad2708d=1528110006,1528110133; Hm_lvt_4fa92845bccd62fadac63eb227f2a1ef=1528110228; Hm_lpvt_4fa92845bccd62fadac63eb227f2a1ef=1528110279; Hm_lvt_2913e54536765a2bf2c08c0fb25b4003=1528110334; Hm_lvt_7064e8ba1cf87a5c008fc61e91f7b841=1528110397; Hm_lpvt_7064e8ba1cf87a5c008fc61e91f7b841=1528110397; Hm_lvt_d624ff36dcb87f17c328d73c297f7799=1528110412; Hm_lpvt_d624ff36dcb87f17c328d73c297f7799=1528110412; Hm_lvt_8257a196df3916574fa89d7567071790=1528110446; Hm_lpvt_8257a196df3916574fa89d7567071790=1528110446; Hm_lpvt_2913e54536765a2bf2c08c0fb25b4003=1528110518; Hm_lpvt_6557398d368c2c5d56b4ebf03da843a7=1528110826; Hm_lvt_7f7f65f4bf03a2c8bb731a4c628641b6=1528110829; Hm_lpvt_7905279f5e0979a49bdc161dbad2708d=1528110972; Hm_lpvt_7f7f65f4bf03a2c8bb731a4c628641b6=1528110972",
		"pragma": "no-cache",
		"upgrade-insecure-requests": "1",
		"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
	}
	
def clear_html(content_str):
	
	
	content_str = str(content_str)	
	
	content_str = re.sub(r'<div[\s\S]*?>','<div>',content_str)
	content_str = re.sub(r'<p[\s\S]*?>','<p>',content_str)
	content_str = re.sub(r'<strong[\s\S]*?>','<strong>',content_str)
	content_str = re.sub(r'<span[\s\S]*?>','<span>',content_str)
	
	#清除有style样式的标签样式
	content_str = re.sub(r'style=[\s\S]*?>','>',content_str)
	
	#清除文章内的a链接
	content_str = re.sub(r'<a[\s\S]*?>','',content_str)
	content_str = re.sub(r'</a>','',content_str)	
	
	#清除table里的标签样式	
	content_str = re.sub(r'<table[\s\S]*?>','<table>',content_str)
	content_str = re.sub(r'<tbody[\s\S]*?>','<tbody>',content_str)
	content_str = re.sub(r'<tr[\s\S]*?>','<tr>',content_str)
	content_str = re.sub(r'<th[\s\S]*?>','<th>',content_str)
	content_str = re.sub(r'<td[\s\S]*?>','<td>',content_str)
	content_str = re.sub(r'<col[\s\S]*?>','<col>',content_str)
	content_str = re.sub(r'<colgroup[\s\S]*?>','<colgroup>',content_str)		
	#制表、换行
	content_str = content_str.replace('\t','').replace('\n','')			
	
	#敏感词
	content_str = content_str.replace('阿里巴巴','')
	content_str = content_str.replace('淘宝','')
	content_str = content_str.replace('天猫','')
	content_str = content_str.replace('国美','')
	content_str = content_str.replace('苏宁','')
	content_str = content_str.replace('ali','')
	content_str = content_str.replace('alibaba','')
	content_str = content_str.replace('taobao','')
	content_str = content_str.replace('tmall','')
	content_str = content_str.replace('gome','')
	content_str = content_str.replace('suning','')
	content_str = content_str.replace('美乐乐','')
	content_str = content_str.replace('小编','')
	content_str = content_str.replace('【','')
	content_str = content_str.replace('】','')
	content_str = content_str.replace('（','')
	content_str = content_str.replace('）','')	
	content_str = content_str.replace('<span></span>','')	
	content_str = content_str.replace('秀美','')	
	content_str = content_str.replace('小编','')
	content_str = content_str.replace('女性网','')

	return content_str	
	
def get_tag(title):	
	tag = ''
	url = '?pagesize=1&qp_disable=no&client=&key=%s'%urllib.quote(title.encode('gbk'))
	r = requests.get(url)
	#JSON.Head.Query.WordSearchInfo.ShowWordOne
	try:
		j_data = json.loads(r.content.decode('gbk').encode('utf-8'))
		tag = j_data["Head"]["Query"]["WordSearchInfo"]["ShowWordOne"]	
	except Exception,e:
		print e
	if tag:
		return tag
	else:
		return 'jd'
	
def main():		
	wb = xlwt.Workbook()
	sheet = wb.add_sheet('sheet1')
	sheet.write(0,0,'categoryID')#categoryID帮助中心
	sheet.write(0,1,'tag')#tag标签
	sheet.write(0,2,'source')#文章来源
	sheet.write(0,3,'writer')#作者
	sheet.write(0,4,'title')
	sheet.write(0,5,'description')
	sheet.write(0,6,'content')	
	sheet.write(0,7,'origin_url')
	

	filename = 'jiajujiajichangshi'
	
	content_url_list = [url.strip() for url in open("%s.txt"%filename)]			
	for index,k in enumerate(content_url_list):
		content_str = ''
		content_txt = ''
		title = ''
		crumb = ''
		try:				
			url = 'https://i.7y7.com/mip/'+k.split('/')[-1]
			
			r = requests.get(url,headers=headers,timeout=60)
			#max_page = get_max_page(r.content)			
				#如果是404页面，直接跳过
			if '404' in BeautifulSoup(r.content,"lxml").find('title').get_text():
				continue
			else:				
				s = BeautifulSoup(r.content,"lxml")			
				title = s.find('h1').get_text()
				crumb = s.find('header').get_text()
				
				content_str = s.find('div',attrs={"class":"word_2x box full"})				
				content_txt = str(s.find('div',attrs={"class":"word_2x box full"}).get_text()[0:150]).decode('utf-8')	
				content_str = clear_html(content_str)	
		except Exception,e:
			print e	
			with open('error.txt',r'a+') as my:
				my.write(k.strip()+'\n')
		#抓正文规则
		try:			
			sheet.write(index+1,0,'000')#categoryID帮助中心
			sheet.write(index+1,1,get_tag(title))#tag标签
			sheet.write(index+1,2,'jd')#文章来源
			sheet.write(index+1,3,'jd')#作者
			sheet.write(index+1,4,title.decode('utf-8'))
			sheet.write(index+1,5,content_txt)
			if len(content_str) < 32767:
				sheet.write(index+1,6,content_str.decode('utf-8'))
			else:
				sheet.write(index+1,6,'String longer than 32767 characters')				
			sheet.write(index+1,7,url)
			sheet.write(index+1,8,crumb.decode('utf-8'))			
			wb.save("result_%s.xls"%filename)		
		except Exception,e:
			print e
		print filename,index
		# if index == 10:
			# break
		
if __name__ == '__main__':
	main()
