#coding:utf-8
import requests,sys,re,pycurl,StringIO,time,xlrd,xlwt,HeaderData,md5,json
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver
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
	sheet.write(0,7,'md5_id')
	sheet.write(0,8,'title')
	sheet.write(0,9,'description')
	sheet.write(0,10,'content')
			
	content_url_list = [url.strip() for url in open('jrhelp.jd.com_index_detail_url.txt')]
	#https://article.jd.com/?id=987009
	
	
	service_args = []
	service_args.append('--load-images=no')  #关闭图片加载
	service_args.append('--disk-cache=yes')  #开启缓存
	service_args.append('--ignore-ssl-errors=true') #忽略https错误
	
	browser = webdriver.PhantomJS(service_args=service_args)
	
	browser.implicitly_wait(30)        #设置超时时间
	browser.set_page_load_timeout(30)  #设置超时时间
	
	for index,k in enumerate(content_url_list):	
		content_str = ''
		try:
			url = 'https://article.jd.com/?id='+str(k.strip())#获取文件中的url，具体根据txt里字段定
			print index,url
		except Exception,e:
			print e
		
		#抓正文规则
		try:
			#browser = webdriver.PhantomJS(executable_path=r'D:\programfiles\anaconda\Lib\site-packages\selenium\webdriver\phantomjs\bin\phantomjs.exe')
			browser.get(url)

			content_main = browser.find_element_by_class_name("detail_cont_main").get_attribute('innerHTML')
			s = BeautifulSoup(content_main,"lxml")			
			
			#删除商品部分，type=3, 删除头部标题部分
			content = [soup.extract() for soup in s('div',attrs={"class":"detail_cm_item detail_cm_goods"})]
			content = [soup.extract() for soup in s('div',attrs={"class":"detail_cm_head"})]
			
			
			
			#因为懒加载，导致img的src值不是图片的url地址，需要处理
			imatag = s.find_all('img')
			for itag in imatag:
				if '1x1'in itag.get('src'):
					itag['src'] = itag.get('data-lazy-img')
					itag['data-lazy-img'] = 'done'
			
			
			
			content_txt = str(s.get_text()).decode('utf-8')[0:250]#
			
			#替换掉不需要的标签
			s = str(s).replace('<html>','').replace('</html>','').replace('<body>','').replace('</body>','')
				
			title = browser.find_element_by_tag_name("h3").text
			'''
			txttag = browser.find_elements_by_class_name("detail_cm_text")#加个s
			pictag = browser.find_elements_by_class_name("detail_cm_pic")#加个s
			
			for t in txttag:
				content_str +=  '</p>'+t.text+'</p>'		
				
			for pic in pictag:
				print pic.get_attribute('innerHTML')
			'''
		
			
			
			m1 = md5.new()
			m1.update(title)			
			md5_str = m1.hexdigest()[8:-8]#取中间16位
			
			
			content = s.decode('utf-8')
			
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
				
			if len(content) < 32767:
				sheet.write(index+1,10,content)
			else:
				sheet.write(index+1,10,'String longer than 32767 characters')
			wb.save("result.xls")
			
			
			
		except Exception,e:
			print e
		print index
			
		time.sleep(0.1)		
	browser.quit()
if __name__ == '__main__':
	main()
