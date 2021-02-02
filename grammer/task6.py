#1.使用os模块获取当前的工作目录
import os

print(os.getcwd())

# 2.创建文件hello.py，在该文件中编写函数test()，函数要求能够在控制台输出“hello”语句。创建文件
# main.py，在该文件中运行hello.py中的test()函数
#!/usr/bin/python       文件直接在Unix/Linux/Mac上运行
# -*- coding: UTF-8 -*-     .py文件本身使用标准UTF-8编码
 
import hello
 
hello.test()

#3. 用Python打开并展示你电脑中的任意一张图片（推荐使用Pillow库）
from PIL import Image

image = Image.open('paper.png')
# image.show()

#4. 小明想要在海报上展示一个网站，但是直接把网页链接放到海报上既不美观也不友好，所以请你帮
# 他生成一个包含网页链接的二维码吧（任意网页皆可）
import qrcode

qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('https://www.baidu.com/')

qr.make(fit=True)#fit参数为真或者没有给出version参数时，将会调用best_ fit方法来找到适合数据的最小尺寸。
img = qr.make_image()
img.show()

