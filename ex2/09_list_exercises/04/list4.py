#coding:utf8
# 用列表推导式生成100内的大于20的偶数

print [x for x in range(1,101) if (x>20) and (x%2==0)]

