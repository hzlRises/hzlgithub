# coding:utf-8
from base import *

if '--help' in sys.argv[1]:
	print '''python fengchao.py input_file output_file
input_file每行一个关键词
output_file包含两列，搜索词和搜索量
文件需打开并更新其中的COOKIE, TOKEN和USERID
'''
	quit()
COOKIE = 'BAIDUID=9F58FC9D722E08254E7F1E9ED6E5621A:FG=1; BIDUPSID=9F58FC9D722E08254E7F1E9ED6E5621A; PSTM=1463534354; H_PS_PSSID=; BDSFRCVID=7M_sJeCCxG3xuKvRMFd1Sqyr09sgaLlGJ5x73J; H_BDCLCKID_SF=JRu8_I_MtCvbfP0khn32btFHqxbXq5buX57Z0lOnMp05J-5o5l5YQ43L0pQ8bj88-KvK2nRTWD5WMIO_e4bK-TrBDa8eJx5; H_WISE_SIDS=104688_104588_104919_104495_100181_102435_106368_104483_103550_106311_104331_106058_104340_106323_106237_103999_106149_104639_106071_106162_106158_106238; plus_cv=1::m:1552fab9; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a02135655377; uc_login_unique=bfe2f9157677a9806ecdb45bb824cab3; __cas__st__3=9e118e11cf7f09176403c3ad893e60d9e29ee4f909ced69656eead3e610d09e22a38fbe0e14d313a230535a9; __cas__id__3=8048066; __cas__rn__=213565537; SAMPLING_USER_ID=8048066; BDRCVFR[gltLrB7qNCt]=mk3SLVN4HKm; BDRCVFR[VjobkFsAYtR]=mk3SLVN4HKm'
TOKEN = '9e118e11cf7f09176403c3ad893e60d9e29ee4f909ced69656eead3e610d09e22a38fbe0e14d313a230535a9'
USERID = '8048066'

# 参数1 输入文件，参数2 输出文件
# 输入文件每行一个词根，输出文件两列：关键词、搜索量
input_file, output_file = sys.argv[1:3]

f = open(output_file, 'w')

for i, line in enumerate(open(input_file), 1):
	kw = line.rstrip().split('\t')[0]
	print i, kw

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
	for group in json.loads(data)['data']['group']:
		print >>f, '%s\t%s' % (group['resultitem'][0]['word'].encode('utf-8'),group['resultitem'][0]['pv'])
f.close  