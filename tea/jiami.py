#coding:utf-8
import md5,sys

reload(sys)
sys.setdefaultencoding("utf-8")

f = open('jiami_.txt',r'a+')

for line in open('jiami.txt'):
	m1 = md5.new()
	m1.update(line.strip())
	sign = m1.hexdigest()
	
	print sign
	f.write(sign+'\n')
	
f.close()
	
