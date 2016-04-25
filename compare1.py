from base import *

kws = {}
for line in open(sys.argv[1]):
	        kws[line.rstrip()] = 0

for line in open(sys.argv[2]):
					kw, s = line.rstrip().split('\t')
					if kw in kws:
							kws[kw] = s

for kw, s in kws.iteritems():
				print '%s\t%s' % (kw, s)
