# 3 递归函数解释，用自己的话说明这个递归函数的工作流程。

def func1(i):
	if i<100:
		return i + func1(i+1)
	return i
print(func1(0))

'''
如果 i 小于 100， 不妨设  i  = 2
1、 f(2)  return 2 + f(3) 
                    f(3) return 3+f(4)
                      ........
                           f(99)   return 99 + f(100)
                                  f(100)  return 100 
  
  
  
  然后往前  推 把 f(100)=100带入 上一层
  依次算出
  
  最后算出  f(2)
  
  '''