#coding:utf8
from __future__ import division
import re

# r=r"htb$"
#
# print re.findall(r,'jjjjjjjjjjjjjjjjjht  b')

# s='ddd^abcggggggggggggggg^abckkkkkkkkkkkk^abck'
# r=r'\^abc'
# print re.findall(r,s)


#ss=199+200-488*999/3
ss="aaa+bbb-ccc*ddd/fff"
print 'ss is ',str(ss)
print re.split(r'[\+\-\*/]',str(ss))
print '#'*40
print 'this is match', re.match(r'\w*[\+\-\*/]\w*[\+\-\*/]\w*[\+\-\*/]\w*[\+\-\*/]\w*',ss).group()
print 'this is search',re.search(r'(\w*[\+\-\*/](\w*)?)*',ss).group()