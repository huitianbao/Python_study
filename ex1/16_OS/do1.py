#coding:utf8
import os

def getCurrentPath(filename):
    return os.listdir(filename)




def getTotalPath(filename):
    # FirstPath=os.getcwd()
    SecondPath=getCurrentPath(filename)


def getRelativePath(filename):
    temp1=getCurrentPath(filename)
    if temp1!=None:

        for k in temp1:
            getRelativePath(k)





print getCurrentPath("D/a/a1/a1.txt")


# 获取当前层的文件列表
# def getCurrentPath(filename):
#     print os.listdir(filename)
#     print type(os.listdir(filename))






