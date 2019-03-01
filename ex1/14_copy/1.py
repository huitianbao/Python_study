

import copy
# a = ['a1', 'a2']
# b = a
#
# print 'this is a =', a
# print 'this is b =', b
#
# print 'id a', id(a)
# print 'id b', id(b)
# a.append('...a3')
# print 'this is a =', a
# print 'this is b =', b
#
# print 'id a', id(a)
# print 'id b', id(b)







a = ['a1', 'a2',[1,2,3]]
b=copy.copy(a)
print 'this is a',a
print id(a)

print id(a[0])
print id(a[1])
print id(a[2])
print 'this is b',b
print id(b)
print id(b[0])
print id(b[1])
print id(b[2])

d=copy.deepcopy(a)

print 'this is d',d
print id(d)
print id(d[0])
print id(d[1])
print id(d[2])

print '='*50
a[2].append(4)
print 'this is a',a
print 'this is d',d
print 'this is b',b

