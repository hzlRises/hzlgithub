#coding:utf-8
import time,md5,requests,json,sys,urllib
import secret
#hzl
reload(sys)
sys.setdefaultencoding("utf-8")
'''
获取access_token
https://auth.360buy.com/oauth/token?grant_type=authorization_code&client_id=5516FCE2AEB0F8D4143494099E0471B5&redirect_uri=http://techseo.cn/&code=o4Ry0I&state=quanyi&client_secret=a5addbe9dd9b43adab27d2071da09e9c
'''






#长链接转换为短链接
def getShortUrl(url):
	encode_url = urllib.quote(url)
	sina_url = 'http://api.t.sina.com.cn/short_url/shorten.json?source=3271760578&url_long=%s'%encode_url
	r_short = requests.get(sina_url)
	j_data = json.loads(r_short.content)
	return j_data[0]['url_short']
		


def getGoodsIdByUrl(url):
	#url = 'https://item.m.jd.com/product/12673813270.html?&utm_source=iosapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL'
	if 'item' in url:
		sku_id = url.split('/')[4].split('.')[0]	
		return sku_id
	'''
	else:		
		id_str_list = url.split('&')
		for i in id_str_list:			
			if 'id=' in i:				
				return i.split('=')[1]
			
	'''
#拼接sign 获取md5
def getSignAndMd5(keys,app_secret,params):
	#拼接sign
	md5_str = app_secret
	for key in keys:
		md5_str += key
		md5_str += params[key]
	md5_str += app_secret
	
	#md5计算
	m1 = md5.new()
	m1.update(md5_str)
	sign = m1.hexdigest()
	return sign
	
	
def getFanliLink(skuId):
	url = 'https://item.m.jd.com/product/%s.html'%skuId	
	params = {
	'access_token':'%s'%secret.getSecret()['access_token'],
	'app_key':'%s'%secret.getSecret()['app_key'],
	'method':'jingdong.service.promotion.batch.getcode',
	'timestamp':secret.getSecret()['now'],
	'v':'2.0',
	'id':'%s'%skuId,
	'url':'%s'%url,	
	'unionId':'%s'%secret.getSecret()['union_id'],
	'channel':'WL',
	'webId':'%s'%secret.getSecret()['site_id'],
	}	
	
	#参数排序
	keys = params.keys()
	keys.sort()
	#访问服务
	url = 'https://api.jd.com/routerjson?sign=%s'%getSignAndMd5(keys,secret.getSecret()['app_secret'],params)
	r = requests.get(url,params=params)
	skuinfo_result = json.loads(r.content)
	unicode_str = skuinfo_result['jingdong_service_promotion_batch_getcode_responce']['querybatch_result']
	unicode_result = json.loads(unicode_str)
	click_url = unicode_result['urlList'][0]['url']
	
	return click_url
	
	
def getProductInfo(sku_id):

	params = {
	'access_token':'%s'%secret.getSecret()['access_token'],
	'app_key':'%s'%secret.getSecret()['app_key'],
	'method':'jingdong.service.promotion.goodsInfo',
	'timestamp':secret.getSecret()['now'],
	'skuIds':'%s'%sku_id,
	'v':'2.0',
	}	
	
	#参数排序
	keys = params.keys()
	keys.sort()
	
	#访问服务
	url = 'https://api.jd.com/routerjson?sign=%s'%getSignAndMd5(keys,secret.getSecret()['app_secret'],params)
	r = requests.get(url,params=params)	
	skuinfo_result = json.loads(r.content)
	unicode_str = skuinfo_result['jingdong_service_promotion_goodsInfo_responce']['getpromotioninfo_result']
	unicode_result = json.loads(unicode_str)	
	goodsName = unicode_result['result'][0]['goodsName']#商品名称
	unitPrice = unicode_result['result'][0]['unitPrice']#商品价格
	commisionRatioPc = unicode_result['result'][0]['commisionRatioPc']#佣金比例	
	#返给用户的钱
	fanli = round(unitPrice*commisionRatioPc/100*0.3,2)	
	'''
	for k,v in unicode_result['result'][0].iteritems():
		if k == 'goodsName':
			print v
		if k == 'commisionRatioPc':
			print v
		if k == 'unitPrice':
			print v
		
	
	'''
	return goodsName.encode('utf-8'),str(unitPrice),str(fanli)
	
	
	
def getSelfCode(url):
	params = {
	'access_token':'%s'%secret.getSecret()['access_token'],
	'app_key':'%s'%secret.getSecret()['app_key'],
	'method':'jingdong.service.promotion.getcode',
	'timestamp':secret.getSecret()['now'],	
	'v':'2.0',
	'promotionType':'7',
	'materialId':'%s'%url,
	'unionId':'%s'%secret.getSecret()['union_id'],
	'channel':'WL',
	'webId':'%s'%secret.getSecret()['site_id'],
	'adttype':'6',
	}	
	
	#参数排序
	keys = params.keys()
	keys.sort()
	
	#访问服务
	url = 'https://api.jd.com/routerjson?sign=%s'%getSignAndMd5(keys,secret.getSecret()['app_secret'],params)
	r = requests.get(url,params=params)	
	result_ = json.loads(r.content)
	unicode_str = result_['jingdong_service_promotion_getcode_responce']['queryjs_result']
	unicode_result = json.loads(unicode_str)
	click_url = unicode_result['url']
	return click_url
	
def main():
	pass
if __name__ == '__main__':
	main()
	
	
	
	
	
'''
一一一一返 利 消 息一一一一
奥康男鞋  黑色圆头商务休闲真皮加绒男鞋低帮鞋套脚舒适保暖皮鞋
------------------
【商品原价】199元
【返利红包】6.17元
--------------------
【购买方法】一定要复制这条信息，才会有返利！打开【手机淘宝】可领卷并下单￥1z1M0MQzAxN￥
------------------
输入“买关键词”  (例如：买连衣裙)
自动查找你想要的商品
'''
