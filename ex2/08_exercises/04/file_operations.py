# coding:utf8
import linecache
import sys

# 四.已知一个文件
# test.txt，内容如下：
#
# ____________
# 2012
# 来了。
# 2012
# 不是世界末日。
# 2012
# 欢乐多。
# _____________
#
# 1.
# 请输出其内容。

# for k in linecache.getlines('test_u.txt'):
#     print k


# 2.
# 请计算该文本的原始长度。
fo = open('test_u.txt', "r+")
read_fo = fo.read()
# print len(read_fo)
# 3.
# 请去除该文本的换行。
# fo.seek(0)
# print type(read_fo)
# new_context=read_fo.replace("\n",'')
# fo.seek(0)
# fo.write(new_context)


# 4.
# 请替换其中的字符
# "2012"
# 为
# "2013"。

# new_context2 = read_fo.replace("2012", "2013")
# fo.seek(0)
# fo.write(new_context2)

# 5.
# 请取出最中间的长度为5的子串。
# 6.
# 请取出最后2个字符。
# strmy=read_fo[len(read_fo)-2:]
# print strmy
# 7.
# 请从字符串的最初开始，截断该字符串，使其长度为11.
#截取前11 个字符
# s1=read_fo[:11]
# print 's1',s1,'len s1',len(s1)
# #截取后11 个字符
# s2=read_fo[len(read_fo)-11:]
# print 's2',s2,'len s2',len(s2)

# 8.
# 请将{4}中的字符串保存为test1.py文本.

fo.close()

fo_1=open("test_u.txt","r+")
fo_2=open('test1.py','w')
fo_2.write(fo_1.read())

fo_1.close()
fo_2.close()
