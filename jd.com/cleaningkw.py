#coding:utf-8
#处理关键词特殊字符
import re

def main():
#	f1 = open('reg.txt')
	f = open('result_hanzishuzi.txt',r'w+')
	for line in open('hanzishuzi1.txt'):
		kw = line.strip()
		w_str=''
		
		
#		要死啊，fuck,,,
#		f3 = open('reg.txt')
#		for reg in f3:
#			if reg in kw:
#				kw = re.sub(r'%s'%reg,'',kw)


		reg = re.compile('\+|=|-|）|（|\)|\(|&|%|……\^|￥|\$|#|@|】|【| |-|\.|\*|amp|nbsp|;|\/|]|\[|{|}|：|；')
		reg2 = re.compile(r'\d+')
		reg3 = re.compile(r'[a-zA-Z]+')
		kw = re.sub(reg,'',kw)#特殊字符
		kw = re.sub(reg2,'',kw)#数字
		kw = re.sub(reg3,'',kw)#字母
		w_str = w_str+kw
		f.write(w_str+'\n')
	f.close()
#	f1.close()
	
if __name__ == '__main__':
	main()
'''
#coding:utf-8
#处理关键词特殊字符

author = 'heziliang'
import re
def main():
	for line in open('kw.txt'):
		kw = line.strip()
		kw = re.sub(r'(\(.*?\))','',kw)#两边都是英文括号
		kw = re.sub(r'（.*?）','',kw)#两边都是中文括号
		kw = re.sub(r'(\(.*?）)','',kw)#左边英文，右边中文
		kw = re.sub(r'(（.*?\))','',kw)#左边中文，右边英文
		kw = re.sub(r'>|<|\+|=|-|）|（|\)|\(|&|%|……|\^|￥|\$|#|@|】|【| |-|\.|\*|amp|nbsp|;|\/|\]|\[|{|}|：|；|》|《|、|:|。','',kw)#特殊字符
		
		reg6 = re.search(r'(\d+)$',kw)#数字结尾
		reg7 = re.search(r'[a-zA-Z]+$',kw)#字母结尾
		
		if not reg6 or reg7:
			kw = re.sub(r'\d+','',kw)#数字替换为空
			kw = re.sub(r'[a-zA-Z]+','',kw)#字母替换为空
			kw = kw.upper()#小写统一变大写
			with open('results.txt',r'a+') as my:
				my.write(kw+'\n')
if __name__ == '__main__':
	main()




'''





'''
#coding:utf-8
#处理阿里关键词2500万
import re
def main():
#	f1 = open('reg.txt')

#	f = open('result_qq.txt',r'a+')
	for line in open('0.txt'):
		kw = line.strip()
		reg = re.search(r'(\d+)',kw)#含数字
		reg2 = re.search(r'[a-zA-Z]+',kw)#字母
		#特殊字符
		reg3 = re.search(r'>|<|\+|=|-|）|（|\)|\(|&|%|……|\^|￥|\$|#|@|】|【| |-|\.|\*|amp|nbsp|;|\/|\]|\[|{|}|：|；|》|《|、|:|。',kw)
		if reg or reg2 or reg3:
			pass
		else:
			for black in open('blackkw.txt'):#遍历黑名单关键词，依次匹配
				bkw = black.strip()
				if bkw in kw:#匹配上黑名单保存
					with open('re_hmd.txt',r'a+') as my:
						my.write(kw+','+bkw+'\n')
#				else:
#					f.write(kw+'\n')#这里只想要没有匹配到黑名单的关键词
		
#	f.close()
#	f1.close()
	
if __name__ == '__main__':
	main()
	
	
	
'''





