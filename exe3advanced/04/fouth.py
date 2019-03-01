#coding:utf8
'''
4 定义一个方法get_funcname(func),func参数为任意一个函数对象，需要判断函数是否可以调用，如果可以调用则返回该函数名(
类型为str)，否则返回 “fun is not function"。

'''
def test_fun():
    print('hello')
    return 1
def get_funcname1(funcc):
    '''
    func参数为任意一个函数对象，需要判断函数是否可以调用，如果可以调用则返回该函数名(
    类型为str)，否则返回 “fun is not function"
    '''
    if callable(funcc)==True:
        return funcc
    else:
        return '%s is not function' % funcc



def get_funcname2(func):
    return type(func) is "<class 'function'>"

def get_funcname3(func):
    return type(isinstance(func,"<class 'function'>"))


if __name__=="__main__":
    print(1,get_funcname1('test_fun'))
    print('callable',callable(test_fun))
    # print('type of test_fun()',type(test_fun))
    print(2,get_funcname2(test_fun))
    print(3,get_funcname3(test_fun))