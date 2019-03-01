# /user/bin/python
# coding:utf8

import re
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


# print getHtml("http://tieba.baidu.com/f?kw=周杰伦")

def getImage(html):
    imageRe = r = r'img src="(http.+\.jpg)'
    imageRe_compile = re.compile(imageRe)
    imageList = re.findall(imageRe_compile, html)

    return imageList


myhtml = getHtml("http://tieba.baidu.com/f?kw=周杰伦")
myImageURL_List = getImage(myhtml)
x = 1
for k in myImageURL_List:
    urllib.urlretrieve(k, 'F:\pyimage\%s.jpg' % x)
    # urllib.urlretrieve(k, '%s.jpg' % x)

    x = x + 1
