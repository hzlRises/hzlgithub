#coding:utf-8
#切割千万级别关键词文本文件，100万一个
kw = 0
for i,line in enumerate(open('ali_words.txt')):
	f = open('%s.txt'%kw,r'a+')
	f.write(line.strip()+'\n')
	if i%1000000 == 999999:
		f.close()
		kw += 1
		f = open('%s.txt'%kw,r'a+')
