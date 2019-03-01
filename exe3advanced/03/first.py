#coding:utf8
'''
 定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。
其他类型则报错，并且返回一个偶数列表：（注：列表里面的元素为偶数）。
'''


def et_num(num):
    even_list=[]
    for k in num:
        if str(k).isdigit():
            if k%2==0:
                even_list.append(k)

        else:
            return 'Input Type Error'

    return even_list

if __name__=='__main__':
    list_1=[1,2,3,4,5,6,7,8]
    list_2=[1,2,'e']
    print et_num(list_1)
    print et_num(list_2)