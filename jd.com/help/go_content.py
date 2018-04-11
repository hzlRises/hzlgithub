#coding:utf-8
import requests,sys,re,pycurl,StringIO,time,xlrd,xlwt,HeaderData,md5
from bs4 import BeautifulSoup
reload(sys) 
sys.setdefaultencoding('utf8')

def main():	
	wb = xlwt.Workbook()
	sheet = wb.add_sheet('sheet1')
	sheet.write(0,0,'categoryID')#categoryID帮助中心
	sheet.write(0,1,'status')#status未审核
	sheet.write(0,2,'recommend')#recommend未推荐
	sheet.write(0,3,'type')#type运营添加
	sheet.write(0,4,'tag')#tag标签
	sheet.write(0,5,'source')#文章来源
	sheet.write(0,6,'writer')#作者
	sheet.write(0,7,'md5_id')#摘要	
	sheet.write(0,8,'title')
	sheet.write(0,9,'description')
	sheet.write(0,10,'content')
			
	content_url_list = [url.strip() for url in open('help.jd.com_index_detail_url.txt')]
	for index,k in enumerate(content_url_list):			
		try:
			url = k#获取文件中的url，具体根据txt里字段定
			print index,url
		except Exception,e:
			print e
		
		#抓正文规则
		try:
			r = requests.get(url,headers=HeaderData.get_header(),timeout=60)
			s = BeautifulSoup(r.content,"lxml")
			
			title = str(s.find('div',attrs={"class":"help-tit1 flk06"}).get_text()).decode('utf-8')
			
			content = str(s.find('div',attrs={"class":"contxt"}))			
			content_str = re.sub('<div class="help-tit1 flk06">(.*?)</div>','',content).decode('utf-8')			
			
			s2 = BeautifulSoup(content_str,"lxml")#把content_str当做html再用BeautifulSoup解析一次
			
			#content_txt = str(s.find('div',attrs={"class":"contxt"}).get_text()).decode('utf-8')[0:250]#取前250个字符
			
			content_txt = s2.get_text()[0:250]#取前250个字符			
			
			
			m1 = md5.new()
			m1.update(title)
			
			md5_str = m1.hexdigest()[8:-8]#取中间16位
			
			
			sheet.write(index+1,0,'148')#categoryID帮助中心
			sheet.write(index+1,1,'1')#status未审核
			sheet.write(index+1,2,'1')#recommend未推荐
			sheet.write(index+1,3,'0')#type运营添加
			sheet.write(index+1,4,'jd')#tag标签
			sheet.write(index+1,5,'jd')#文章来源
			sheet.write(index+1,6,'jd')#作者
			sheet.write(index+1,7,md5_str)
			sheet.write(index+1,8,title)
			if content_txt:
				sheet.write(index+1,9,content_txt)
			else:
				sheet.write(index+1,9,title)
			if len(content_str) < 32767:
				sheet.write(index+1,10,content_str)
			else:
				sheet.write(index+1,10,'String longer than 32767 characters')
			wb.save("result.xls")
			continue
			
			'''
			content = [soup.extract() for soup in s('img')]#删除文章里的img标签
			content = [soup.extract() for soup in s('a')]#删除文章里的img标签
			content = str(s.find('td')).replace('<td>','').replace('</td>','').replace('div','p')#替换掉td和div	
			'''	
		except Exception,e:
			print e
			
			
		time.sleep(0.1)		
	
if __name__ == '__main__':
	main()
