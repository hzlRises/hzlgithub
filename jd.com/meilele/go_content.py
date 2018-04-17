#coding:utf-8
import requests,sys,re,pycurl,StringIO,time,xlrd,xlwt,HeaderData,md5,json
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver
reload(sys) 
sys.setdefaultencoding('utf-8')

filename = 'article_cat-1'

categoryID = '000'


def get_title_md5(title):
	m1 = md5.new()
	m1.update(title)			
	md5_str = m1.hexdigest()[8:-8]#取中间16位
	
	return md5_str	
	
	
	
def clear_html(content_str):
	content_str = str(content_str)	
	
	content_str = re.sub(r'<div[\s\S]*?>','',content_str)
	content_str = re.sub(r'<p[\s\S]*?>','<p>',content_str)
	content_str = re.sub(r'<strong[\s\S]*?>','<strong>',content_str)
	content_str = re.sub(r'<span[\s\S]*?>','<span>',content_str)
	content_str = re.sub(r'<table[\s\S]*?>','<table>',content_str)
	content_str = re.sub(r'<tbody[\s\S]*?>','<tbody>',content_str)
	content_str = re.sub(r'<tr[\s\S]*?>','<tr>',content_str)
	content_str = re.sub(r'<th[\s\S]*?>','<th>',content_str)
	content_str = re.sub(r'<td[\s\S]*?>','<td>',content_str)
	content_str = re.sub(r'<font[\s\S]*?>','<font>',content_str)	
	
	
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
	
	#正文内嵌a标签加粗样式	
	content_str = content_str.replace('<strong class="autolink">','')
	content_str = content_str.replace('</strong>','')
	
	#如果不清除这个strong，正文会全部加粗
	content_str = content_str.replace('<strong>','')
	
	#清除推荐阅读以及之后的字符
	content_str = re.sub(r'推荐阅读[\s\S]*','',content_str)	
	content_str = re.sub(r'更多精彩推荐[\s\S]*','',content_str)	
	content_str = re.sub(r'阅读推荐[\s\S]*','',content_str)	
	content_str = re.sub(r'美文赏析[\s\S]*','',content_str)	
	content_str = re.sub(r'热门搜索[\s\S]*','',content_str)	
	content_str = re.sub(r'文章来源[\s\S]*','',content_str)	
	content_str = re.sub(r'相关文章[\s\S]*','',content_str)	
	content_str = re.sub(r'猜你喜欢[\s\S]*','',content_str)	
	content_str = re.sub(r'更多相关推荐[\s\S]*','',content_str)	
	content_str = re.sub(r'文章来源[\s\S]*','',content_str)		
	content_str = re.sub(r'更多精彩内容请点击下方链接[\s\S]*','',content_str)		
	content_str = re.sub(r'猜您还喜欢[\s\S]*','',content_str)		
	content_str = re.sub(r'总结[\s\S]*','',content_str)		
	content_str = re.sub(r'结语[\s\S]*','',content_str)		
	content_str = re.sub(r'更多资讯请点击[\s\S]*','',content_str)		
	
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

	return content_str
	
	
	
def get_tag(title):	
	tag = ''
	url = 'http://custom.p-search.jd.local/?pagesize=1&qp_disable=no&client=&key=%s'%urllib.quote(title.encode('gbk'))
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
	sheet.write(0,11,'origin_url')
	
	
	content_url_list = [url.strip() for url in open('%s_detail_url.txt'%filename)]
	
	
	for index,k in enumerate(content_url_list):	
		content_str = ''
		content_txt = ''
		try:
			url = 'http://www.meilele.com'+k.strip()#获取文件中的url，具体根据txt里字段定			
		except Exception,e:
			print e
		
		#抓正文规则
		try:
			r = requests.get(url,headers=HeaderData.get_header(),timeout=60)	
			s = BeautifulSoup(r.content,"lxml")
			title = s.find('title').get_text()#.split('_')[0]#.decode('utf-8')
			
			#因为懒加载，导致img的src值不是图片的url地址，需要处理			
			imatag = s.find_all('img')
			for itag in imatag:
				if 'blank.gif'in itag.get('src'):
					itag['src'] = itag.get('data-src')	
					
			content_str = s.find('div',attrs={"class":"content"})#.get_text()			
			#清除正文里的商品模块
			bb = [soup.extract() for soup in s('div',attrs={"class":"pc-box"})]		
			content_txt = str(content_str.get_text()).decode('utf-8')[0:250]
			
			content_str = clear_html(content_str)
			
			sheet.write(index+1,0,categoryID)#categoryID帮助中心
			sheet.write(index+1,1,'1')#status未审核
			sheet.write(index+1,2,'1')#recommend未推荐
			sheet.write(index+1,3,'0')#type运营添加
			sheet.write(index+1,4,get_tag(title))#tag标签
			sheet.write(index+1,5,'jd')#文章来源
			sheet.write(index+1,6,'jd')#作者
			sheet.write(index+1,7,get_title_md5(title))
			sheet.write(index+1,8,title)
			sheet.write(index+1,9,content_txt)
			if len(content_str) < 32767:
				sheet.write(index+1,10,content_str.decode('utf-8'))
			else:
				sheet.write(index+1,10,'String longer than 32767 characters')
				
			sheet.write(index+1,11,k.strip())
			wb.save("result_%s.xls"%filename)	
				
		except Exception,e:
			print e
		print index,k.strip()		

if __name__ == '__main__':
	main()
