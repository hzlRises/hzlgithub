#coding:utf-8
#import numpy as np
import matplotlib.pyplot as plt
x = range(20)
y = []
num = 200
for i in x:	
	y.append(num)
	num = num*1.1
	print num
y2 = [40*i for i in x]
	
plt.plot(x,y)
plt.plot(x,y2)
plt.show()
