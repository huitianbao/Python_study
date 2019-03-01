# 1. 已知字符串
from pip._vendor.msgpack.fallback import xrange

a = "aAsmr3idd4bgs7Dlsf9eAF"
# 要求如下

# 1.1 请将a字符串的大写改为小写，小写改为大写。

# def changeUpLow(x):
#     xx=''
#     for k in x:
#         if k.islower():
#             xx=xx+k.upper()
#         elif k.isupper():
#             xx=xx+k.lower()
#         else:
#             xx=xx+k
#     return xx
# print(a)
# print(changeUpLow(a))

# 1.2 请将a字符串的数字取出，并输出成一个新的字符串。
# def getNum(x):
#     xx=''
#     for k in x:
#         if k.isdigit():
#             xx=xx+k
#     return xx
# print(getNum(a))
# 1.3 请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}
########################################################################################################################
#
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# # 把list 类型转成 String类型
# def list_to_string(list):
#     sum = ''
#     for l in list:
#         sum = sum + l
#     return sum
# #去除数字
# def remove_digits(x):
#     list_xx = list(x)
#     count_digits = 0
#     while count_digits <= (len(list_xx) - 1):
#         if list_xx[count_digits] >= '0' and list_xx[count_digits] <= '9':
#             del list_xx[count_digits]
#         count_digits += 1
#     return list_to_string(list_xx)
# #全部先转成小写
# def lower_my(x):
#     return x.lower()
#
# def getTuple(x):
#     a11 = (remove_digits(x))  # a11 是 a 去除了  数字的
#     a22 = lower_my(a11)  # a22 是 a 去除了数字 全部小写的
#     a33 = list_to_string(list(set(a22)))  # a33 是 a 去除了数字 全部小写的  去除了重复的
#     list_t=[]
#     for k1 in a33:
#         count_33=0
#         for k2 in a22:
#             if k1==k2:
#                 count_33+=1
#         list_t.append((k1,count_33))
#     return list_t
#
# def getDict(x):
#     a111 = (remove_digits(x))  # a11 是 a 去除了  数字的
#     a222 = lower_my(a111)  # a22 是 a 去除了数字 全部小写的
#     a333 = list_to_string(list(set(a222)))  # a33 是 a 去除了数字 全部小写的  去除了重复的
#     dict_t={}
#     for k1 in a333:
#         count_33=0
#         for k2 in a222:
#             if k1==k2:
#                 count_33+=1
#         dict_t.update({k1:count_33})
#     return dict_t
#
# print(getTuple(a))
# dict_my=getDict(a)
# print(dict_my)
# dict_my_sorted=sorted(dict_my,key=lambda x:x[0])
#
# print(dict_my_sorted)
########################################################################################################################

# 1.4 请去除a字符串多次出现的字母，仅留最先出现的一个。例 'abcabb'，经过去除后，输出 'abc'
########################################################################################################################
# s='abcabbddddeeeeeeeeeffffffffffgggggggaaaaa'
# def listToString(list):
#     sum=''
#     for l in list:
#         sum=sum+l
#     return sum
#
#
# def getFirst(input):
#     list_3 = []  # 存放 不断增加的 字符串
#     list_3.append(input[0])
#     for xx in input:
#         if xx in list_3:
#             pass
#         else:
#             list_3.append(xx)
#     return list_3
#
#
# print(listToString(getFirst(s)))

########################################################################################################################
# 1.5 请将a字符串反转并输出。例：'abc'的反转是'cba'
########################################################################################################################
# print(list(a))
# list_a=list(a)
# list_a.reverse()
# print("".join(list_a))
########################################################################################################################
# 1.6 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符 串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）
########################################################################################################################
# 把list 类型转成 String类型
# def list_to_string(list):
#     sum = ''
#     for l in list:
#         sum = sum + l
#     return sum
#
# # 去除String类型中的数字
# def remove_digits(x):
#     list_xx = list(x)
#     count_digits = 0
#     while count_digits <= (len(list_xx) - 1):
#         if list_xx[count_digits] >= '0' and list_xx[count_digits] <= '9':
#             del list_xx[count_digits]
#         count_digits += 1
#     return list_to_string(list_xx)
#
# str_a=remove_digits(a)
# # print(str_a)
# list_str_a=list(str_a)
#
#
# #不区分大小写排序
# def case_insensitive_sort(liststring):
#     listtemp = [(x.lower(), x) for x in liststring]  # 将字符串列表，生成元组，（忽略大小写的字符串，字符串）
#     listtemp.sort()  # 对元组排序，因为元组为：（忽略大小写的字符串，字符串），就是按忽略大小写的字符串排序
#
#     return [x[1] for x in listtemp]  # 排序完成后，返回原字符串的列表
#
#
# print(list_to_string(case_insensitive_sort(list_str_a)))

########################################################################################################################
# 1.7 请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
# s='boy'
# list_boy=list(s)
# print(list_boy)
# flag_b=0
# flag_o=0
# flag_y=0
# for ff in a:
#     if ff=='b':
#         flag_b=1
#     if ff=='o':
#         flag_o=1
#     if ff=='y':
#         flag_y=1
# if flag_b and flag_o and flag_y:
#     print('True')
# else:print('False')

# def charge_isin(x,target):   #x=a,target='boy'
#     list_t=list(target)
#     flag_list=[]  #[0, 0, 0]
#     for f in xrange(len(list_t)):
#         flag_list.append(0)
#
# count=0
#     for tt in target:
#         if tt in x:



######################################################################
# def is_in(x, ta):
#     flag = []
#     for i in xrange(len(ta)):
#         flag.append(0)
#
#     count = 0
#     list_ta = list(ta)
#     for tt in list_ta:
#         # print('tt = ',tt)
#         if tt in x:
#             flag[count] = 1
#         count += 1
#
#     return flag
#
#
# def charge_flag(flag):  # list flag 全是1 才满足要求
#     flag_count = 0
#     for f1 in flag:
#         if f1 == 1:
#             flag_count += 1
#
#     if flag_count < len(flag):
#         return False
#     if flag_count == len(flag):
#         return True
#
#
# def print_my(x, ta):
#     bool_my = charge_flag(is_in(x, ta))
#     if bool_my:
#         print("%s 在 %s 中" % (ta, x))
#     else:
#         print("%s 不在 %s 中" % (ta, x))
#
# print_my(a,'boy')


# 1.8 要求如1.7，此时的单词判断，由'boy'改为四个，分别是 'boy','girl','bird','dirty'，请判断如上这4个字符串里的每个字母，是否都出现在a字符串里。
# print_my(a,'girl')
# print_my(a,'bird')
# print_my(a,'dirty')

# 1.9 输出a字符串出现频率最高的字母
########################################################################################################################
#去除数字
# a = "aAsmr3idd4bgs7Dlsf9eAF"
# # 把list 类型转成 String类型
# def list_to_string(list):
#     sum = ''
#     for l in list:
#         sum = sum + l
#     return sum
# # 去除String类型中的数字
# def remove_digits(x):
#     list_xx = list(x)
#     count_digits = 0
#     while count_digits <= (len(list_xx) - 1):
#         if list_xx[count_digits] >= '0' and list_xx[count_digits] <= '9':
#             del list_xx[count_digits]
#         count_digits += 1
#     return list_to_string(list_xx)
#
# #不区分大小写排序
# def case_insensitive_sort(liststring):
#     listtemp = [(x.lower(), x) for x in liststring]  # 将字符串列表，生成元组，（忽略大小写的字符串，字符串）
#     listtemp.sort()  # 对元组排序，因为元组为：（忽略大小写的字符串，字符串），就是按忽略大小写的字符串排序
#
#     return [x[1] for x in listtemp]  # 排序完成后，返回原字符串的列表
#
#
# # 去除 list中 重复的字母
# def duplicate_removal(list_c):
#     return list(set(list_c))
#
# def find_frequency(a):
#     # 首先去重，放到一个list1中
#     list1=duplicate_removal(list(remove_digits(a)))
#     # 然后统计每个字母出现的次数放到list2中
#     list2 = []
#     for k in list1:
#         list2_count = 0
#         for aa in a:
#             if aa == k:
#                 list2_count += 1
#         list2.append((k, list2_count))
#     list2.sort(key=lambda x: x[1])
#     return list2[-1][0]
#
#
# print(find_frequency(a))
########################################################################################################################