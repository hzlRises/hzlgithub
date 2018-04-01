#coding:utf-8
import itchat,time
from PIL import Image
from selenium import webdriver
from urllib import quote
import sys
reload(sys)
sys.setdefaultencoding('utf-8')	

def save_jpg():
	city_list = ['beijingtianqi','chengdutianqi','handantianqi','xiamentianqi']		
	for index,city in enumerate(city_list):
		time.sleep(1)
		encode_city = quote(city)
		url = 'https://www.baidu.com/s?ie=UTF-8&wd=%s'%encode_city	
		picName = '%s.png'%index		
		browser = webdriver.PhantomJS()
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
		
		user_content_baby = itchat.search_friends(name=u'')
		userName_baby = user_content[0]['UserName']
		itchat.send_image('send_%s.png'%index,toUserName = userName_baby)
		

	
def main():
	itchat.auto_login(hotReload=True)
	while True:
		time.sleep(1)
		current_time = time.localtime(time.time())#
		if ((current_time.tm_hour == 7) and (current_time.tm_min) == 30 and (current_time.tm_sec == 0)):
			save_jpg()


if __name__ == '__main__':
	main()





'''
#coding:utf-8
import itchat,json,time
import requests,sys
reload(sys) 
sys.setdefaultencoding('utf8')

def getWeather(cs):
	url = 'http://wthrcdn.etouch.cn/weather_mini?citykey=%s'%cs
	r = requests.get(url)
	j_data = json.loads(r.content)
	for i in range(1):
		city = j_data["data"]["city"]
		aqi = j_data["data"]["aqi"]#空气质量指数
		ganmao = j_data["data"]["ganmao"]
		wendu = j_data["data"]["wendu"]

	for i in range(1):
		date = j_data["data"]["forecast"][i]["date"]
		high = j_data["data"]["forecast"][i]["high"]
		fengli = j_data["data"]["forecast"][i]["fengli"]
		
		low = j_data["data"]["forecast"][i]["low"]
		fengxiang = j_data["data"]["forecast"][i]["fengxiang"]
		type = j_data["data"]["forecast"][i]["type"]
		
	fengli = fengli.replace('<![CDATA[','').replace(']]>','')
	print city,aqi,ganmao,wendu,date,high,fengli,low,fengxiang,type
	desc = u'[愉快]宝贝早安[愉快]'+'\n'+u'【'+date+city+u'天气预报】'+type+'\n'+u'【空气指数】%s'%aqi+'\n'+u'【温度】'+u'实时%s℃，'%wendu+u'最'+high+'，'+u'最'+low+'\n'+u'【风向/风力】'+fengxiang+fengli+'\n'+u'【感冒指数】'+ganmao
	
	return desc
def  main():
	#登陆微信
	itchat.auto_login(hotReload=True)
	#发送天气预报
	while True:	
		time.sleep(1)
		current_time = time.localtime(time.time())
		print "sended weather forecast..."+str(current_time.tm_sec)
		if((current_time.tm_hour == 7) and (current_time.tm_min == 30) and (current_time.tm_sec == 0)):
		#if current_time.tm_sec == 1:		
			#给自己发
			user_content = itchat.search_friends(name=u'雨一直下')
			userName = user_content[0]['UserName']
			itchat.send(getWeather(000),toUserName = userName)#
			itchat.send(getWeather(000),toUserName = userName)#
	
			
			#给宝贝发
			user_content_baby = itchat.search_friends(name=u'')
			userName_baby = user_content_baby[0]['UserName']
			itchat.send(getWeather(0000),toUserName = userName_baby)#
			#itchat.send(getWeather(0000),toUserName = userName_baby)#
			

if __name__ == "__main__":
	main()



'''
	
