# coding = utf-8
"""
作者:joe
根据关键词获取百度搜索结果前3页，导出标题和网址到CSV文件中，用于寻找外链资源。
"""
import requests
import random
import csv
from urllib import parse
from bs4 import BeautifulSoup as bs
#  获取网址的域名  https://pypi.python.org/pypi/tld
from tld import get_tld
# 校验URL是否合法
import validators
# 创建一个存储结果的CSV文件，使用追加模式
save_file = open('result.csv', 'a')
# 创建CSV对象
csvwriter = csv.writer(save_file)
# 写入文件表头
fields = ['title', 'true_url', 'domain']
csvwriter.writerow(fields)

def get(word, page = 2):
	# 需要采集百度搜索结果的关键词
	word = word
	# 对关键词进行URLencode
	word = parse.quote_plus(word)
	# 拼接待查询网址
	for pn in range(1, page + 1):
		# 百度分页样例  第二页  https://www.baidu.com/s?ie=utf-8&wd=python&pn=10
		url = 'https://www.baidu.com/s?ie=utf-8&wd=' + word + '&pn=' + str((pn-1)*10)
		headers = {}
		headers['User-Agent'] = "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0" + str(random.randint(1,99))
		headers['Referer'] = url
		# 超时设为10秒，如果网页10秒内无响应抛出异常
		timeout = 10
		# 发送请求
		res = requests.get(url, headers = headers, timeout = timeout)
		# 获取页面的响应状态码(200/404/301等)
		http_status = res.status_code
		# 获取待采集页面的编码(UTF-8，GBK等编码)
		res_encoding = res.encoding
		# 获得采集页面的HTML代码，转化为UTF8编码，避免乱码问题
		html_code = res.text.encode(res.encoding).decode('utf8')
		# 把HTML代码转化为用Beautiful Soup变成DOM对象，解析内核使用lxml，效率高
		soup = bs(html_code, "lxml")

		# 通过DOM标签拿到搜索结果标题部分代码块
		for item in soup.select(".c-container h3.t"):
			# 获取标题文本，strip()去掉前后空格
			title = item.get_text().strip()
			# 标题模块读第一个A标签对应的百度加密URL
			encode_url = item.select('a')[0].get('href')
			# 使用Request Head方法请求加密URL，从跳转后的Header信息中获得真实地址
			true_url = requests.head(encode_url, allow_redirects=False).headers.get('location')
			if validators.url(true_url):		
				domain = get_tld(true_url, as_object=True)
				domain = domain.subdomain + '.' + domain.tld
			else:
				domain = true_url
			print(title)
			print(encode_url)
			print(true_url)
			print(domain)
			csvwriter.writerow([title, true_url, domain])

if __name__ == "__main__":
	get("挖掘机", 5)
