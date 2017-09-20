# -*- coding: utf-8 -*-
import csv,sys
reload(sys)
sys.setdefaultencoding("utf-8")

noincludefile = open('nofile.txt','w')
includefile = open('yesfile.txt','w')
keyfile = open('keyfile.txt','w')



with open('check_url_index.csv') as csvfile:
	
	reader = csv.reader(csvfile)
	for x in reader:
		y = ','.join(x)
		if "已索引" in y:
			keyfile.write(y+'\n')
			print y
			
		elif "未索引" in y:
			includefile.write(y+'\n')
			print y
		elif  "未收录" in y:
			noincludefile.write(y+'\n')
			print y
		else:
			print y
			continue
	
			