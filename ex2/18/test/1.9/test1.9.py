#去除数字
a = "aAsmr3idd4bgs7Dlsf9eAF"
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
print(a)
str_a=remove_digits(a)
print(str_a)


#不区分大小写排序
def case_insensitive_sort(liststring):
    listtemp = [(x.lower(), x) for x in liststring]  # 将字符串列表，生成元组，（忽略大小写的字符串，字符串）
    listtemp.sort()  # 对元组排序，因为元组为：（忽略大小写的字符串，字符串），就是按忽略大小写的字符串排序

    return [x[1] for x in listtemp]  # 排序完成后，返回原字符串的列表
print(list_to_string(case_insensitive_sort(str_a)))

# 想法  把排序完成的   字符串  想办法 拆分成 元组 或者list  相同的字母 放到同一个元组中
#  然后看每个元组的长度，最长的就是频率最高的



'''
想法 2  是这样的
首先去重，放到一个  list1 中
然后统计每个 字母出现的次数
放到 list2 中 
取出 max(list2)对应的 index
到 list 1   中取字母
'''