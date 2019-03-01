#coding:utf8

'''
1.定义一个func(name)，该函数效果如下。
assert func("lilei") = "Lilei"
assert func("hanmeimei") = "Hanmeimei"
assert func("Hanmeimei") = "Hanmeimei"
'''

def func(name):
    return str.capitalize(name)



print(func('fffffff'))

assert func('lilei')=='Lilei'
assert func("hanmeimei") == "Hanmeimei"
