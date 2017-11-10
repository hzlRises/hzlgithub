#coding:utf-8
import requests,sys,json,MySQLdb,csv,time
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')
#conn = MySQLdb.connect('localhost','root','','fenlei',charset='utf8')
def main():
	for line in open('4.txt'):
		time.sleep(0.01)
		url = '000'
		load = {'key':'%s'%line.strip(),'pagesize':'000','qp_disable':'000','client':'000'}#,'debug':'yes'
		#请求
		try:
			r = requests.get(url,params=load)
			data = r.content.decode('gbk').encode('utf-8')#还是编码问题
			data = json.loads(data)
		except Exception,e:
			print e
			with open('fail.txt',r'a+') as my:
				my.write(line.strip()+'\n')
			pass
		#解析
		try:
			fid = data["Paragraph"][0]["cid1"]
			sid = data["Paragraph"][0]["cid2"]
			tid = data["Paragraph"][0]["catid"]
		except Exception,e:
			print e
			#如果关键词的分类返回结果为null，则此次循环结束
			continue
		try:
			#f.write(line.strip().decode('gbk').encode('utf-8')+':'+row1[0]+','+row2[0]+','+row3[0]+'\n')
#			f.write(fid+','+sid+','+tid+line.strip().decode('gbk').encode('utf-8')+'\n')
			writer.writerow((fid,sid,tid,line.strip().decode('gbk').encode('utf-8')))
			print line.strip(),fid,sid,tid
		except Exception,e:
			print e
		
#f = open('result_fenlei_0.txt',r'a+')
csvf = open('result_4.csv','ab')
writer = csv.writer(csvf)


main()
#f.close()
csvf.close()
#	conn.close()
		
