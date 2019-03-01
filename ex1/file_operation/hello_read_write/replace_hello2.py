#coding:utf8
# 第一种思路 ：
# 1、把文件先用read 读入
# 2、修改指定的字符串
#    利用字符串相关操作即可
# 3、把改完的数据写回原文件

#第二
# 1、找出需要修改的字符串
# 2、统一修改
# 3、写回原文件
import re

fo = open('hello.txt', 'r+')
fo_str = fo.read()
print type(fo_str)
print fo_str
re_fo_str = fo_str.replace('hello', '111111')
print re_fo_str
fo.seek(0, 0)
fo.write(re_fo_str)

# r=r'hello'
# find=re.findall(r,fo_str)
# print find
# print type(find)

fo.close()
