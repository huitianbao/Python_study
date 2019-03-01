# 4.已知  a =  [1,2,3,6,8,9,10,14,17],请将该list转换为字符串，例如 '123689101417'.
a =  [1,2,3,6,8,9,10,14,17]

str_a=[]
for k in a:
    str_a.append(str(k))
print(str_a)

def list_to_string(x):
    sum=''
    for kk in x:
        sum=sum+kk
    return sum
print(list_to_string(str_a))