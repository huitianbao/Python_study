#coding:utf8
# 2 用位置匹配，关键字匹配，收集匹配(元组收集,字典收集)分别写4个函数，完成功能；
# 传递3个列表参数：
# [1,2,3],[1,5,65],[33,445,22]
# 返回这3个列表中元素最大的那个，结果是：445

def find_max_local(list_1,list_2,list_3):
    '用位置匹配收集三个list 找到 list中最大的数字，返回'
    if isinstance(list_1,list) and isinstance(list_2,list) and isinstance(list_3,list):

        list_max = []
        list_max.append(max(list_1))
        list_max.append(max(list_2))
        list_max.append(max(list_3))
    else:
        return "输入参数有误，请重新输入"

    return max(list_max)




if __name__=="__main__":
    # print(find_max_local())
    print([])

# print(isinstance([],type([])))
# print(isinstance([],list))
# print(type([]))