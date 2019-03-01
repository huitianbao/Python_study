#coding:utf8
##习题3：
b = [23,45,22,44,25,66,78]
#
# 用列表解析完成下面习题：
#
#
# 1 生成所有奇数组成的列表
print [x for x in b if x%2==1]
#
# 2 输出结果: ['the content 23','the content 45']
print ['the cotent %s' % b[x] for x in xrange(2) ]
#
# 3 输出结果: [25, 47, 24, 46, 27, 68, 80]
for x in xrange(len(b)):
    b[x]+=2
print b