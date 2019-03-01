# 2.2 调用函数：cinfo(x=88,y=22,z=44) 你定义cinfo函数体里面的内容并且返回结果：
#
# ('xaay','yaay','zaay')
dict_1={88:'xaay',22:'yaay',44:'zaay'}

def cinfo(**kwargs):
    dict_2=dict(kwargs)
    list_1=list(dict_2.values())
    list_2=[]
    for k in list_1:
       list_2.append(dict_1[k])

    return tuple(list_2)

print(cinfo(x=88,y=22,z=44))
