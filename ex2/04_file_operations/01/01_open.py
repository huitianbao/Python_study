import linecache
fo =open('test.txt')

read_list=fo.read()
print read_list
print '*'*50
fo.seek(0,0)
# print linecache.getline('test.txt',2)
print linecache.getlines('test.txt')
for k in linecache.getlines('test.txt'):
    print k