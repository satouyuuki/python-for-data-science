import datetime
#import time

#now = datetime.datetime.now()
#base = datetime.datetime(1970, 1, 1)
target = datetime.datetime(2022, 10, 21, 21, 37, 37, 362200)
num = target.timestamp()
print(f"Seconds since January 1, 1970: {num:,.4f} or {num:.2e} in scientific notation")
print(target.strftime("%b %d %Y"))
#print(base.timestamp())
#print(target.timestamp())
#result = target - base
#print(result.total_seconds())
#tmp = 1666355857.3622
#Fri Oct 21 21:37:37 2022
#test = time.ctime(tmp)
#print(test)
