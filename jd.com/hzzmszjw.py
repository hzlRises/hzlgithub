#coding:utf-8
#处理关键词特殊字符
import re
def main():
#	f1 = open('reg.txt')
	f = open('result_hzzmsz.txt',r'w+')
	for line in open('hzzmsz.txt'):
		kw = line.strip()
		reg = re.search(r'(\d+)$',kw)
		reg2 = re.search(r'[a-zA-Z]+$',kw)
		if reg or reg2:
			f.write(kw+'\n')
		else:
			pass
	f.close()
#	f1.close()
	
if __name__ == '__main__':
	main()
