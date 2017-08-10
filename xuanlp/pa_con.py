#coding:utf-8
import requests,sys,re,pycurl,StringIO,time,xlrd,xlwt
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "BAIDUID=60C4EC61A25A4925BF326DC1939844BE:FG=1; PSTM=1494748917; BIDUPSID=B1C0B1801A9916C109EC6119661AB803; IK_CID_82=2; IK_CID_85=2; __cfduid=d84c32890f009080e7ac9ddd7f14ea19e1495369334; IK_CID_95=2; FP_UID=a989f29df4088cc692c1dcf977476a99; IK_CID_81=5; IK_CID_79=1; IK_CID_1031=10; IK_CID_83=7; IK_CID_78=1; IK_CID_80=5; IK_CID_1=13; IK_60C4EC61A25A4925BF326DC1939844BE=129; IK_CID_74=81; PSINO=2; H_PS_PSSID=1423_13550_21091_17001_20929; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1501332758,1501509384,1501765796,1502116577; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1502117404",
    "Host": "zhidao.baidu.com",
    "Referer":"https://zhidao.baidu.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}

def main():
	f = open('re_con.txt',r'a+')
	for k in open('linkss.txt'):
		url = k.split('|')[2]
		print url
		r = requests.get(url,headers=headers)
		s = BeautifulSoup(r.content,"lxml")
		content = s.find('pre',attrs={'class':'best-text mb-10'})
		if content:#最佳答案
			f.write(k.strip()+'|'+re.(r'"\.*"',str(content)))#还没解决？？？？？
#		other_answer = s.find_all('span',attrs={'class':'con'})
#		if other_answer:#其他答案
#			for ot in other_answer:
#				f.write(ot.get_text().strip()+'|')
		f.write('\n')
	f.close()
if __name__ == '__main__':
	main()


'''
def main():
	data = xlrd.open_workbook('xuanlp.xlsx')
	table = data.sheets()[3]#第三个表
	nrows = table.nrows#获取行数
	wb = xlwt.Workbook()
	sheet = wb.add_sheet('baidu')
	
	for i in range(nrows):
		print table.row_values(i)[2]#第三列
		r = requests.get(table.row_values(i)[2],headers=headers)
		s = BeautifulSoup(r.content,"lxml")
		best_content = s.find('pre',attrs={'class':'best-text mb-10'})
		if best_content:
			sheet.write(i,3,best_content.get_text().strip()+'|')
		other_answer = s.find_all('span',attrs={'class':'con'})
#		if other_answer:
#			for ot in other_answer:
#				sheet.write(i,3,ot.get_text().strip()+'|')
			
if __name__ == '__main__':
	main()
'''
