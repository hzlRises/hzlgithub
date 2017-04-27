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
'''
写matplotlib这个的demo源于在网上看到一个有意思的面试题，面试题是这样的：“在北京某地段，一位软件工程师看中了一套房子，售价是200万。
不过，以目前工程师的收入还买不起，只好观望。假设房价每年上涨10%，工程师每年固定能赚40万。
他想买这套房子，不贷款，不涨工资，也没有其他收入，每年不吃不喝不消费，那么他需要几年才能攒够钱买这套房子？”

当时心里一琢磨，列个方程式不就出来了，设x年以后可以买的起，方程式是这样的 ：“40x = 200(1+10%)x”，
然后就懵逼了，一元高次方程，不会解，于是打算用matplotlib画个函数图，两条曲线的交点，就是最后的方程解。先暂且设定x为20

至于结果如何，懂的老铁自然懂

'''
