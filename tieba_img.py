#coding:utf-8
import urllib
import re
'''
以前在贴吧看到美女图片，只能手动另存为到本地，现在....
'''
def imgGet():
	html = urllib.urlopen('http://tieba.baidu.com/p/4578614900').read()
	pattern = '<img class="BDE_Image" src="(.*?)"'
	reg = re.compile(pattern)
	return re.findall(reg,html)
for line in imgGet():
	urllib.urlretrieve(line,'img/ %s'%line.split('/')[-1])
'''
urllib.urlretrieve(url, filename, reporthook, data)
参数说明：
url：外部或者本地url
filename：指定了保存到本地的路径（如果未指定该参数，urllib会生成一个临时文件来保存数据）；
reporthook：是一个回调函数，当连接上服务器、以及相应的数据块传输完毕的时候会触发该回调。我们可以利用这个回调函数来显示当前的下载进度。
data：指post到服务器的数据。该方法返回一个包含两个元素的元组(filename, headers)，filename表示保存到本地的路径，header表示服务器的响应头。
'''