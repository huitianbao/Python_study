#coding:utf8
# 2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）。

import urllib

from pip._vendor.urllib3.util import request


def get_page(url_input='https://www.cnblogs.com/wang-can/p/3591116.html'):
    'python2 获取网页内容的方法'
    uo=urllib.urlopen(url_input)

    html_content=uo.read()

    return html_content


def get_page3(utl_input='https://www.cnblogs.com/wang-can/p/3591116.html'):
    'python 3 获取网页内容的方法'     #  失败的尝试
    response=request.urlopen(utl_input)
    return response.read()



if __name__=="__main__":
    URL = 'https://daohang.qq.com/?fr=hmpage'
    # print get_page(URL)
    get_page3()



