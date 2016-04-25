#coding:utf-8
import re,urllib2
url = 'http://zhishi.fang.com/sitemap_pc_jiaju_zhishi.xml'
sitemapUrl = urllib2.urlopen(url).read()
pattren = re.compile('<loc>(.*?)</loc>')
link = pattren.findall(sitemapUrl)
#print type(link)	<type 'list'>
f = open('url.txt',r'w')
f.writelines(line.strip()+'\n' for line in link)
f.close
#ceshi