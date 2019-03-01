# 1 写一个函数代码，返回这3个数字中最大的一个。
#
a = 123

b = 345

c = 444

def find_main(a,b,c):
    '找到 a,b,c 中最大的'
    return max(a,b,c)

print(find_main(a,b,c))