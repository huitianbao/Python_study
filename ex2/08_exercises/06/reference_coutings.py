# coding:utf8
import sys

if sys.getdefaultencoding() != 'utf-8':
 reload(sys)
 sys.setdefaultencoding('utf-8')

# ________
#
a = "中文编程"
b = a
c = a
a = "python编程"
b = u'%s' % a
d = "中文编程"
e = a
c = b
b2 = a.replace("中","中")
# ________

# 1.请给出str对象"中文编程"的引用计数  程序答案   4
print sys.getrefcount("中文编程")
# 2.请给出str对象"python编程"的引用计数           6

print sys.getrefcount("python编程")

















































































