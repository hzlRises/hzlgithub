#coding:utf-8
import requests
import xml.dom.minidom
from xml.etree import ElementTree as ET
import smtplib
from email.mime.text import MIMEText
from email.header import Header
mail_port = 25
mail_host = 'smtp.163.com'

mail_user = '..'

mail_pass = '..'

mail_to = '..'

cityId = 101010100#北京

def getTag(xmlFile):
	#城市
	city = xmlFile.getElementsByTagName('city')
	city = city[0]
#	print city.firstChild.data
	#更新时间
	updatetime = xmlFile.getElementsByTagName('updatetime')
	updatetime = updatetime[0]
#	print updatetime.firstChild.data
	
	#温度
	wendu = xmlFile.getElementsByTagName('wendu')
	wendu = wendu[0]
#	print wendu.firstChild.data
	
	#风力
	fengli = xmlFile.getElementsByTagName('fengli')
	fengli = fengli[0]
#	print fengli.firstChild.data
	
	#湿度
	shidu = xmlFile.getElementsByTagName('shidu')
	shidu = shidu[0]
#	print shidu.firstChild.data
	
	#风向
	fengxiang = xmlFile.getElementsByTagName('fengxiang')
	fengxiang = fengxiang[0]
#	print fengxiang.firstChild.data
	
	#日出
	sunrise = xmlFile.getElementsByTagName('sunrise_1')
	sunrise = sunrise[0]
#	print sunrise.firstChild.data
	
	#日落
	sunset = xmlFile.getElementsByTagName('sunset_1')
	sunset = sunset[0]
#	print sunset.firstChild.data

#	result = '\n'.join(city.firstChild.data,updatetime.firstChild.data,wendu.firstChild.data,fengli.firstChild.data,shidu.firstChild.data,fengxiang.firstChild.data,sunrise.firstChild.data,sunset.firstChild.data)
#	sendMail(
#	u'城市'+city.firstChild.data+'\n'
#	u'更新时间'+updatetime.firstChild.data+'\n'
#	u'温度'+wendu.firstChild.data+'\n'
#	u'风力'+fengli.firstChild.data+'\n'
#	u'风向'+fengxiang.firstChild.data+'\n'
#	u'湿度'+shidu.firstChild.data+'\n'
#	u'日出'+sunrise.firstChild.data+'\n'
#	u'日落'+sunset.firstChild.data+'\n'
#	)
	return city.firstChild.data,updatetime.firstChild.data,wendu.firstChild.data,fengli.firstChild.data,fengxiang.firstChild.data,shidu.firstChild.data,sunrise.firstChild.data,sunset.firstChild.data
def getAqi():
	#空气质量指数
	aqi_list = []
	per = ET.parse('aa.xml')
	for opener in per.findall('./environment'):
		for child in opener.getchildren():
#			print child.tag,':',child.text
			aqi_list.append(child.text)
#	sendMail(
#	u'空气质量指数：'+aqi_list[0]+','+aqi_list[3]+'\n'
#	u'PM2.5指数：'+aqi_list[1]+'\n'
#	u'外出建议：'+aqi_list[2]
#	)
	return aqi_list[0],aqi_list[3],aqi_list[1],aqi_list[2]

def getForecast():
	#预报
	forecast_list = []
	per = ET.parse('aa.xml')
	for opener in per.findall('./forecast/weather'):
		for child in opener.getchildren():
#			print child.tag,':',child.text
			forecast_list.append(child.text)
			for grandson in child.getchildren():
#				print grandson.tag,':',grandson.text
				forecast_list.append(grandson.text)
	return tuple(forecast_list)
def getZhishu():
	#各种指数
	zhishu_list = []
	per = ET.parse('aa.xml')
	for opener in per.findall('./zhishus'):
		for child in opener.getchildren():
#			print child.tag,':',child.text
			zhishu_list.append(child.text)
			for grandson in child.getchildren():
#				print grandson.tag,':',grandson.text
				zhishu_list.append(grandson.text)
	return tuple(zhishu_list)		

def sendMail(content):
	msg = MIMEText(content,'html','utf-8')
	msg['Subject'] = Header(u'专属天气预报','utf-8')
	msg['From'] = u'亮仔'#mail_user
#	msg['To'] = ','.join(mail_to)
	msg['To'] = mail_to
	s = smtplib.SMTP()
	s.connect(mail_host,mail_port)
	s.login(mail_user, mail_pass)
	s.sendmail(mail_user,mail_to, msg.as_string())
	s.close()

if __name__ == "__main__":
	#http://wthrcdn.etouch.cn/weather_mini?citykey=101010100
	url = 'http://wthrcdn.etouch.cn/WeatherApi?citykey=%s'%cityId#xiamen101230201   bj101010100
	r = requests.get(url)
	with open('aa.xml',r'w') as my:
		my.write(str(r.content))
	domtree = xml.dom.minidom.parse('aa.xml')
	getTag(domtree)
	getAqi()
	getForecast()
	getZhishu()
	allContent_list = list(getTag(domtree)+getAqi()+getForecast()+getZhishu())
	sendMail(
	'\
	<table border="1" text-align:center;>\
		<tr style="background:#D5E9FA">\
			<td><strong>City:%s,Updatetime:%s,Wendu:%s</strong></td>\
		</tr>\
		<tr>\
			<td><strong>Fengli:%s,Fengxiang:%s</strong></td>\
		</tr>\
		<tr style="background:#D5E9FA">\
			<td><strong>Shidu:%s</strong></td>\
		</tr>\
		<tr>\
			<td><strong>Sunrise:%s,Sunset:%s</strong></td>\
		</tr>\
		<tr style="background:#D5E9FA">\
			<td><strong>Aqi:%s,Quality:%s,PM2.5:%s</strong></td>\
		</tr>\
		<tr>\
			<td><strong>Suggestion:%s</strong></td>\
		</tr>\
		<tr><td><table border="1">\
		<tr style="background:#D5E9FA">\
		<td>Date</td>\
		<td>Day</td>\
		<td>Night</td>\
		</tr>\
		<tr>\
			<td>%s,%s,%s</td>\
			<td>%s,%s,%s</td>\
			<td>%s,%s,%s</td>\
		</tr>\
		<tr>\
			<td>%s,%s,%s</td>\
			<td>%s,%s,%s</td>\
			<td>%s,%s,%s</td>\
		</tr>\
		<tr>\
			<td>%s,%s,%s</td>\
			<td>%s,%s,%s</td>\
			<td>%s,%s,%s</td>\
		</tr></table></td></tr>\
	<tr><td>\
	1 %s:%s,%s<br />\
	2 %s:%s,%s<br />\
	3 %s:%s,%s<br />\
	4 %s:%s,%s<br />\
	5 %s:%s,%s<br />\
	6 %s:%s,%s<br />\
	7 %s:%s,%s<br />\
	8 %s:%s,%s<br />\
	9 %s:%s,%s<br />\
	10 %s:%s,%s<br />\
	11 %s:%s,%s<br />\
	</td></tr>\
	</table>\
	'
	%(
	#head
	allContent_list[0],
	allContent_list[1],
	allContent_list[2],
	allContent_list[3],
	allContent_list[4],
	allContent_list[5],
	allContent_list[6],
	allContent_list[7],
	#environment
	allContent_list[8],
	allContent_list[9],
	allContent_list[10],
	allContent_list[11],
	
	#weather
	allContent_list[12],
	allContent_list[13],
	allContent_list[14],
	allContent_list[16],
	allContent_list[17],
	allContent_list[18],
	allContent_list[20],
	allContent_list[21],
	allContent_list[22],
	
	#weather
	allContent_list[23],
	allContent_list[24],
	allContent_list[25],
	allContent_list[27],
	allContent_list[28],
	allContent_list[29],
	allContent_list[31],
	allContent_list[32],
	allContent_list[33],
	
		#weather
	allContent_list[34],
	allContent_list[35],
	allContent_list[36],
	allContent_list[38],
	allContent_list[39],
	allContent_list[40],
	allContent_list[42],
	allContent_list[43],
	allContent_list[44],
	
	
	#晨练指数1
	allContent_list[68],
	allContent_list[69],
	allContent_list[70],
	#舒适度2
	allContent_list[72],
	allContent_list[73],
	allContent_list[74],

	#穿衣指数3
	allContent_list[76],
	allContent_list[77],
	allContent_list[78],
	
	#感冒指数4
	allContent_list[80],
	allContent_list[81],
	allContent_list[82],
	
	#晾晒指数5
	allContent_list[84],
	allContent_list[85],
	allContent_list[86],
	
	#旅游指数6
	allContent_list[88],
	allContent_list[89],
	allContent_list[90],
	
	#紫外线强度7
	allContent_list[92],
	allContent_list[93],
	allContent_list[94],
	
	#洗车指数
	allContent_list[96],
	allContent_list[97],
	allContent_list[98],
	
	#运动指数9
	allContent_list[100],
	allContent_list[101],
	allContent_list[102],
	
	#约会指数10
	allContent_list[104],
	allContent_list[105],
	allContent_list[106],
	
	#雨伞指数11
	allContent_list[108],
	allContent_list[109],
	allContent_list[110],
	)
	)
