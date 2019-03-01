#coding:utf8
#习题1：

# 列表
a = [11,22,24,29,30,32]

# 1 把28插入到列表的末端
a.append(28)
# 2 在元素29后面插入元素57
a.insert(4,57)
print a
#
# 3 把元素11修改成6
a[0]=6
print a

# 3 删除元素32
del a[-2]
print a
#
# 4 对列表从小到大排序
a.sort()
print a
# 从大到小
a.reverse()
print a
