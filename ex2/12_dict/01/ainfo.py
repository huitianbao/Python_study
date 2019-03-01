#coding:utf8
# 字典习题:
#
# 已知字典：
ainfo = {'ab':'liming','ac':20}

# 完成下面的操作
#
# 1 使用2个方法，输出的结果：
#
# ainfo = {'ab':'liming','ac':20,'sex':'man','age':20}
#    1
# ainfo['sex']='man'
# ainfo['age']=20
# print ainfo
#   2
# ainfo.update({'sex':'man','age':20})
# print ainfo
# 2 输出结果：['ab','ac']
# print ainfo.keys()

# 3 输出结果：['liming',20]
# print ainfo.values()
# 4 通过2个方法返回键名ab对应的值。
# print ainfo['ab']
# print ainfo.get('ab')
# 5 通过2个方法删除键名ac对应的值。
print ainfo
# ainfo.pop('ac')
# del ainfo['ac']

print ainfo


