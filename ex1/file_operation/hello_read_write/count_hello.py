import re
file_open=open('hello.txt')
print type(file_open.readlines())
file_open.seek(0,0)
s= file_open.readlines()

sum=0
r=r'hello'
for k in s:
    sum=sum+len(re.findall(r,k))

file_open.close()
print 'the number of hello is ',sum






