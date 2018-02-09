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
	desc = date+city+u'天气预报：'+type+'，'+u'空气指数：%s'%aqi+'，'+u'温度：'+high+'，'+low+'，'+u'风向/风力：'+fengxiang+fengli+'，'+ganmao
	return desc
def  main():
	#登陆微信
	itchat.auto_login(hotReload=True)
	user_content = itchat.search_friends(name=u'雨一直下')
	userName = user_content[0]['UserName']
	itchat.send(getWeather(101230201),toUserName = userName)#厦门
	itchat.send(getWeather(101010100),toUserName = userName)#北京
	

if __name__ == "__main__":
	while(1):
		main()
		time.sleep(60)
		
		
		
'''
#coding:utf-8
import itchat,json,time
import requests,sys
reload(sys) 
sys.setdefaultencoding('utf8')

#http://yhq.techseo.cn/yhq/?r=l&kw=%E7%94%B7%E7%9A%AE%E9%9E%8B


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
 #   print(msg['Text'])
	url = 'http://yhq.techseo.cn/yhq/?r=l&kw=' + 'iphone' #msg['Text']
	short_url_api = 'http://tools.aeink.com/tools/dwz/urldwz.php?longurl=%s'%url
	r = requests.get(short_url_api)
	j_data = json.loads(r.content)
	
	print j_data['ae_url']
	

def  main():
	itchat.auto_login(hotReload=True)
	itchat.run()
	
	

if __name__ == "__main__":
	short_url_api = 'http://tools.aeink.com/tools/dwz/urldwz.php?longurl=%s'%('http://yhq.techseo.cn/yhq/?r=l&kw=iphone')
	r = requests.get(short_url_api)
	j_data = json.loads(r.content)	
	print j_data['ae_url']

	

'''
