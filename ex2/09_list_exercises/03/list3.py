#coding:utf8
# 三 有下面2个列表：
#
# a = [1,99,33,44,55,22]
#
# 输出结果:
#
# 1：[1,2,99,33,44,55,22,(11,33,54)]


# 2: [1,2,99,33,101,44,55,22]



a = [1,99,33,44,55,22]

a.insert(1,2)


t=(11,33,54)
print a.append(t)

a = [1,99,33,44,55,22]
a.insert(1,2)
a.insert(4,101)
print a
