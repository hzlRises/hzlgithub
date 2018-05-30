#coding:utf-8
import requests,sys,re,pycurl,StringIO,time,xlrd,xlwt,HeaderData,md5,json
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver
reload(sys) 
sys.setdefaultencoding('utf-8')	
	
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
	url = ''%urllib.quote(title.encode('gbk'))
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

		
def get_max_page(content):
	content_srt = str(content)#.decode('',errors='ignore')
	
	num = re.findall(r'(\d+)</a></li><li><a',content_srt)#.decode('utf-8',errors='ignore')

	if num:
		return int(num[-1])
	else:
		return 0

		
		
def get_content(url,max_page):
	url_qian = url.split('.')[0]
	content_zuhe = ''
	
	r_0 = requests.get('http://www.wed114.cn'+url,headers=HeaderData.get_header(),timeout=60)
	s_0 = BeautifulSoup(r_0.content,"lxml")	
	content_str_0 = s_0.find('div',attrs={"class":"substance"})
	content_str_0 = clear_html(content_str_0)

	
	content_zuhe = content_zuhe + content_str_0
	
	title_0 = s_0.find('h1').get_text()
	crumb_0 = s_0.find('div',attrs={"class":"position"}).find_all('a')
	cru_str = ''
	for cru in crumb_0:
		cru_str = cru_str + cru.get_text()+'>'
		
	content_txt_0 = str(s_0.find('div',attrs={"class":"substance"}).get_text()[0:150]).decode('utf-8')
	
	
	for i in range(2,max_page+1):
		r = requests.get('http://www.wed114.cn'+url_qian+'_'+str(i)+'.html',headers=HeaderData.get_header(),timeout=60)
		if '404' in BeautifulSoup(r.content,"lxml").find('title').get_text():
			continue
		else:				
			s = BeautifulSoup(r.content,"lxml")					
			content_str = s.find('div',attrs={"class":"substance"})		
			content_str = clear_html(content_str)
			content_zuhe = content_zuhe + content_str
			
	return title_0,cru_str,content_txt_0,content_zuhe
	
	
	
	
def main():		
	filename = 'fushi'
	
	
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
	
	content_url_list = [url.strip() for url in open("url_%s.txt"%filename)]	
	
	for index,k in enumerate(content_url_list):
		content_str = ''
		content_txt = ''
		title = ''
		crumb = ''
		try:
			url = k
			r = requests.get('http://www.wed114.cn'+url,headers=HeaderData.get_header(),timeout=60)
			max_page = get_max_page(r.content)
			if max_page == 0:			
				#如果是404页面，直接跳过
				if '404' in BeautifulSoup(r.content,"lxml").find('title').get_text():
					continue
				else:				
					s = BeautifulSoup(r.content,"lxml")			
					title = s.find('h1').get_text()
					crumb = s.find('div',attrs={"class":"position"}).find_all('a')
					cru_str = ''
					for cru in crumb:
						cru_str = cru_str + cru.get_text()+'>'					
					content_str = s.find('div',attrs={"class":"substance"})				
					content_txt = str(s.find('div',attrs={"class":"substance"}).get_text()[0:150]).decode('utf-8')	
					content_str = clear_html(content_str)
			else:
				title,cru_str,content_txt,content_str = get_content(url,max_page)			
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
			sheet.write(index+1,8,cru_str.decode('utf-8'))			
			wb.save("result_%s.xls"%filename)		
		except Exception,e:
			print e
		print index
		# if index == 10:
			# break
		
if __name__ == '__main__':
	main()
