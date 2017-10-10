# coding = utf-8
'''
服务器日志批处理，利用Python实现，日志批量筛选和有效导出。
'''

import re
import time

path = 'test.log'

status_200 = 0
status_301 = 0
status_404 = 0
baiduspider_num = 0
line_num = 0

with open(path, 'r') as f:
	all_lines = f.readlines()
	line_num = len(all_lines)
	for line in all_lines:
		item = line.rstrip()
		pattern = '.*?\_\d+\:(.*?)\s+\-\s+\-\s+\[(.*?)\]\s+\"(.*?)\s+(.*?)\"\s+STAT=(\d+)\s+.*?\"(.*?)\"\s+\"(.*?)\"\s+\"(.*?)\"'
	
		match = re.search(pattern, item)
		
		remote_addr = match.group(1)
		time_local = match.group(2)
		# 字符串转换为标准时间结构，%d代表日期 %b代表英文简写月份，%Y代表完成的年份，%H完整小时，%M完整分钟，%S完整秒 %z代表时区。  参考 http://www.mamicode.com/info-detail-317126.html
		time_local = time.strptime(time_local, "%d/%b/%Y:%H:%M:%S %z")
		# 转化为容易理解的日期样式 比如 2017-09-20 12:00:00
		time_local = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
		method = match.group(3)
		request = match.group(4)
		status = match.group(5)
		http_referer = match.group(6)
		http_user_agent = match.group(7)
		http_x_forwarded_for = match.group(8)

		print("remote_addr：" + remote_addr)
		print("time_local：" + str(time_local))
		print("status：" + status)
		print("method：" + method)
		print("request：" + request)
		print("http_referer：" + http_referer)
		print("http_user_agent：" + http_user_agent)
		print("http_x_forwarded_for：" + http_x_forwarded_for)
		print("*"*100)
		
		if status == '200':
			status_200 += 1
		if status == '301':
			status_301 += 1
		if status == '404':
			status_404 += 1
			# 把404页面写入文件中，方便以后分析
			with open('status_404.txt', 'a') as file:
				content = "\t".join((remote_addr, time_local, status, request, http_referer, http_user_agent, http_x_forwarded_for)) + "\n"
				file.write(content)

		if "Baiduspider/2.0; +http://www.baidu.com/search/spider.html" in http_user_agent:
			baiduspider_num += 1

print("总行数：{0}".format(line_num))
print("正常200状态页面数量：{0}，占比：{1}%".format(status_200,round((status_200*100/line_num), 2)))
print("301重定向页面数量：{0}，占比：{1}%".format(status_301,round((status_301*100/line_num), 2)))
print("404找不到页面数量：{0}，占比：{1}%".format(status_404,round((status_404*100/line_num), 2)))
print("百度蜘蛛抓取数：{0} ".format(baiduspider_num))
