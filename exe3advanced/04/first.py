#coding:utf8
'''1 定义一个方法get_fundoc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，
如果该函数没有描述文档，则返回"not found"'''
import os
import sys
def get_fundoc(func):
    ro=os.popen(help(func))
    content=sys.stdout
    c=ro.__doc__

    return c

print(get_fundoc('str'))



