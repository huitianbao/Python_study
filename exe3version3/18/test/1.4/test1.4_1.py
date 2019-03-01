# 1.4 请去除a字符串多次出现的字母，仅留最先出现的一个。例 'abcabb'，经过去除后，输出 'abc'

s='abcabbddddeeeeeeeeeffffffffffgggggggaaaaa'
def listToString(list):
    sum=''
    for l in list:
        sum=sum+l
    return sum


def getFirst(input):
    list_3 = []  # 存放 不断增加的 字符串
    list_3.append(input[0])
    for xx in input:
        if xx in list_3:
            pass
        else:
            list_3.append(xx)
    return list_3


print(listToString(getFirst(s)))
