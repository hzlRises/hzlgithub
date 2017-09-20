# -*- coding: utf-8 -*-
"""
批量查询url是否收录及索引脚本
作者: brooks
"""
import csv
import requests  # 此为第三方模块，安装方法: pip install requests
import time
import threading
from Queue import Queue


class CheckIndex(threading.Thread):
    def __init__(self, queue, csvwriter):
        super(CheckIndex, self).__init__()
        self.queue = queue
        self.csvwriter = csvwriter

    def run(self):
        while True:
            url = self.queue.get()
            data = self.get_serp(url)
            self.extract_data(url, data)
            self.queue.task_done()

    def get_serp(self, url, retry_nums=3):
        """
        @url: 要查询的url
        @retry_nums: 失败重试次数
        """
        url = "https://www.baidu.com/s?wd={0}&tn=json".format(url)
        headers = {
            "Host": "www.baidu.com",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.44 Safari/537.36"
        }
        result = {}
        try:
            r = requests.get(url, headers=headers, timeout=30)
            r.encoding = 'utf-8'
        except Exception:
            result = {}
            if retry_nums > 0:
                return self.get_serp(url, retry_nums - 1)
        else:
            try:
                result = r.json()
            except Exception:
                result = {}
                time.sleep(600)  # 出现验证码，程序暂停10分钟重新查询
                return self.get_serp(url, retry_nums - 1)
        return result

    def extract_data(self, check_url, data):
        """
        @check_url: 查询url
        @data: 要提取的json数据
        """
        try:
            result_data = data['feed']['entry']
        except KeyError:
            title = ''
            url = check_url
            ctime = ''
            isindex = '查询出错'
            self.csvwriter.writerow([title, url, ctime, isindex])
        else:
            if result_data[0]:
                for item in result_data[:-1]:
                    url = item['url']
                    if check_url in [url]:
                        title = item['title'].encode('utf-8')
                        indextime = item['time']
                        ctime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(indextime))
                        if indextime == 0:
                            isindex = '未索引'
                        else:
                            isindex = '已索引'
                        self.csvwriter.writerow([title, url, ctime, isindex])
                        print title
                        print url
                        print ctime
                        print '-' * 100
                        break
                else:
                    title = ''
                    url = check_url
                    ctime = ''
                    isindex = '未收录'
                    self.csvwriter.writerow([title, url, ctime, isindex])
            else:
                title = ''
                url = check_url
                ctime = ''
                isindex = '未收录'
                self.csvwriter.writerow([title, url, ctime, isindex])


def check_test(url, retry_nums=3):
    """
    测试函数
    @url: 要查询的url
    """
    url = "https://www.baidu.com/s?wd={0}&tn=json".format(url)
    headers = {
        "Host": "www.baidu.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.44 Safari/537.36"
    }
    result = {}
    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.encoding = 'utf-8'
    except Exception:
        result = {}
        if retry_nums > 0:
            return check_test(url, retry_nums - 1)
    else:
        try:
            result = r.json()
        except Exception:
            print r.text
            result = {}
    if result:
        result_data = result['feed']['entry'][0]
        print bool(result_data)

if __name__ == '__main__':
    url_list = [url.strip() for url in open('checkurl.txt')]  # 待查询url列表，文件必须是utf-8编码，每行一条
    queue = Queue()
    save_file = open('check_url_index.csv', 'a')  # 查询结果保存文件
    fields = ['title', 'url', 'indextime', 'isindex']
    csvwriter = csv.writer(save_file)
    csvwriter.writerow(fields)
    for url in url_list:
        queue.put(url)

    for i in range(15):  # 15为线程数量
        t = CheckIndex(queue, csvwriter)
        t.setDaemon(True)
        t.start()
    queue.join()
    save_file.close()
