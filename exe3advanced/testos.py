import os
def list_dir():
    path=os.getcwd()
    return os.listdir(path)


print(list_dir())
