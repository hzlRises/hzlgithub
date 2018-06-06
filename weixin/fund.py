#coding:utf-8
import itchat,sys
from PIL import Image
from selenium import webdriver
reload(sys)
sys.setdefaultencoding('utf-8')
def get_fund():
	'''
	162605景顺长城鼎益混合(LOF)
	160505博时主题行业混合(LOF)
	002121广发沪港深新起点股票
	000011华夏大盘精选混合
	163402兴全趋势投资混合(LOF)
	070032
	217027
	165312
	519066
	110022	
	'''	
	itchat.auto_login(hotReload=True)
	fund_list = ['162605','160505','002121','000011','163402','070032','217027','165312','519066','110022']	
	
	for index,fund in enumerate(fund_list):
		fund_id = str(fund)		
		#url = 'https://www.baidu.com/s?ie=UTF-8&wd=%s'%str(fund_id)		
		url = 'http://fund.eastmoney.com/%s.html'%str(fund_id)		
		picName = 'fund_%s.png'%index
		browser = webdriver.PhantomJS(executable_path=r'D:\programfiles\anaconda\Lib\site-packages\selenium\webdriver\phantomjs\bin\phantomjs.exe')
		browser.get(url)
		browser.maximize_window()
		browser.save_screenshot(picName)#保存截图	
		
		
		imgelement = browser.find_element_by_xpath('//*[@id="body"]/div[14]/div/div/div[1]')
	
		location = imgelement.location#获取x,y轴坐标
		size = imgelement.size#获取长宽
		
		rangle = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']-20))
		i = Image.open(picName)	#打开
		tinaqi = i.crop(rangle)#使用Image的crop函数，从截图中再次截取我们需要的		
		tinaqi.save('send_fund_%s.png'%index)		
		browser.close()	
		
		
		#发送
		user_content = itchat.search_friends(name=u'雨一直下')
		userName = user_content[0]['UserName']
		itchat.send_image('send_fund_%s.png'%index,toUserName = userName)
		
		
		if fund_id in ['070032','217027','165312','519066','110022']:
			user_content_baby = itchat.search_friends(name=u'徐莹')
			userName_baby = user_content_baby[0]['UserName']
			itchat.send_image('send_fund_%s.png'%index,toUserName = userName_baby)		
		

def main():
	get_fund()


if __name__ == '__main__':
	main()
