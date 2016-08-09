#encoding=utf-8
import pycurl
import StringIO
import urllib
import sys
import json
import codecs
import time
sysCharType = sys.getfilesystemencoding()
def curl(url, debug=False, **kwargs):
        while 1:
                try:
                        s = StringIO.StringIO()
                        c = pycurl.Curl()
                        c.setopt(pycurl.URL, url)
                        c.setopt(pycurl.REFERER, url)
                        c.setopt(pycurl.FOLLOWLOCATION, True)
                        c.setopt(pycurl.TIMEOUT, 60)
                        c.setopt(pycurl.ENCODING, 'gzip')
                        c.setopt(pycurl.USERAGENT, 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')
                        c.setopt(pycurl.NOSIGNAL, True)
                        c.setopt(pycurl.WRITEFUNCTION, s.write)
                        for k, v in kwargs.iteritems():
                                c.setopt(vars(pycurl)[k], v)
                        c.perform()
                        c.close()
                        return s.getvalue()
                except:
                        if debug:
                                raise
                        continue

kws=open('kw.txt','r').readlines()
for kw in kws:
    print kw+'开始'
    zm=['','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(zm)):
        for r in range(len(zm)):
            query=kw+zm[i]+zm[r]
            html = curl('http://suggestion.baidu.com/su?wd='+ urllib.quote_plus(query)+'&json=2')
            time.sleep(0.2)
            sysHtml = html.decode(sysCharType).encode('utf-8')
            kjson=sysHtml[16:]
            kdict=json.loads(kjson,encoding='UTF-8')
            klist=kdict['s']
            f1 = codecs.open('kwlist.txt', 'a',encoding='UTF-8')
            for l in range(len(klist)):
                f1.write(klist[l]+ '\n')
        print zm[i]+'结束'

print 'ok!!!'
