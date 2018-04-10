#coding:utf-8
import requests,sys,re,pycurl,StringIO,time,xlrd,xlwt,HeaderData
from bs4 import BeautifulSoup
reload(sys) 
sys.setdefaultencoding('utf8')

def main():	
	wb = xlwt.Workbook()
	sheet = wb.add_sheet('sheet1')
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
			
			print type(title),type(content_str)
			sheet.write(index,0,title)
			sheet.write(index,1,content_str)
			
			
			'''
			content = [soup.extract() for soup in s('img')]#删除文章里的img标签
			content = [soup.extract() for soup in s('a')]#删除文章里的img标签
			content = str(s.find('td')).replace('<td>','').replace('</td>','').replace('div','p')#替换掉td和div	
			'''	
		except Exception,e:
			print e
			
		time.sleep(0.1)
		wb.save("result.xls")
		
	
if __name__ == '__main__':
	main()
