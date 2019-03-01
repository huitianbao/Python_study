def sort_lower(liststring):
    listtemp = [(x.lower(), x) for x in liststring]  # 将字符串列表，生成元组，（忽略大小写的字符串，字符串）
    # print(listtemp)
    listtemp.sort()  # 对元组排序，因为元组为：（忽略大小写的字符串，字符串），就是按忽略大小写的字符串排序

    return [x[1] for x in listtemp]  # 排序完成后，返回原字符串的列表


def sort_upper(liststring):
    listtemp = [(x.upper(), x) for x in liststring]  # 将字符串列表，生成元组，（忽略大小写的字符串，字符串）
    # print(listtemp)
    listtemp.sort()  # 对元组排序，因为元组为：（忽略大小写的字符串，字符串），就是按忽略大小写的字符串排序

    return [x[1] for x in listtemp]  # 排序完成后，返回原字符串的列表
a = "aAsmriddbgsDlsfeAF"
print(a)
print(sort_lower(a))
print(sort_upper(a))
