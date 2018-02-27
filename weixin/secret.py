#coding:utf-8
import time
def getSecret():
	payloads = {
	'app_key':'666',
	'app_secret':'666',
	'union_id':666,
	'site_id':666,
	'tuiguang_id':666,#推广位名称:weixinbot
	'pid':'666',
	'redirect_uri':'http666techseo.cn/',
	'state':'666',
	'code':'666',
	'access_token':'666-ab6d-4eef-b610-4fc35385fb5b',
	'client_id':'666',
	'now':'%s'%time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),
	}
	# for k,v in payloads.iteritems():
		# print k,v
	return payloads
def main():
	getSecret()	
	pass
if __name__ == '__main__':
	main()
