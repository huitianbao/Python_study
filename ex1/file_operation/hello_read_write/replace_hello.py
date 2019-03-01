#coding:utf8
import re

file_open=open('hello.txt','r+')
print type(file_open.readlines())
file_open.seek(0,0)
s= file_open.readlines()

sum=0
#统计每行里面的  hello个数
count=0
kk=1
r=r'hello'
for k in s:
    print '='*50
    print '第 ',kk,'行'
    kk+=1
    print k
    print '=' * 50
    find=re.findall(r,k)
    print 'find is ', find

    if find !=None:
        #改变值
        pass
        #写回文件
    file_open.write()













file_open.close()
