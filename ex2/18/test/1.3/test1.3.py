# 1.3 请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}

a = "aAsmr3idd4bgs7Dlsf9eAF"
#去除数字
# 把list 类型转成 String类型
def list_to_string(list):
    sum = ''
    for l in list:
        sum = sum + l
    return sum
# 去除String类型中的数字
def remove_digits(x):
    list_xx = list(x)
    count_digits = 0
    while count_digits <= (len(list_xx) - 1):
        if list_xx[count_digits] >= '0' and list_xx[count_digits] <= '9':
            del list_xx[count_digits]
        count_digits += 1
    return list_to_string(list_xx)

print('a is',a)
str_a=list_to_string(remove_digits(a))
print('去除数字的 a ',str_a)

list_str_a=list(set(str_a))
print('去重的 a',list_str_a)
list_22=[]
#全部先转成小写
def lower_my(x):
    return x.lower()

#小写的去除数字的   a
aa=lower_my(list_to_string(list_str_a))
list_str_a_lower=lower_my(aa)
print('list_str_a_lower',list_str_a_lower)
for k in list_str_a_lower:
    count_22 = 0
    for mmm in a:
        if k==mmm:
            count_22+=1
    list_22.append((k,count_22))

print('list_22',list_22)



