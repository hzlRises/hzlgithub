import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')	
author = 'heziliang'
item = 1
f = open('item_%s.xml' % item, r'a+')
f_index = open('index_item.xml',r'a+')
f_index.write('<?xml version="1.0" encoding="utf-8"?>'+'\n')
f_index.write('<sitemapindex>'+'\n')
for i, line in enumerate(open('urls.txt')):	
	if i % 50000==0:
		print i
		f.write('<?xml version="1.0" encoding="utf-8"?>'+'\n')
		f.write('<urlset>'+'\n')
	f.write(' '+'<url>'+'\n')
	f.write('  '+'<loc>'+line.strip()+'</loc>'+'\n')
	f.write('  '+'<lastmod>'+str(datetime.date.today())+'</lastmod>'+'\n')
	f.write('  '+'<changefreq>daily</changefreq>'+'\n')
	f.write('  '+'<priority>1.0</priority>'+'\n')
	f.write(' '+'</url>'+'\n')
	if i % 50000==49999:
		f.write('</urlset>')		
		f.close()
		f_index.write(' '+'<sitemap>'+'\n')
		f_index.write('  '+'<loc>item_%s.xml</loc>'%item+'\n')
		f_index.write('  '+'<lastmod>'+str(datetime.date.today())+'</lastmod>'+'\n')
		f_index.write(' '+'</sitemap>'+'\n')
		item += 1
		f = open('item_%s.xml' % item, r'a+')
f.write('</urlset>')
f.close()
f_index.write('</sitemapindex>')
f_index.close()
