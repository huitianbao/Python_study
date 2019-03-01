#coding:utf8
# 计算  1 ++ 100

# def fun(x):
# #     if x==0:
# #         return 0
# #     elif x==1:
# #         return 1
# #     else:
# #         return fun(x-1)+x
# #
# # print fun(0)
# # print fun(1)
# # print fun(100)

# 计算斐波那契

def fun2(x):
    if x==1:
        return 1
    elif x==2:
        return 2
    else:
        return fun2(x-1)+fun2(x-2)


print fun2(4)