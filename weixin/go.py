#coding:utf-8
import itchat,json,time,requests,sys,urllib,os,re,weather
import jd
from PIL import Image
from selenium import webdriver
#hzl
reload(sys) 
sys.setdefaultencoding('utf-8')


#发送消息并且记录到log
def send_msg_(message):
	now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
	pass
	

@itchat.msg_register(itchat.content.TEXT)
# 注册消息响应事件，消息类型为itchat.content.TEXT，即文本消息

def text_reply(msg):
	message = ''
	key = ''
	print msg['Text']#unicode
	'''
	print type(msg['Text'])#unicode
	msg['Text'].encode("utf-8")  unicode转为 str
	print urllib.quote(msg['Text'].encode("utf-8"))	
	'''
	
	if 'jd.com' in msg['Text'] and 'item' in msg['Text']:
		sku_id = jd.getGoodsIdByUrl(msg['Text'])
		goods_name,price,fanli = jd.getProductInfo(sku_id)		
		click_url = jd.getFanliLink(sku_id)		
		message = u'一一一一返 利 信 息一一一一\n'+goods_name+'\n'+u'【商品原价】'+price+'元'+'\n'+u'【商品返利】'+fanli+'元'+'\n'+u'【返利链接】'+jd.getShortUrl(click_url)
	elif '帮助' in msg['Text']:
		message = '[愉快]【淘宝购物领券】假如你想买鼠标垫，请发送"找鼠标垫"给机器人，机器人会把找到的鼠标垫相关优惠券链接发给你，点进去复制淘口令，再打开淘宝/天猫APP就可以领到优惠券啦。\n[愉快]【京东购物返利】打开京东APP，找到自己想买的商品，点击右上角分享按钮，把商品分享给机器人，就可以看到返利链接啦，确认收货后发送【提现】，等待客服审核就可以啦。\n快试试吧...'
	#回复表情
	elif '[' in msg['Text'] and ']' in msg['Text']:
		message = u'[愉快]'
	elif '提现' in msg['Text']:
		#需要给主人发消息，先获得主人的id，以@符号开头
		user_content = itchat.search_friends(name = u'雨一直下')		
		userName = user_content[0]['UserName']		
		#获取提现申请人的昵称
		friend_content = itchat.search_friends(userName = msg.fromUserName)
		friend_name = friend_content['NickName']
		#给主人发消息提醒
		itchat.send( friend_name+u'申请提现',toUserName = userName)				
		#判断提现人性别
		if friend_content['Sex'] == 1:
			message = friend_name +u'帅哥请耐心等待，客服确认中'	
		elif friend_content['Sex'] == 0:
			message = friend_name +u'美女请耐心等待，客服确认中'
		else:
			message = friend_name +u'请耐心等待，客服确认中'			
	
	#活动页转链接
	elif 'hzlxy' in msg['Text']:
		link = msg['Text'].encode("utf-8").replace('hzlxy','')
		link = re.sub(r'\?.*','',link)
		r = requests.get(link)
		url = r.url
		duan_url = jd.getSelfCode(url)
		short_url = jd.getShortUrl(duan_url)		
		message = short_url	
	
	elif 'xmtq' in msg['Text'] or '天气预报' in msg['Text']:
		
		if 'xmtq' in msg['Text']:
			key = 'xmtq'
		else:
			key = 'beijingtianqi'
		weather_url = 'https://www.baidu.com/s?ie=UTF-8&wd=%s'%key
		browser = webdriver.PhantomJS(executable_path=r'D:\programfiles\anaconda\Lib\site-packages\selenium\webdriver\phantomjs\bin\phantomjs.exe')
		browser.get(weather_url)
		browser.maximize_window()
		browser.save_screenshot('send_auto_answes.png')#保存截图	
		
		#获取天气模板的位置、尺寸大小
		imgelement = browser.find_element_by_xpath('//*[@id="1"]')
		location = imgelement.location#获取天气x,y轴坐标
		size = imgelement.size#获取天气的长宽
		
		
		rangle = (int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']-20))
		i = Image.open('send_auto_answes.png')	#打开0.png
		tinaqi = i.crop(rangle)#使用Image的crop函数，从截图中再次截取我们需要的		
		tinaqi.save('send_auto_answes_0.png')		
		browser.close()	
		
		itchat.send_image('send_auto_answes_0.png',msg.fromUserName)
		
		'''
		user_content = itchat.search_friends(name=u'雨一直下')
		userName = user_content[0]['UserName']
		itchat.send_image('send_%s.png'%index,toUserName = userName)		
		'''
		
		
	elif '我的基金' in msg['Text']:
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
			'''
			if fund_id == '002121':
				imgelement = browser.find_element_by_xpath('//*[@id="2"]')
			'''
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
			
			'''
			if fund_id in ['070032','217027','165312','519066','110022']:
				user_content_baby = itchat.search_friends(name=u'徐莹')
				userName_baby = user_content_baby[0]['UserName']
				itchat.send_image('send_fund_%s.png'%index,toUserName = userName_baby)					
			'''
	elif '找' in msg['Text']:
		msg['Text'] = msg['Text'].replace('找','')
		url = 'http://techseo.cn/yhq/?r=l&kw=%s'%(urllib.quote(msg['Text'].encode("utf-8")))
		message = u'一一一一导 购 信 息一一一一\n已为您找到：%s\n点击下方链接查看\n%s\n-----------\n发送【帮助】查看使用机器人流程\n更多大额神券商品点击下方链接：\nhttp://t.cn/RYaBrUa'%(msg['Text'],jd.getShortUrl(url))

	else:
		#url = 'http://techseo.cn/yhq/?r=l&kw=%s'%(urllib.quote(msg['Text'].encode("utf-8")))
		#message = u'一一一一导 购 信 息一一一一\n已为您找到:%s\n点击下方链接查看\n%s\n-----------\n发送【帮助】查看使用机器人流程\n更多大额神券商品点击下方链接：\nhttp://t.cn/RYaBrUa'%(msg['Text'],jd.getShortUrl(url))
		#message = '您输入的指令有误，请发送【帮助】查看教程'
		pass
	# if message:
		# print message
	itchat.send(message,msg.fromUserName)
	
	#记录
	now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
	with open('log.txt',r'a+') as my:
		my.write('TEXT,'+itchat.search_friends(userName = msg.fromUserName)['NickName']+','+msg['Text']+','+now+'\n')
#	return url


#处理分享消息,获取分享信息里的链接
@itchat.msg_register(itchat.content.SHARING)
def sharing_reply(msg):
	#print msg['Url']#['url']
	if 'jd.com' in msg['Url'] and 'item' in msg['Url']:
		try:			
			sku_id = jd.getGoodsIdByUrl(msg['Url'])			
			goods_name,price,fanli = jd.getProductInfo(sku_id)		
			click_url = jd.getFanliLink(sku_id)
			message = u'一一一一返 利 信 息一一一一\n'+goods_name+'\n'+u'【商品原价】'+price+'元'+'\n'+u'【商品返利】'+fanli+'元'+'\n'+u'【返利链接】'+jd.getShortUrl(click_url)
		except Exception,e:
			message = u'此商品暂时无返利。'	
	else:
		message = u'请您确定是从京东APP的商品详情页分享的链接哦。'
	itchat.send(message,msg.fromUserName)
	now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
	with open('log.txt',r'a+') as my:
		my.write('SHARING,'+itchat.search_friends(userName = msg.fromUserName)['NickName']+','+msg['Url']+','+now+'\n')

'''
#处理群消息
@itchat.msg_register([itchat.content.TEXT, itchat.content.SHARING], isGroupChat=True)
def group_reply_text(msg):
	chatroom_id = msg['FromUserName']
	username = msg['ActualNickName']
	#print username,chatroom_id
	
	if chatroom_id == '@@be5e2eb0246421f5deb6298faa715e046dc4b30a879566d3b233bf7cecb8c343' and msg['Type'] == itchat.content.TEXT:
		url = 'http://yhq.techseo.cn/yhq/?r=l&kw=%s'%(urllib.quote(msg['Text'].encode("utf-8")))
		
		itchat.send(u'一一一一导 购 信 息一一一一\n已为您找到:%s\n点击下方链接查看\n%s'%(msg['Text'],url),'@@a3f3bfafe461ecb368a6c602e42d1cb6f4a26fca1fff90215a69653298af31b5')
'''	
# 处理好友添加请求
@itchat.msg_register(itchat.content.FRIENDS)
def add_friend(msg):
    # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.add_friend(**msg['Text'])
    # 加完好友后，给好友打个招呼
    itchat.send_msg('[愉快]你好，我是网购优惠券、返利机器人，\n发送【帮助】查看使用机器人流程。', msg['RecommendInfo']['UserName'])
	
		

def  main():	
	#登陆微信
	itchat.auto_login(hotReload=True)
	itchat.run()

#itchat.send('Hello, filehelper', toUserName='filehelper')
	
if __name__ == "__main__":
	main()
