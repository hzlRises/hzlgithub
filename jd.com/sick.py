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
