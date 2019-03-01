#coding:utf8
import string

def func(name,callback=None):
    if isinstance(name,str):
        if callback==None:
            return name.capitalize()
        else:
            return callback(name)
    else:
        print('输入有误，请重新输入')


assert func('lilei')=='Lilei'
# assert func('lilei',str.upper())=='LILEI


#此方法   string.upper    python 2   有用，Python 3  没用
print(func('lilei',string.upper))