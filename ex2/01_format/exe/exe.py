# coding:utf8

# 1：
#
# a = 'pyer'
#
# b = 'apple'
#
# 用字典和format方法实现：
#
# my name is pyer, i love apple.
#
#
# 2:打开文件info.txt,并且写入500这个数字。

a = 'pyer'
b = "apple"

a1 = 'my name is {name},i love {something}'.format(name="pyer", something="apple")
print 'a1',a1

a2 = 'my name is %(name)s,i love %(something)s' % {'name' :"pyer", 'something' : "apple"}
print 'a2',a2


