#coding:utf-8
import itchat,json,time,requests,sys,urllib
import jd
#hzl
reload(sys) 
sys.setdefaultencoding('utf-8')

@itchat.msg_register(itchat.content.TEXT)
# 注册消息响应事件，消息类型为itchat.content.TEXT，即文本消息
def text_reply(msg):
	print msg['Text']#unicode
#	print type(msg['Text'])#unicode
#	msg['Text'].encode("utf-8")  unicode转为 str
#	print urllib.quote(msg['Text'].encode("utf-8"))	
	if 'jd.com' in msg['Text']:
		sku_id = jd.getGoodsIdByUrl(msg['Text'])
		goods_name,price,fanli = jd.getProductInfo(sku_id)
		
		click_url = jd.getFanliLink(sku_id)		
		print click_url
		message = u'一一一一返 利 信 息一一一一\n'+goods_name+'\n'+u'【商品原价】'+price+'元'+'\n'+u'【商品返利】'+fanli+'元'+'\n'+u'【返利链接】'+jd.getShortUrl(click_url)
	elif '帮助' in msg['Text']:
		message = '[愉快]【在淘宝购物前领券】假如你想买鼠标垫，直接把鼠标垫三个字发给机器人，机器人会把找到的鼠标垫相关商品链接发给你，点进去复制淘口令，再打开淘宝/天猫APP就可以领到优惠券啦。\n[愉快]【在京东购物】打开京东APP，找到自己想买的商品，点击右上角分享按钮，把商品链接复制，发给我就可以看到返利链接啦，确认收货后发送【提现】，等待客服审核就可以啦。\n快试试吧...'
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
			message = friend_name +u'帅哥，请耐心等待哦，由于人数较多，客服火速确认中呢...'		
		elif friend_content['Sex'] == 0:
			message = friend_name +u'美女，请耐心等待哦，由于人数较多，客服火速确认中呢...'
		else:
			message = friend_name +u'请耐心等待哦，由于人数较多，客服火速确认中呢...'
			
			
	else:
		url = 'http://yhq.techseo.cn/yhq/?r=l&kw=%s'%(urllib.quote(msg['Text'].encode("utf-8")))
		message = u'一一一一导 购 信 息一一一一\n已为您找到:%s\n点击下方链接查看\n%s\n-----------\n发送【帮助】查看使用机器人流程\n更多大额神券商品点击下方链接：\nhttp://t.cn/RTzLM6g'%(msg['Text'],jd.getShortUrl(url))

	print message
	itchat.send(message,msg.fromUserName)
	
	#记录
	now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
	with open('log.txt',r'a+') as my:
		my.write(itchat.search_friends(userName = msg.fromUserName)['NickName']+','+msg['Text']+','+now+'\n')
#	return url


#处理分享消息,获取分享信息里的链接
@itchat.msg_register(itchat.content.SHARING)
def sharing_reply(msg):
	#print msg['Url']#['url']
	if 'jd.com' in msg['Url']:
		sku_id = jd.getGoodsIdByUrl(msg['Url'])
		goods_name,price,fanli = jd.getProductInfo(sku_id)		
		click_url = jd.getFanliLink(sku_id)		
		message = u'一一一一返 利 信 息一一一一\n'+goods_name+'\n'+u'【商品原价】'+price+'元'+'\n'+u'【商品返利】'+fanli+'元'+'\n'+u'【返利链接】'+jd.getShortUrl(click_url)
	else:
		message = u'请确定您是从京东APP分享的链接哦。'
	itchat.send(message,msg.fromUserName)
	now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
	with open('log.txt',r'a+') as my:
		my.write(itchat.search_friends(userName = msg.fromUserName)['NickName']+','+msg['Url']+','+now+'\n')

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
    itchat.send_msg('[愉快]你好，我是微信自动回复消息机器人\n[抠鼻]想在淘宝/天猫买东西？直接把关键词发给我，机器人帮你找相关商品优惠券。\n[抠鼻]想在京东买东西？把链接发给我，机器人给你发返利红包\n--------------\n发送【帮助】查看使用机器人流程。', msg['RecommendInfo']['UserName'])
	
		

def  main():
	itchat.auto_login(hotReload=True)
	itchat.run()
#itchat.send('Hello, filehelper', toUserName='filehelper')
	
if __name__ == "__main__":
	main()
