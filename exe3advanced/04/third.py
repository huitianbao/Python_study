#coding:utf8
# 3 定义一个方法list_info(list), 参数list为列表对象，怎么保证在函数里对列表list进行一些相关的操作，不会影响到原来列表的元素值，比如：

#
# def list_info(list):
#    '''要对list进行相关操作，不能直接只写一句return[1,2,5]，这样就没意义了'''

# print list_info(a):返回结果：[1,2,5]
# print a 输出结果：[1,2,3]
#
# 写出函数体内的操作代码。

def list_info(list):
    list_c=list.copy()
    count=0
    for k in list_c:
        list_c[count]+=1
        count+=1
    return list_c

if __name__=="__main__":
    a = [1, 2, 3]
    print('list_info=',list_info(a))
    print('a        =',a)