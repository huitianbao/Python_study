# 2. 已知字典：
#
ainfo = {'b':'python','a':'haha','c':'hehe','f':'xiaoming'}
# 2.1 迭代字典，输出结果：
#
# ('a', 'haha')
# ('c', 'hehe')
# ('b', 'python')
# ('f', 'xiaoming')


# 2.2 用2种方法输出结果：
#
# a
# c
# b
# f
# list_values=ainfo.values()
# list_keys=ainfo.keys()
#
# print(type(list_values))
# print(type(list_keys))
# for k,y in ainfo.items():
#     print(k)
# 2.3 写出查找字典里面值等于'haha'的key的代码

def find_key(dict,value):
    answer_k=''
    for k,v in dict.items():
        if v==value:
            answer_k=k
    return answer_k

print('the key of haha is ',find_key(ainfo,'haha'))


