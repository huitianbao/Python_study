# 提示一下用到函数的：**和*，猩猩是字典，星是元组
#
# 2.1 调用函数：ainfo(x=88,y=22,z=44) 你定义ainfo函数体里面的内容并且返回结果：
#
# [22, 44, 88]

def ainfor(**z):
    return list(z.values())

print(ainfor(x=88,y=22,z=44))