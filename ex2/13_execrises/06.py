# coding:utf8
# 已知集合:
setinfo = set('acbdfem')
finfo = set('sabcdef')
#完成下面操作：
#
# 1 添加字符串对象'abc'到集合setinfo
setinfo.add('abc')
print setinfo
# 2 删除集合setinfo里面的成员m
setinfo.remove('m')
print setinfo
#
# 3 求2个集合的交集和并集
print '交集',setinfo&finfo
print '并集',setinfo|finfo