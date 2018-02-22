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
import urllib
reload(sys) 
sys.setdefaultencoding('utf8')


@itchat.msg_register(itchat.content.TEXT)

# 注册消息响应事件，消息类型为itchat.content.TEXT，即文本消息
def text_reply(msg):
	url = 'http://yhq.techseo.cn/yhq/?r=l&kw=%s'%(urllib.quote(msg['Text']))	
	print url
	itchat.send(url,msg.fromUserName)

# 处理好友添加请求
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.add_friend(**msg['Text']) 
    # 加完好友后，给好友打个招呼
    itchat.send_msg(u'你好，我是机器人', msg['RecommendInfo']['UserName'])


	

def  main():
	itchat.auto_login(hotReload=True)
	itchat.run()
#itchat.send('Hello, filehelper', toUserName='filehelper')
	

if __name__ == "__main__":
	main()
	
	

'''
