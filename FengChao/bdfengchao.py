# -*- coding: utf-8 -*-
"""
verseion: beta2.2
说明：
百度蜂巢挖词脚本
利用百度蜂巢关键词规划师工具进行关键词挖掘
用到第三方模块：requests
详见：http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
作者：Brooks QQ: 76231607
请勿用于任何商业用途，版权最终归作者所有
"""
import requests
import json
import time


def get_result_data(key, uconfig, cookie, retry=3):
    """获取关键词查询结果数据
    :param key: 要查询的关键词
    :param uconfig: 用户配置信息
    :param cookie: cookie登录信息
    :param retry: 链接过程失败重试次数
    :return: 返回json类型数据以及错误信息
    """
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookie,
        'Host': 'fengchao.baidu.com',
        'Origin': 'http://fengchao.baidu.com',
        'Referer': 'http://fengchao.baidu.com/nirvana/main.html?userid=%s' % uconfig['userid'],
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    query = 'http://fengchao.baidu.com/nirvana/request.ajax?'\
            'path=jupiter/GET/kr/word&reqid=%s' % uconfig['reqid']

    params = {
        "logid": -1,
        "query": key,
        "querySessions": [key],
        "querytype": 1,
        "regions": "0",
        "device": 0,
        "rgfilter": 1,
        "entry": "kr_wordlist_addwords",
        "planid": "0",
        "unitid": "0",
        "needAutounit": False,
        "filterAccountWord": True,
        "attrShowReasonTag": [],
        "attrBusinessPointTag": [],
        "attrWordContainTag": [],
        "showWordContain": "",
        "showWordNotContain": "",
        "pageNo": 1,  # 由于pageSize已经是1000，所以不需要再进行分页查询
        "pageSize": 1000,
        "orderBy": "",
        "order": "",
        "forceReload": True
    }
    form_data = {
        'params': json.dumps(params),
        'path': 'jupiter/GET/kr/word',
        'userid': uconfig['userid'],
        'token': uconfig['token'],
        'eventId': uconfig['eventId'],
        'reqid': uconfig['reqid']
    }

    try:
        resp = requests.post(query, headers=headers, data=form_data, timeout=10)
    except requests.exceptions.RequestException:
        resultitem = {}
        err = u"请求了那么多次，百度还是没给返回正确的信息！"
        if retry > 0:
            return get_result_data(key, uconfig, cookie, retry - 1)
    else:
        resp.encoding = 'utf-8'
        try:
            resultitem = resp.json()
        except ValueError:
            resultitem = {}
            err = u"获取不到json数据，可能是被封了吧，谁知道呢？"
        else:
            err = None
    return resultitem, err


def parse_data(datas):
    """用于解析获取回来的json数据
    :param datas: json格式的数据
    :return: 返回关键词列表以及错误信息
    """
    try:
        resultitem = datas['data']['group'][0]['resultitem']
    except (KeyError, ValueError, TypeError):
        kws = []
        err = u'获取不到关键词数据'
    else:
        kws = ['{}\t{}'.format(item['word'].encode('utf-8'), item['pv']) for item in resultitem]
        err = None
    return kws, err


if __name__ == '__main__':
    sfile = open('resultkeys.txt', 'w')  # 结果保存文件
    faileds = open('faileds.txt', 'w')  # 查询失败保存文件
    checkwords = [word.strip() for word in open('checkwords.txt')]  # 要查询的关键词列表
    cookies = open('cookie.txt').read().strip()  # cookie文件, 里面只放一条可用的cookie即可
    # 用户配置信息，请自行登录百度蜂巢后台通过抓包获取 (以下只是虚拟数据不能直接使用)
    config = {
        'userid': 23285888,
        'token': 'c9163bf064179032a05e36e6f7dc69381b292296s82243b67ac308f196e90a0ec05bce0d70d351c8d5ff68b5c',
        'eventId': '4b534s46-e593-8888-d00c-14890485888',
        'reqid': '4b534s46-7f8b-8888-de26-148904853888'
    }
    for word in checkwords:
        print u'正在查询: {}'.format(word)
        print u'-' * 50
        dataresult, error = get_result_data(word, config, cookies)
        if error:
            print u'{}: {}'.format(word, error)
            faileds.write('%s\n' % word)
            faileds.flush()
            continue
        keywordlist, error = parse_data(dataresult)
        if error:
            print u'{}: {}'.format(word, error)
            faileds.write('%s\n' % word)
            faileds.flush()
            continue
        for kw in keywordlist:
            sfile.write("%s\n" % kw)
            sfile.flush()
            print u'{}'.format(kw)
        print '=' * 50
        time.sleep(2)  # 每个词的查询间隔时间为2秒，如果不怕被封，可以直接去掉
    sfile.close()
    faileds.close()
    print u"所有关键词查询完毕"





'''
脚本使用说明：
1. 百度蜂巢挖词脚本优化版，主要解决了不能对中文进行挖词的问题；
2. 脚本同时封装了方法，可以随时进行外部调用；
3. 脚本是基于Python2.7.x版本开发的，暂不支持Python3.x；
4. 使用脚本需要有百度蜂巢的账号，因为需要获取到cookie，用户id等信息才能进行采集；
5. 需要知道怎么去抓包来获取脚本需要的字段信息(userid token eventId reqid)；
6. 脚本仅用于内部学习交流之用，请勿用于商业用途，对脚本进行贩卖等；
7. 脚本最终解析权归作者所有(Brooks QQ: 76231607)。
================================广告================================
学习牛B的SEO技术，跟牛B的大神打交道，ITSEO，你的最佳选择：
网址：www.itseo.net
=================================END================================

'''
