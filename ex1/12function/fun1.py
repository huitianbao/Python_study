# coding:utf8
from __future__ import division

#=========================================================================
# 这是一个简单地函数
# def fun():
#     print 'hello world'
#
# fun()

#=========================================================================
# 测试返回值
# def fun():
#     return "htb"
#
# z=fun()

# print z

#=========================================================================
#测试传入参数
# 1 简单地单一参数


# def fun(x):
#     print 'this is 传入的形参 x= ',x
#
#
#
# fun('htb')
# print '~'*50
# fun((1,2))
# print '~'*50
# fun({'name':'htb','age':20})

#=========================================================================

# 2 简单的多个参数

# def fun(x,y):
#     print 'this is ',x,'this is ',y
#
# fun(1,2)
# fun('htb',25)
# print '~'*50
# fun((1,2),(3,4))
# print '~'*50
# fun({'name':'htb','age':20},{})

#=========================================================================
# 3  关于参数的几个注意

   #（1）传入一个元组，但是访问元组里的多个数据
   #     用 *t

#=========================================================================
# def fun(x,y):
#     print 'tuple1 =',x
#     print 'tuple2 =',y
#
#
# t=('htb','帅')
# fun(*t)


#=========================================================================
#    (2)传入一个  队列  []      传入对列的时候  还是用的   *l

#    或者   字典  dict   传入字典的时候用     **d

# l=['htb','帅']
# def fun(x,y):
#   print 'tuple1 =',x
#   print 'tuple2 =',y
#
# fun(*l)


#=========================================================================

#     (3)  传入   字典的  时候用     ** d
#并且传入字典的时候要注意，形参的名称要和  字典的  key  相匹配，否则报错

# dictmy={'name':'htb','age':18}
# def fun(name,age):
#   print 'my name is ',name
#   print 'my age  is ',age
#
# fun(**dictmy)

#=========================================================================

#   参数的  冗余


# def fun(x,*args):
#     print x
#     print args
#
#
#
# fun(1,2,3,4,5)


dictmy1={'name':'htb1','age':24}
dictmy2={'name':'htb2','age':18}
dicttest={'test':'dataghjkl'}
list1=['l_htb1','l_24']
list2=['l_htb2','l_18']
def fun(x,y,*args,**dictargs):
    print 'this is ',x
    print 'this is ', y
    print 'this is ',args
    print 'this is ',dictargs



# fun(list1,'list1_after')
# print '='*50
# fun(list2,'list2_after')



#fun(dictmy1,'dictmy1_after')
print '='*50
fun(dictmy1,dictmy2,'hjkl;nm,.mkllkl;kl''nvdfnsdvdvdso',dicttest,z=2222,tt='iiiii')
