# 二：定义一个字典类：dictclass。完成下面的功能：
[(k1,v1),(k2,v2),(k3,v3)]
然后把 [] 变成 {}
即可
# dict = dictclass({你需要操作的字典对象})
# 1 删除某个key
# del_dict(key)
#
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
# get_dict(key)
#
# 3 返回键组成的列表：返回类型;(list)
# get_key()
#
# 4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
# update_dict({要合并的字典})

class dictclass(object):
    def __init__(self,key_list,value_list):
        self.key_list=key_list
        self.value_list=value_list


    def del_dict(self,key):
        del self.value_list
        del self.key_list[key]





