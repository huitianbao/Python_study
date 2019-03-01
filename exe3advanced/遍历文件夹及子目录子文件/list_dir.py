import os

def list_dir(path):

    list_1=[]
    if os.path.isdir(path):
        list_1=os.listdir(path)

        for k in list_1:
            print(path+'\\'+k)
            if os.path.isdir(path+'\\'+k):
                list_dir(path+'\\'+k)








# list_dir('E:/pythoncodenew/exe3advanced')
list_dir('E:\pythoncodenew\exe3advanced\\01')