import re

s='img src="vbsdcjsbvks.jpg"'
ss='img src="http://imgsrc.baidu.com/forum/wh%3D60%2C60%3B/sign=a169e1bdea1190ef01ae9ad9fe37ab26/279759ee3d6d55fb96a7477660224f4a20a4dd78.jpg"'
r=r'img src=(.+\.jpg)'

print 'this  is ',re.findall(r,ss)
