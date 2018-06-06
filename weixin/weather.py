#coding:utf-8
import itchat,time,fund
from PIL import Image
from selenium import webdriver
from urllib import quote
import sys
reload(sys)
sys.setdefaultencoding('utf-8')	

def save_jpg():
	city_list = ['xiamentianqi','beijingtianqi']
	for index,city in enumerate(city_list):
		time.sleep(1)
		encode_city = quote(city)
		url = 'https://www.baidu.com/s?ie=UTF-8&wd=%s'%encode_city	
		picName = '%s.png'%index		
		browser = webdriver.PhantomJS(executable_path=r'D:\programfiles\anaconda\Lib\site-packages\selenium\webdriver\phantomjs\bin\phantomjs.exe')
		browser.get(url)
		browser.maximize_window()
		browser.save_screenshot(picName)#保存截图		
		
		#获取天气模板的位置、尺寸大小
		imgelement = browser.find_element_by_xpath('//*[@id="1"]')
		location = imgelement.location#获取天气x,y轴坐标
		size = imgelement.size#获取天气的长宽
		
		rangle = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']-20))
		i = Image.open(picName)	#打开0.png
		tinaqi = i.crop(rangle)#使用Image的crop函数，从截图中再次截取我们需要的		
		tinaqi.save('send_%s.png'%index)		
		browser.close()	
		
		
		#发送
		user_content = itchat.search_friends(name=u'雨一直下')
		userName = user_content[0]['UserName']
		itchat.send_image('send_%s.png'%index,toUserName = userName)
		
		if city == 'xiamentianqi':
			user_content_baby = itchat.search_friends(name=u'徐莹')
			userName_baby = user_content_baby[0]['UserName']
			itchat.send_image('send_%s.png'%index,toUserName = userName_baby)
	
def main():
	itchat.auto_login(hotReload=True)
	while True:
		time.sleep(1)		
		current_time = time.localtime(time.time())
		print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))		
		# get_fund()
		# break		
		if ((current_time.tm_hour == 7) and (current_time.tm_min) == 0 and (current_time.tm_sec == 0)):
			save_jpg()
		if(((current_time.tm_hour == 14) and (current_time.tm_min) == 30 and (current_time.tm_sec == 0))):
			fund.get_fund()
			
			


if __name__ == '__main__':
	main()

