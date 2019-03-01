#/user/bin/python
#coding:utf8

import re
s="""
hhsdj dskj hello src=cvst yes jjjjjfs
jcsihdc src=123 yes nknk
hello src=python yes kska
"""
r1='hello src=.+ yes'
print re.findall(r1,s,re.M)
r2='hello src=(.+) yes'
print re.findall(r2,s,re.M)