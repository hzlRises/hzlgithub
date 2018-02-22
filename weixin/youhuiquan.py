#coding:utf-8
import itchat,json,time
import requests,sys
import urllib
reload(sys) 
sys.setdefaultencoding('utf-8')

@itchat.msg_register(itchat.content.TEXT)
# 注册消息响应事件，消息类型为itchat.content.TEXT，即文本消息
def text_reply(msg):
	print msg['Text']#unicode
#	msg['Text'].encode("utf-8")  unicode转为 str
#	print urllib.quote(msg['Text'].encode("utf-8"))	
	url = 'http://yhq.techseo.cn/yhq/?r=l&kw=%s'%(urllib.quote(msg['Text'].encode("utf-8")))	
	print url
	message = u'一一一一导 购 信 息一一一一\n已为您找到:%s\n点击下方链接查看\n%s'%(msg['Text'],url)
	itchat.send(message,msg.fromUserName)
#	return url


#处理群消息
@itchat.msg_register([itchat.content.TEXT, itchat.content.SHARING], isGroupChat=True)
def group_reply_text(msg):
	chatroom_id = msg['FromUserName']
	username = msg['ActualNickName']
	
	if chatroom_id == '@@a3f3bfafe461ecb368a6c602e42d1cb6f4a26fca1fff90215a69653298af31b5' and msg['Type'] == itchat.content.TEXT:
		url = 'http://yhq.techseo.cn/yhq/?r=l&kw=%s'%(urllib.quote(msg['Text'].encode("utf-8")))
		itchat.send(u'一一一一导 购 信 息一一一一\n已为您找到:%s\n点击下方链接查看\n%s'%(msg['Text'],url),'@@a3f3bfafe461ecb368a6c602e42d1cb6f4a26fca1fff90215a69653298af31b5')

		
# 处理好友添加请求
@itchat.msg_register(itchat.content.FRIENDS)
def add_friend(msg):
    # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.add_friend(**msg['Text'])
    # 加完好友后，给好友打个招呼
    itchat.send_msg('你好，我是优惠券机器人，想找什么优惠券直接发给我，我帮你找！', msg['RecommendInfo']['UserName'])
		
		
		
		
def  main():
	itchat.auto_login(hotReload=True)
	itchat.run()
#itchat.send('Hello, filehelper', toUserName='filehelper')
	
if __name__ == "__main__":
	main()
	
