# coding:utf8
import os


# 递归函数

def getTotalOath(path):
    current = os.getcwd()

    listmy = os.listdir(path)
    for k in listmy:
        if os.path.isdir(current + '\\' + path + '\\' + k):
            print current + '\\' + path + '\\' + k
            getTotalOath(current + '\\' + path + '\\' + k)
        else:
            print current + '\\' + path + '\\' + k


def getTotalOath2(path):
    current = os.getcwd()

    listmy = os.listdir(path)
    for k in listmy:
        if os.path.isdir(path + '\\' + k):
            print current + '\\' + path + '\\' + k
            getTotalOath(path + '\\' + k)
        else:
            print k+"hhhhhhhhh"


# getTotalOath("D")
getTotalOath2("D")
