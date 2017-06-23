import requests,re
def main():
	num = 0
	for i in range(0,104):
		url = '**sitemap/words_%s.xml'%i
		r = requests.get(url)
		for link in re.findall(r'<loc>(.*?)</loc>',r.content):			
			with open('%s.txt'%i,r'a+' ) as my:
				my.write(link+'\n')
				print link
		print num
		num += 1
main()
