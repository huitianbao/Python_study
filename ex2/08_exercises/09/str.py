
import re

a = "i,am,a,boy,in,china"
a1="i,am,a,{gender},in,{country}".format(gender="xxx",country="yyyy")
print a1

sp=a.split(",")
print sp
print sp[3],sp[-1]
def find_first():
 count=0
 for k in a:
    count+=1
    if k=='i':
        break
 return count



# def find



