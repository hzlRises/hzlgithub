import time,os
while True:
    current_time = time.localtime(time.time())
    if((current_time.tm_hour == 7) and (current_time.tm_min == 0) and (current_time.tm_sec == 0)):
		print "Hello World"
		os.system("python go.py")
    time.sleep(1)
