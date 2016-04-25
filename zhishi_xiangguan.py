著作权归作者所有。
商业转载请联系作者获得授权，非商业转载请注明出处。
作者：张亚楠
链接：https://www.zhihu.com/question/26838876/answer/34332882
来源：知乎

import requests
import time


def append_list(l1, l2):
	'''
	一个辅助函数，作用是将一个列表合并到已知列表，并剔除已存在的元素
	'''
	for l in l2:
		if l not in l1:
			l1.append(l)
	return l1

words = ['ruby']  # 初始关键词列表

def relatewords(words):
	'''
	主体函数
	'''
	for w in words:  # 遍历初始关键词列表
		if len(words) < 100:  # 做个判断，如果关键词列表小于100个，可以修改为10W
			url = 'http://www.baidu.com/s?wd=%s&tn=baidurs2top' % w  # 相关搜索的API，来自@吴星
			r = requests.get(url)  # 请求网页
			c = r.content.decode('utf-8').split(',')  # 得到网页内容，并且解码为unicode，以逗号分为列表
			words = append_list(words, c)  # 将得到的新关键词加入关键词列表，一方面为遍历，一方面作结果
			print len(words)  # 显示列表目前的个数，debug用，可取消
			time.sleep(3)  # 等待3秒，防屏蔽
		else:  # 如果列表大于1000，则不用遍历，已经得到结果
			break  # 跳出循环
	return words  # 返回最后列表

l = relatewords(words)
for i in l:
	print i
print len(l)