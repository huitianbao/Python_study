import re

fo = open('hello.txt', 'r+')
fo_str = fo.read()
fo.seek(0, 0)
fo.write(fo_str.replace('hello', '111111'))