# coding:utf-8
import json
import random
import shutil
import sys
import time
import urllib

import requests
import openpyxl

if len(sys.argv) > 1 and '--help' in sys.argv[1]:
    print '''python fengchao.py file.xlsx
文件需打开并更新其中的COOKIE
'''
    quit()

COOKIE = 'BIDUPSID=A1D7FEED5ACAF63B079C37CDE4A6024B; PSTM=1469497677; BDUSS=W9CR3V-M2V1RGFDdWlyLTJDaVY2bnJWSWlxRldoRFZiVENwRzZ4eHB4Y21qY0pYQVFBQUFBJCQAAAAAAAAAAAEAAACDmi1VVGhpbmt3aWtpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACYAm1cmAJtXY; BAIDUID=A1D7FEED5ACAF63B079C37CDE4A6024B:FG=1; uc_login_unique=07e9c809d59f783501b5a5bb2dbef50d; H_PS_PSSID=1466_18241_19861_17001_12076_20856_20733_20837_20885; SFSSID=89a6e74d5a80cd3770c9bf83e56ff48a; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a02221236844; __cas__st__3=f9080732f5e45b1c36f350c2cb39af682c0b63cea429d73533b6c9aec3490eb7a389ec1e4063c0d98fcef24a; __cas__id__3=11255558; __cas__rn__=222123684; Hm_lvt_ab31944d33b258d42a263a7c78b303a3=1471508960,1471512421,1471955977,1472111000; Hm_lpvt_ab31944d33b258d42a263a7c78b303a3=1472111000; __bsi=9076050137757375281_31_13_N_R_4_0303_c02f_Y; SAMPLING_USER_ID=11255558'
TOKEN ='f9080732f5e45b1c36f350c2cb39af682c0b63cea429d73533b6c9aec3490eb7a389ec1e4063c0d98fcef24a'
USERID = '11255558'

session = requests.session()
ws = openpyxl.load_workbook(sys.argv[1])
for sheet in ws:
    rows = sheet.rows
    for start in range(0, len(rows), 1000):
        wordList = {row[0].value: start + i + 1 for i, row in enumerate(rows[start:start+1000]) if row[0].value}
        if not wordList:
			break
        post = {
            'params':'{"logid":-1,"entry":"kr_station_bidestimate_tab","bidWordSource":"wordList","regions":"0","device":0,"pageNo":1,"pageSize":1000,"orderBy":"","order":"desc","wordList": %s}' % json.dumps([{'word': word.encode('utf-8'), 'bid': None, 'wmatch': None, 'wctrl': None} for word in wordList.keys()]),
            'path': 'jupiter/GET/kr/bidestimate',
            'token': TOKEN,
            'userid': USERID,
        }
        print "requesting"
        data = session.post('http://fengchao.baidu.com/nirvana/request.ajax?path=jupiter/GET/kr/bidestimate', data=post, headers={'Cookie': COOKIE}).json()
        if 'data' not in data:
            print 'request error:', data
            quit()

        errItems = data['data']['errorItems']
        print 'request keyword: %d, receive %d, error items: %s' % (len(wordList), len(data['data']['data']), errItems[0]['message'] if errItems else 'empty')
        for d in data['data']['data']:
            word = d['word']
            pcPv = d['pcPv']
            sheet.cell(column=3, row=wordList[word]).value = pcPv

        timeout = random.randint(1, 5)
        print "sleep %d sec" % timeout
        time.sleep(timeout)

ws.save(sys.argv[1] + ".tmp")
shutil.move(sys.argv[1] + ".tmp", sys.argv[1])

