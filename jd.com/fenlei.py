#coding:utf-8
# author = 'heziliang'
import requests,sys,json,MySQLdb
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')
conn = MySQLdb.connect('localhost','root','','fenlei',charset='utf8')
with conn:
	def main():
		for line in open('kwss.txt'):	    
			#公司接口与参数配置
      url = '*********'
			load = {'****':'%s'%line.strip(),'****':'****','****':'****','****':'****'}
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
				cur1 = conn.cursor()
				sql1 = 'select fclass_name from t_fclass where fclass=%s' %fid
				cur1.execute(sql1)
				conn.commit()
				row_num1 = int(cur1.rowcount)
				for i in range(row_num1):
					row1 = cur1.fetchone()									
				cur2 = conn.cursor()
				sql2 = 'select sclass_name from t_sclass where sclass=%s' %sid
				cur2.execute(sql2)
				conn.commit()
				row_num2 = int(cur2.rowcount)
				for i in range(row_num2):
					row2 = cur2.fetchone()								
				cur3 = conn.cursor()
				sql3 = 'select tclass_name from t_tclass where tclass=%s' %tid
				cur3.execute(sql3)
				conn.commit()
				row_num3 = int(cur3.rowcount)
				for i in range(row_num3):
					row3 = cur3.fetchone()					
			except Exception,e:
				print e
				#如果关键词的分类返回结果为null，则此次循环结束
				continue
			try:
				f.write(line.strip().decode('gbk').encode('utf-8')+':'+row1[0]+','+row2[0]+','+row3[0]+'\n')
				print line.strip(),fid,sid,tid
			except Exception,e:
				print e					
	f = open('result_fenlei.txt',r'a+')
	main()
	f.close()
#	conn.close()


'''
#coding:utf-8
import requests,sys,json,MySQLdb
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')
#conn = MySQLdb.connect('localhost','root','','fenlei',charset='utf8')
def main():
	for line in open('kwss.txt'):			
		url = '000'
		load = {'key':'%s'%line.strip(),'pagesize':'****','qp_disable':'***','client':'****'}#,'debug':'yes'
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
			f.write(line.strip().decode('gbk').encode('utf-8')+':'+fid+','+sid+','+tid+'\n')
			print line.strip(),fid,sid,tid
		except Exception,e:
			print e					
f = open('result_fenlei.txt',r'a+')
main()
f.close()
#	conn.close()
		



'''


