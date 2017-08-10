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
    "Cookie": "IPLOC=CN1100; SUV=1494858714774900; CXID=41ACAA634EC03E664106324C546F4DED; SUID=345748DF2208990A000000005857D960; sw_uuid=4000410243; ssuid=2245000202; dt_ssuid=766539408; SNUID=1278903F51540602DA6535C951608C8D; sg_uuid=2943647500; cid=websearch2ww; sct=5; ld=Rkllllllll2B0VAAlllllVuGQQclllllbDloyZllllwllllljklll5@@@@@@@@@@; ss_cidf=1",
    "Host": "wenwen.sogou.com",
    "Referer":"http://wenwen.sogou.com/s/?w=%E9%80%81%E5%A5%B3%E6%9C%8B%E5%8F%8B&st=4&pg=2&ch=sp.pt",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}

def main():
	f = open('re_con_sogou.txt',r'a+')
	for k in open('linkss_sogou.txt'):
		url = k.split('|')[5]
		print url
		r = requests.get(url,headers=headers)
		s = BeautifulSoup(r.content,"lxml")
		content = s.find_all('pre',attrs={'class':'replay-info-txt answer_con'})
		f.write(k.strip()+'|')
		if content:#最佳答案
			for c in content:
				c = str(c.get_text().strip())
				f.write('<p>'+c+'</p>')#.replace('<br />','')这里目测还需要把换行replace掉
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
