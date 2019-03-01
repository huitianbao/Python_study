# 1.3 请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}

a = "aAsmr3idd4bgs7Dlsf9eAF"
# 把list 类型转成 String类型
def list_to_string(list):
    sum = ''
    for l in list:
        sum = sum + l
    return sum
#去除数字
def remove_digits(x):
    list_xx = list(x)
    count_digits = 0
    while count_digits <= (len(list_xx) - 1):
        if list_xx[count_digits] >= '0' and list_xx[count_digits] <= '9':
            del list_xx[count_digits]
        count_digits += 1
    return list_to_string(list_xx)
#全部先转成小写
def lower_my(x):
    return x.lower()

def getTuple(x):
    a11 = (remove_digits(x))  # a11 是 a 去除了  数字的
    a22 = lower_my(a11)  # a22 是 a 去除了数字 全部小写的
    a33 = list_to_string(list(set(a22)))  # a33 是 a 去除了数字 全部小写的  去除了重复的
    list_t=[]
    for k1 in a33:
        count_33=0
        for k2 in a22:
            if k1==k2:
                count_33+=1
        list_t.append((k1,count_33))
    return list_t

def getDict(x):
    a111 = (remove_digits(x))  # a11 是 a 去除了  数字的
    a222 = lower_my(a111)  # a22 是 a 去除了数字 全部小写的
    a333 = list_to_string(list(set(a222)))  # a33 是 a 去除了数字 全部小写的  去除了重复的
    dict_t={}
    for k1 in a333:
        count_33=0
        for k2 in a222:
            if k1==k2:
                count_33+=1
        dict_t.update({k1:count_33})
    return dict_t

print(getTuple(a))
dict_my=getDict(a)
print(dict_my)
dict_my_sorted=sorted(dict_my,key=lambda x:x[0])

print(dict_my_sorted)