# 1.6 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），
# 并且重新输出一个排序后的字符串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）

a = "aAsmr3idd4bgs7Dlsf9eAF"

list_1=[x for x in list(a) if not x.isdigit()]
list_2=[(x,x.lower()) for x in list_1]

list_2.sort(key=lambda x:x[1])

list_answer=[x[0] for x in list_2]


