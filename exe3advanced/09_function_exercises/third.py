#coding:utf8
"""
3.定义一个func(*kargs),效果如下。

l = func(1,2,3,4,5)
for i in l:
	print i,
#输出 1 2 3 4 5

l = func(5,3,4,5,6)
for i in l:
	print i
#输出 5 3 4 5 6


"""
def func(*kargs):
    for k in kargs:
        print(k)



func(1,2,3,4)