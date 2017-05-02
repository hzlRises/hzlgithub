#coding:utf-8
from urlparse import urlsplit
from os.path import basename
import urllib2
import re
import requests
import os
import json
#当一个颜值很高的程序员是怎样一番体验？
url = 'https://www.zhihu.com/question/37787176'

if not os.path.exists('images'):
    os.mkdir("images")

page_size = 50
offset = 0
url_content = urllib2.urlopen(url).read()
answers = re.findall('h3 data-num="(.*?)"', url_content)
limits = int(answers[0])
while offset < limits:
    post_url = "http://www.zhihu.com/node/QuestionAnswerListV2"
    params = json.dumps({
        'url_token': 37787176,
        'pagesize': page_size,
        'offset': offset
    })
    data = {
        '_xsrf': '',
        'method': 'next',
        'params': params
    }
    header = {
        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
        'Host': "www.zhihu.com",
        'Referer': url
    }
    response = requests.post(post_url, data=data, headers=header)
    answer_list = response.json()["msg"]
    img_urls = re.findall('img .*?src="(.*?_b.*?)"', ''.join(answer_list))
    for img_url in img_urls:
        try:
            img_data = urllib2.urlopen(img_url).read()
            file_name = basename(urlsplit(img_url)[2])
            output = open('images/' + file_name, 'wb')
            output.write(img_data)
            output.close()
        except:
            pass
    offset += page_size
