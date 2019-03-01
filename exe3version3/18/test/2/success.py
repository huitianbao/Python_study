
# 2.在python命令行里，输入import this 以后出现的文档，统计该文档中，"be" "is" "than" 的出现次数。

import re
file = open('this.txt','r')    # 赋予读写权限
list_read=file.read()

content = re.split('[,. \n]',list_read)
print(content)

def count_words(word,content_input):
    count=0
    for c in content_input:
        if c ==word:
            count+=1
    print('%s 个数是 %d'% (word,count))

count_words('be',content)
count_words('is',content)
count_words('than',content)



