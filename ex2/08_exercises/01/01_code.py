#coding:utf8
"""一已经字符串 s = "i,am,lilei",请用两种办法取出之间的“am”字符。"""
import re
s="i,am,lilei"
print s[2:4]
print s.split(",").pop(1)

sub_list=s.split(",")
print sub_list[1]

r=r'am'
print re.findall(r,s)
