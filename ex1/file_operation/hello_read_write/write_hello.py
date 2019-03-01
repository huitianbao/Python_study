import re

fo = open('hello.txt', 'r+')
fo2=open('a2.txt','w')

fo_str = fo.read()
fo.seek(0, 0)
fo.write(fo_str.replace('hello', '111111'))
fo.seek(0,0)
fo2.write(fo.read())
fo.close()
fo2.close()

