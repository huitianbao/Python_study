#coding:utf8
# 1 用lambda和filter完成下面功能：输出一个列表，列表里面包括：1-100内的所有偶数。（提示：可以用filter,lambda）
from pip._vendor.msgpack.fallback import xrange

list_1=[x for x in xrange(1,11) if x%2==0]
print(list_1)
filter_1=filter(lambda x:x%2==0,xrange(1,11))
print(list(filter_1))
print(tuple(filter_1)) #转成 元组不成功
g=lambda x :[(x,i) for i in xrange(1,11)]
print(g(100))
