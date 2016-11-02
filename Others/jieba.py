#!/usr/bin/env python
# -*- coding:utf-8 -*-
import  jieba
import jieba.posseg as pseg
import sys
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')  
import re 
from operator import itemgetter, attrgetter

text = open('baike.txt','r')
#link = re.compile("\s+")
#text = re.sub(link,'',text)
#jieba.load_userdict('u.txt')
fp=open('1.xls','w')

fp.write('fenci\tcipin\tcixing\tdianpingyonghu\n')
nu={}
num={}
user={}
n=0
for line in text:
	print line
	words = pseg.cut(line) 
	result=""
	dict={}
	ends={}
	aa=''
	c=''
	i = 0
	k = 1
	flags=['n','i','eng','nr','nz','ns']    
	for w in words:
	    result+= w.word+"/"+w.flag
	    if(w.flag in flags):
		if len(w.word) > 1: 
		     if w.word in dict:
			dict[w.word]+=1 
		     else:  
        	        dict[w.word]=1
		if len(w.word) > 1:
       		     if w.word in num: 
		        num[w.word]+=1
		        nu[w.word]=w.flag
		     else:
		        num[w.word]=1
		        nu[w.word]=w.flag
	        ends[i] = w.word
        	c = w.word
	        i+=1
        for word in dict:
	    #print word.encode('gbk'),v
	    if word in user:
       	       user[word]+=1
	    else:
	       user[word]=1 
	n+=1
#	print(result.encode('gbk'))

numsort=sorted(num.iteritems(), key=itemgetter(1), reverse=True)
for key,v in numsort:
#	print key.encode('gbk'),v,nu[key],user[key],n
	key_num=nu[key]
	key_user=user[key]
	fp.write(key.encode('gbk')+"\t"+str(v)+"\t"+key_num.encode('gbk')+"\t"+str(key_user)+"\t"+str(n)+"\n")

#bb = ''
#for a,b in ends.items():
#        bb+= b+"--------"+'\n'
#print(bb.encode('gbk'))  
