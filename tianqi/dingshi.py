import time,os
while True:
    current_time = time.localtime(time.time())
    if((current_time.tm_hour == 7) and (current_time.tm_min == 0) and (current_time.tm_sec == 0)):
		print "Hello World"
		os.system("python go.py")
    time.sleep(1)
'''
print current_time//time.localtime(time.time())

time.struct_time(tm_year=2018, tm_mon=4, tm_mday=1, tm_hour=16, tm_min=55, tm_sec=38, tm_wday=6, tm_yday=91, tm_isdst=0)



time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

'''
