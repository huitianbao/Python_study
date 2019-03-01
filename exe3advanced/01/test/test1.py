import glob
import os

def get_dir(file):
    # cwd=os.getcwd()
    path=os.path.abspath(file)
    list_glob=glob.glob(path)
    for k in list_glob:
        print(k)
    return 'end'





if __name__=='__main__':
   print(get_dir('ddddsssshhhh'))