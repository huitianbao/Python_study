#coding:utf8
# 已知元组:
a = (1,4,5,6,7)
#
#
# 1 判断元素4是否在元组里
print 4 in a
#
# 2 把元素5修改成8
b=list(a)
b[2]=8
a=tuple(b)
print a
