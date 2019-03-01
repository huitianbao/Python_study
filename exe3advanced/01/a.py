#coding:utf8
'this is a  __doc__aaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

import glob
def func(*k):
    '该func可以引入任意多的整型参数，结果返回其中最大与最小的值'
    # print(type(k))
    # list_1=list(k)
    for kk in k:
        
    max_k=max(k)
    min_k=min(k)
    dict_1={}
    dict_1.update({'max':max_k,'min':min_k})

    return dict_1

# print (func(7777,8888888,-2,1,2,3))


# 2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。
def func2(*k):
    '该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串'
    list_k=list(k)
    list_len=[]
    list_re=[]
    for kk in list_k:
        list_len.append(len(kk))
    max_len=max(list_len)
    for mm in list_k:
        if len(mm)==max_len:
            list_re.append(mm)
    return list_re

# print(func2("shdv","hjjl"))


# 3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。
# def get_doc(module):
def get_doc(moudle):
    return moudle.__doc__



# 4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。
def get_text(f):
    fo=open(f)
    str_fo=fo.read()
    fo.close()
    return str_fo

# 5.定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。提示（可以了解python的glob模块）
def get_dir():
    listglob = glob.glob(r'E:\pythoncodenew\exe3advanced\01\*')
    for k in listglob:
        print(k)

    return 'end'


if __name__=='__main__':
    print(func(7777, 8888888, -2, 1, 2, 3))
    print(func2("shdv", "hjjl"))
    path="""E:\pythoncodenew\exe3advanced\\01\\02.py"""
    print(get_text(path))

    print(get_dir())