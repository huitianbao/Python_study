#coding:utf8
# 一 元组；a = (1,2,3)
#
# 有2种方法输出实现下面的结果：
#
# (5,2,3)


a=(1,2,3)
b=list(a)
print b
b[0]=5
print tuple(b)


q1=set(a)
q1.remove(1)
q1.add(5)
t1=tuple(q1)
print 'q1 =  ',q1
print 't1 =  ',t1


# 判断2是否在元组 a 里
print '2 is in (1,2,3) :' ,2 in a