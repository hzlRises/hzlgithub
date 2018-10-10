#coding:utf-8
import requests,time,json,datetime
def get_header():
	headers = {
	
	}
	return headers	
	
	
def reply(nowtime):
	url = ''
	data = {
	"message":"upupupupupupupupupupupupupupup",
	"posttime":"%s"%int(time.time()),
	"formhash":"72e1e0e3",
	"usesig":"1",
	"subject":"",
	
	}
	r = requests.post(url,headers=get_header(),data=data,timeout=60)
	if '164267' in r.content:
		print 'success'
	else:
		print 'error'
	with open('log',r'a+') as my:
		my.write(nowtime+r.content+'\n')	
	
def main():	
	while True:
		time.sleep(1)
		current_time = time.localtime(time.time())	
		nowtime = time.strftime('%Y-%m-%d %H:%M:%S',current_time)
		print nowtime
		bool = (current_time.tm_hour >=9) and  (current_time.tm_hour <=21) and (current_time.tm_min ==0) and (current_time.tm_sec == 0)
		if bool:
			reply(nowtime)	
		
	
if __name__ == '__main__':
	main()
	
	
	
'''

'''
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
