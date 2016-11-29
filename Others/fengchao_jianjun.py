# coding:utf-8
import sys
import urllib

import requests

if len(sys.argv) > 1 and '--help' in sys.argv[1]:
    print '''python fengchao.py input_file output_file
input_file每行一个关键词
output_file包含两列，搜索词和搜索量
文件需打开并更新其中的COOKIE, TOKEN和USERID
'''
    quit()

COOKIE = 'td_cookie=18446744071341242172; FC-FE-TERMINUS=fc_terminus_user; BIDUPSID=C2DCC2198B3DBF956A2DAC69612C2C27; PSTM=1478745782; BDUSS=lEeXVDT2ZzVDJnclBhVlhRM1lJZFk5OFBZQklaNkUyZmVXV21vVUhjVHZ0a3RZSVFBQUFBJCQAAAAAAAAAAAEAAACDmi1VVGhpbmt3aWtpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO8pJFjvKSRYV2; BAIDUID=C2DCC2198B3DBF956A2DAC69612C2C27:FG=1; PSINO=1; H_PS_PSSID=1457_21531_17944_21079_17001_21385_21454_21409_21417_21378_21526_21193; MCITY=-131%3A; SFSSID=771036dda5e93079827cb432da2ef07a; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a02293048622; uc_login_unique=59df4c848c728bf0db1d5e69607d418c; __cas__st__3=8a98d45a9be3f7150d51b53cc96c10db145d18f6d05a2fee6b699825eb69a9a418490720ba75fe127d20242c; __cas__id__3=11255558; __cas__rn__=229304862; SAMPLING_USER_ID=11255558'
TOKEN ='8a98d45a9be3f7150d51b53cc96c10db145d18f6d05a2fee6b699825eb69a9a418490720ba75fe127d20242c'
USERID = '11255558'

# 参数1 输入文件，参数2 输出文件
# 输入文件每行一个词根，输出文件两列：关键词、搜索量
input_file, output_file = sys.argv[1:3]

f = open(output_file, 'w')

for i, line in enumerate(open(input_file), 1):
    kw = line.rstrip().split('\t')[0]
    print i, kw,

    # 指定POST的内容
    post = {
        'params': '{"logid":-1,"query":"%s","querySessions":[],"querytype":1,"regions":"0","device":0,"rgfilter":1,"entry":"kr_easyManage_keyword","planid":"0","unitid":"0","needAutounit":false,"filterAccountWord":true,"attrShowReasonTag":[],"attrBusinessPointTag":[],"attrWordContainTag":[],"showWordContain":"","showWordNotContain":"","pageNo":1,"pageSize":300,"orderBy":"","order":"","forceReload":true}' % (kw),
        'path': 'jupiter/GET/kr/word',
        'token': TOKEN,
        'userid': USERID,
    }

    data = requests.post('http://fengchao.baidu.com/nirvana/request.ajax?path=jupiter/GET/kr/word', data=post, headers={'Cookie': COOKIE}).json()

    # 异常情况下直接输出获取到的全部内容
    if 'data' not in data:
        print data
        continue

    if not data['data']['group']:
        print data
        continue

    count = 0
    for group in data['data']['group']:
        for line in group['resultitem']:
            count += 1
            print >>f, '%s\t%d' % (line['word'].encode('utf-8'), line['pv'])
        print count
