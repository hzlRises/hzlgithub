#coding:utf-8
import time
def inputTxt(cat1,cat2,cat3,kw,laiyuan,catalog):
#	print cat1,cat2,cat3,kw,laiyuan,catalog
	try:
		if laiyuan == '运营添加':		
			with open('C:\\Users\***\\1_znmb_index\\mulu\\%s_Yytj.txt'%catalog,r'a+') as my:
				my.write(cat1+','+cat2+','+cat3+','+kw+','+laiyuan+'\n')
		else:
			with open('C:\\Users\\***\\1_znmb_index\\mulu\\%s_Sxzh.txt'%catalog,r'a+') as my:
				my.write(cat1+','+cat2+','+cat3+','+kw+','+laiyuan+'\n')
	except Exception,e:
		with open('error.txt',r'a+') as my:
			now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
			my.write(e+now+'\n')
def main():
	for i in range(0,61):
		
		allStr_list = [line.strip() for line in open('%s.csv'%i)]
		num = 0
		for line in allStr_list[1:]:
			try:
				line = line.strip()
				cat1 = line.split(',')[1].replace('"','')
				cat2 = line.split(',')[3].replace('"','')
				cat3 = line.split(',')[5].replace('"','')
				kw = line.split(',')[6].replace('"','')
				laiyuan = line.split(',')[10].replace('"','')
			except Exception,e:
				with open('error.txt',r'a+') as my:
					now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
					my.write(e+now+'\n')
				
			try:
			
				#图书		
				if int(cat1) == 1713:
					inputTxt(cat1,cat2,cat3,kw,laiyuan,'tushu')	
					
				#价格
				if int(cat1) in [9987,737,1318,670,1672,9855,12259,12473,6233,12218]:
					inputTxt(cat1,cat2,cat3,kw,laiyuan,'jiage')	
				
				#图片
				if int(cat1) in [1620,1315,6728,1319,1320,5025,13678]:
					inputTxt(cat1,cat2,cat3,kw,laiyuan,'tupian')	
				#新款
				if int(cat1) in [652,6994,1316,6144,9847,6196,11729]:
					inputTxt(cat1,cat2,cat3,kw,laiyuan,'xinkuan')	
			except Exception,e:
				with open('error.txt',r'a+') as my:
					now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
					my.write(e+now+'\n')
			num += 1
			print i,num
		with open('C:\\Users\heziliang\\1_znmb_index\\mulu\\done.txt',r'a+') as my:
			now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
			my.write(i+','+now+'\n')
			
if __name__ == '__main__':
	main()
