a = [1,2,3,4,5,6]

# 1 用for if else 的方法查找数字8是否在列表a里，如果在的话，输出字符串'find'，如果不存在的话，

# 输出字符串'not find'
def find_num(x,target):
    flag2=0
    for mm in x:
        if mm==target:
            flag2=1
        else:
            continue
    if flag2==1:
        print("find")
    else:
        print('not find')



find_num(a,8)



# 2 用while语句操作上面的列表a，输出下面结果：
#
# [2,3,4,5,6,7]

def add_y(l,y):
    ll=l.copy()
    count=0
    while(count<=len(ll)-1):
        ll[count]+=y
        count+=1
    return ll
print(a)
print(add_y(a,1))
print(add_y(a,2))
print(add_y(a,3))


# [1, 2, 3, 4, 5, 6]
# [2, 3, 4, 5, 6, 7]
# [4, 5, 6, 7, 8, 9]
# [7, 8, 9, 10, 11, 12]

