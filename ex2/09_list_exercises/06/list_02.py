# coding:utf8
# 二: 利用列表推导完成下面习题：
#
# 1 输出结果：[1 love python,2 love python,3 love python,.... 10 love python]
print ["%d love python" % x for x in xrange(1,11)]
# print [x for x in range(1,10)]
# 2 输出结果：[(0,0),(0,2),(2,0),(2,2)]
print [(x,y) for x in xrange(0,3) for y in xrange(0,3) if x%2==0 and y%2==0]
