# coding:utf8
import sys
import string


# print myname.decode('UTF-8').encode(type)
if sys.getdefaultencoding() != 'utf-8':
 reload(sys)
 sys.setdefaultencoding('utf-8')

# a = "字符串拼接1"
# b = "字符串拼接2"


# 1
a = "字符串拼接1"
b = "字符串拼接2"

s1 = a + b
s2 = "".join([a, b])
s3 = "%s%s" % (a, b)
s4 = "{}{}".format(a, b)

s5 = "{a}{b}".format(a=a, b=b)

print 's1:', s1
print 's2:', s2
print 's3:', s3
print 's4:', s4
print 's5:', s5

# 2.请将a与b拼接成字符串c，并用逗号分隔。
c = ','.join([a, b])
print 'c is ', c
print "type(c)   =  ", type(c)
print len(c)
c[6].decode('gb2312')
# print c.index(6)
print c[6]



