# coding:utf8
import sys
print(sys.getdefaultencoding())
# reload(sys)
# sys.setdefaultencoding('utf-8')
#习题7：

# 用字典的方式完成下面一个小型的学生管理系统。
#
#
# 1 学生有下面几个属性：姓名，年龄，考试分数包括：语文，数学，英语得分。
#
#
# 比如定义2个同学：
#
#
# 姓名：李明，年龄25，考试分数：语文80，数学75，英语85
s1={'姓名':'李明','年龄':25}
s1_sorce={'姓名':'李明','语文':80,'数学':75,'英语':85}
#
# 姓名：张强，年龄23，考试分数：语文75，数学82，英语78
s2={'姓名':'张强','年龄':23}
s2_sorce={'姓名':'张强','语文':75,'数学':82,'英语':78}
#
# 2 给学生添加一门python课程成绩，李明60分，张强：80分
s1_sorce.update({'python':60})
s2_sorce.update({'python':80})
print(s1_sorce)
print(s2_sorce)
#
# 3 把张强的数学成绩由82分改成89分
s2_sorce['数学']=89
print(s2_sorce)
#
# 4 删除李明的年龄数据
s1.pop('年龄')
print(s1)
# 5 对张强同学的课程分数按照从低到高排序输出。
s1_sorce.pop("姓名")
print('s1_sorce',s1_sorce)

# def printData(x):
#     for k in x:
#         print(k,x.get(k))
# printData(s1_sorce)
def sortDict(x):
    for k in sorted(x):
        print(k,x[k])


print('='*50)
print("  s1")
print(s1_sorce)
sortDict(s1_sorce)
print('='*50)
print('  s2')
s2_sorce.pop('姓名')
print(s2_sorce)

sortDict(s2_sorce)
print('='*50)




# 6 外部删除学生所在的城市属性，不存在返回字符串 beijing
print(s1.pop('city','beijing'))
print(s2.pop('city','beijing'))