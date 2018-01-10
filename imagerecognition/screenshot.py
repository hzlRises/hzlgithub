#coding:utf-8
from PIL import ImageGrab
from aip import AipOcr

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def getScreenshot():
	bbox = (537,164,847,258)
	im = ImageGrab.grab(bbox)
	im.save('C:\\Users\\heziliang\\sbtp\\6.jpg')
	print 'saved image...'
	
	image = get_file_content('C:\\Users\\heziliang\\sbtp\\6.jpg')	
	APP_ID = '00'
	API_KEY = '0'
	SECRET_KEY = '0'
	client = AipOcr(APP_ID, API_KEY, SECRET_KEY)	
	text = client.basicGeneral(image)	
	print 'read image...'
	for xy in text['words_result']:
		print xy['words']

def main():
	getScreenshot()

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
