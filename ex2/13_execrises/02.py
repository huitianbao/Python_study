#coding:utf8
#习题2：
# 列表
b = [1,2,3,4,5]

# 1 用2种方法输出下面的结果：
#
# [1,2,3,4,5,6,7,8]
# b.append(6)
# b.append(7)
# b.append(8)
# print b
c=[6,7,8]
print 'b+c=',b+c

#
#
#
# 2 用列表的2种方法返回结果：[5,4]
print b[-1:2:-1]
e=b[3:5]
e.reverse()
print e


# 3 判断2是否在列表里
print 2 in b