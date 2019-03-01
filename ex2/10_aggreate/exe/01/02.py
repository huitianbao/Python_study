#coding:utf8
# 集合a = set(['a','b','c'])做下面的操作：
# 1 添加字符串'jay'到集合a里。
a = set(['a','b','c'])
a.add('jay')
# print a

# 2 集合b = set(['b','e','f','g']) 用2种方法求集合a 和集合b的并集。
b = set(['b','e','f','g'])
c=a|b
print 'c is',c


def getSum(a, b):
    d = set()
    d = a
    for k in b:
        if (k not in a):
            d.add(k)
    return d


print "getSum(a,b) is ",getSum(a,b)



