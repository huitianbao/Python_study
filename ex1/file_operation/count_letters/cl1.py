op=open('1.txt','r')
str_op=op.read()
print type(str_op)

c_a=0
c_A=0
for k in str_op:
    if k.__eq__(" ") or k.__eq__("."):
        continue

    if k.__eq__('a'):
        c_a+=1
    if k.__eq__('A'):
        c_A+=1



print 'a is ',c_a
print 'A is ',c_A