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
