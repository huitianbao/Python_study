#coding:utf8
"""
2.定义一个func(name,callback=None),效果如下。
assert func("lilei") == "Lilei"
assert func("LILEI",callback=string.lower) == "lilei"
assert func("lilei",callback=string.upper) == "LILEI"

"""
import string


def func(name,callback=None):
    if callback==None:
        return str.capitalize(name)
    elif callback==string.lower:
        ss= str.lower(name)
        return ss
    elif callback==string.upper:
        ss=str.upper(name)
        return ss




print(func('lilei'))
assert func("lilei") == "Lilei"
assert func("LILEI",callback=string.lower) == "lilei"
assert func("lilei",callback=string.upper) == "LILEI"






# ss='string.lower'
# s=str.replace(ss,'ing','')
# print(s)