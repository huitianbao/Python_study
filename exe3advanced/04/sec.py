#coding:utf8
# 2 定义一个方法get_cjsum(),求1-100范围内的所有整数的平方和。返回结果为整数类型。
from pip._vendor.msgpack.fallback import xrange

def get_cjsum(x,y):
    '求1-100范围内的所有整数的平方和。返回结果为整数类型'
    if(str(x).isdigit() and str(y).isdigit() and x>0 and y<101):
        sum = 0
        for k in xrange(x, y + 1):
            sum = k ** 2 + sum

        return sum
    else:
        return "输入有误，请重新输入"

print(get_cjsum(1,100))
# print(str(type(1)))






