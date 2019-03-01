# 一：定义一个学生类。有下面的类属性：
#
# 1 姓名
# 2 年龄
# 3 成绩（语文，数学，英语)[每课成绩的类型为整数]
#
# 类方法：
#
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高的分数。get_course() 返回类型:int

class Stu(object):
    def __init__(self,name,age,list_score):

        #检查姓名
        if isinstance(name,str):
            self.name = name
        else:
            print('输入的名字有问题')
        #检查年龄
        if isinstance(age,int) and age>=0 and age<=200:
            self.age = age
        else:
            print('%s 输入的年龄有问题' % self.name)



        #检查分数
        flag=[]
        for k in list_score:
            if isinstance(k,int):
                flag.append(0)
            else:
                flag.append(1)
        if max(flag)==0:
            self.list_score=list_score
        else:
            print('%s 输入的分数有问题' % self.name)




    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

    def get_course(self):
        ' 返回 成绩最高分'
        return max(self.list_score)



zm = Stu('zhangming',20,[69,88,100])
lq = Stu('liqiang',23,[82,60,99])
print(zm.get_name())
print(zm.get_age())
print(zm.get_course())
print('*'*50)

print(lq.get_name())
print(lq.get_age())
print(lq.get_course())
#
# 写好类以后，可以定义2个同学测试下:
#
# zm = student('zhangming',20,[69,88,100])
# 返回结果：
# zhangming
# 20
# 100
#
# lq = student('liqiang',23,[82,60,99])
#
# 返回结果：
# liqiang
# 23
# 99