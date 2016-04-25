# coding:utf-8
from base import *

if '--help' in sys.argv[1]:
	print '''python fengchao.py input_file output_file
input_file每行一个关键词
output_file包含两列，搜索词和搜索量
文件需打开并更新其中的COOKIE, TOKEN和USERID
'''
	quit()
COOKIE = 'BDUSS=FJwd1JpZmdSTXhDRlRNR0lzb25xekM3UzJpQWhkbVZXVDZwNXFQTkRiQWRSVzFXQVFBQUFBJCQAAAAAAAAAAAEAAABh7s8nxLDErGxpZmUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB24RVYduEVWR; BAIDUID=19D61BF1E44E4B461CD478F62D8F59E5:FG=1; PSTM=1448329340; BIDUPSID=4196A58B4BC8EE7B7FF2DC533525223D; H_PS_PSSID=11098_17899_1462_18156_12825_10213_17970_18041_17000_17072_14965_11977_18005_18018_10632; SFSSID=6098fab4ba44229103602ba5e80928cf; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a01983720577; uc_login_unique=61b24bc05238425cd2b7ac9a7a076ca6; __cas__st__3=779de91f1631331bd28b8eea86e228f2e7a4b01aec418b2a5407b5280d5f29861cc7603079ad3feeecc7de57; __cas__id__3=8048066; __cas__rn__=198372057; SAMPLING_USER_ID=8048066'
TOKEN = '779de91f1631331bd28b8eea86e228f2e7a4b01aec418b2a5407b5280d5f29861cc7603079ad3feeecc7de57'
USERID = '8048066'

# 参数1 输入文件，参数2 输出文件
# 输入文件每行一个词根，输出文件两列：关键词、搜索量
input_file, output_file = sys.argv[1:3]

f = open(output_file, 'w')

for i, line in enumerate(open(input_file), 1):
	kw = line.rstrip().split('\t')[0]
	print i, kw,

	# 指定POST的内容
	post = urllib.urlencode({
		'params': '{"entry":"kr_tools","query":"%s","logid":-1,"querytype":1}' % kw,
		'path': 'GET/kr/suggestion',
		'token': TOKEN,
		'userid': USERID,
	})

	data = curl('http://fengchao.baidu.com/nirvana/request.ajax?path=GET/kr/suggestion', POSTFIELDS=post, COOKIE=COOKIE)

	# 异常情况下直接输出获取到的全部内容
	if 'wordid' not in data:
		print data
		continue

	count = 0
        for group in json.loads(data)['data']['group']:
                for line in group['resultitem']:
                        count += 1
                        print >>f, '%s\t%d' % (line['word'].encode('utf-8'), line['pv'])
        print count
