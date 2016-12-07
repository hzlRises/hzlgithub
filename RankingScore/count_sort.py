#coding=utf-8
import operator

f = open("domain.txt")
count_dict = {}
for line in f.readlines():
    line = line.strip()
    count = count_dict.setdefault(line, 0)
    count += 1
    count_dict[line] = count
sorted_count_dict = sorted(count_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
f1 = open('last.txt',r'a+')
for item in sorted_count_dict:
	print "%s,%d" % (item[0], item[1])
	f1.write(item[0]+'>'+str(item[1])+'\n')
f1.close()
