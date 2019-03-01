#coding:utf8
"""
5.定义一个func(name=None,**kargs),该函数效果如下。

assert func(“lilei”) == "lilei"
assert func("lilei",years=4) == "lilei,years:4"
assert func("lilei",years=10,body_weight=20) == "lilei,years:4,body_weight:20"

"""

def func(name=None,**kwargs):
    print(name+','),
    # count=0
    sum=''
    for k in kwargs.keys():
        # sum=sum+k+kwargs[k]+','
        ','.join([sum,k,kwargs[k]])


    return name+','+sum

# print(func('lilei'))
# func("lilei",years=4)
func("lilei",years=10,body_weight=20)






