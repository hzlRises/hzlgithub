import ahocorasick
import time
def main():
	t1 = time.time()
	A = ahocorasick.Automaton()
	#向trie树中添加单词
	with open("blackword.txt",'r') as fp:
		for line in fp:
			bkw = line.strip()
			A.add_word(bkw,(1,bkw))
	#将trie树转化为Aho-Corasick自动机
	A.make_automaton()
	g1 = open("result_dangdang.txt", 'a+')
	for line in open("dangdang.txt"):
		for k,(i,t) in A.iter(line.strip()):
			print line.strip()+t
			g1.write(line.strip()+":"+t+"\n")
	g1.close()
	t2 = time.time()
	print "cost time is ", t2 - t1
main()
'''
import ahocorasick
A = ahocorasick.Automaton()
for index,word in enumerate("he her hers she".split()):
    A.add_word(word, (index, word))
A.make_automaton()
for item in A.iter("_yywwt_"):
    print item
#(2,(0,'he'))
#(3,(1,'her'))
#(4, (2, 'hers'))
#(6, (3, 'she'))
#(6, (0, 'he'))

'''


'''
import ahocorasick
import time
def main():
    t1 = time.time()
    A = ahocorasick.Automaton()
    with open("D:\\seo-dev\\blackword\\blackword.properties", 'r') as fp:
        for line in fp:
            tok = line.strip("\n").split("\t")
            if len(tok) < 1:
                print line.decode('utf-8')
            else:
                A.add_word(tok[0], (1, tok[0]))
    A.make_automaton()
    f1 = open("D:\\seo-dev\\blackword\\back_dangdang.csv", 'w')

    g1 = open("D:\\seo-dev\\blackword\\result_dangdang.csv", 'w')
    
    cnt = 0
    for line in open("D:\\seo-dev\\blackword\\dangdang.csv", 'r'):
        cnt += 1
        if cnt % 10000 == 0:
            print cnt
        tok = line.strip("\n").split(",")
        kw = tok[7]
        media = tok[0]
        good = True
        for k,(i,t) in A.iter(kw):
            if i == 2 and t != kw:
                continue
            tok.append(t)
            line = ",".join(tok) + "\n"
            f1.write(line)
            good = False
            break

        if good:
            line = ",".join(tok) + "\n"
            g1.write(line)
    f1.close()
    g1.close()
    t2 = time.time()
    print "cost time is ", t2 - t1
    return

main()
'''
