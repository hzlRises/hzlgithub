#coding:utf-8
from PIL import ImageGrab
from aip import AipOcr
import time,requests

def getSerp(kw):
	headers = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": "zh-CN,zh;q=0.8",
		"Cache-Control": "max-age=0",
		"Connection": "keep-alive",
		"Cookie": "",
		"Host": "zhidao.baidu.com",
		"Upgrade-Insecure-Requests": "1",
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",    
	}

	url = 'https://zhidao.baidu.com/index?word=%s'%kw
	r = requests.get(url,headers=headers)
	if r.status_code == 200:
		with open('res.txt',r'w+') as my:
			my.write(r.content)
	else:
		print 'error...'
	

def imageRecognition(image):
	APP_ID = '1'
	API_KEY = '1'
	SECRET_KEY = '1'
	client = AipOcr(APP_ID, API_KEY, SECRET_KEY)	
	text = client.basicGeneral(image)	
	print 'read image...'	
	kw_list = []	
	for xy in text['words_result']:		
		kw_list.append(xy['words'])
	kw = ''.join(kw_list)#问题列表转字符串
	return kw

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def getScreenshot():
	
	bbox = (537,164,847,258)
	im = ImageGrab.grab(bbox)
	im.save('C:\\Users\\heziliang\\sbtp\\6.jpg')
	print 'saved image...'
	

def main():
	start = time.time()
	getScreenshot()
	image = get_file_content('C:\\Users\\heziliang\\sbtp\\6.jpg')	
	kw = imageRecognition(image)
	getSerp(kw)#请求百度知道
	
	end = time.time()
	
	print end-start

if __name__ == '__main__':
	main()
	
	
'''
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('example.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """
client.basicGeneral(image);

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为本地图片 """
client.basicGeneral(image, options)

url = "https//www.x.com/sample.jpg"

""" 调用通用文字识别, 图片参数为远程url图片 """
client.basicGeneralUrl(url);

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为远程url图片 """
client.basicGeneralUrl(url, options)


'''
