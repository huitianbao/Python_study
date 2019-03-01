# 1 用while语句的2种方法输出数字：1到10
from pip._vendor.msgpack.fallback import xrange

k=1
while(k>0 and k<11):
    print(k),
    k+=1

# 2 用for语句和continue 输出结果：1 3 5 7 9

for k in xrange(1,10):
    if k&1==0:
        continue

    print(k),



