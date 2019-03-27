'''
本程序用来将VOC数据集的标签与图像分类，将同类别的标签和图像放到同一个文件夹中
使用方法：将该文件放到与VOCdevkit同级的文件夹下，然后直接终端执行即可
'''
#coding:utf-8
import os
import shutil
import xml.dom.minidom
i = '000001'
j = 1   #从第二个<name>，即第一个物体的<name>开始读取
a = int(i)

while a < 9963:
    dom = xml.dom.minidom.parse('VOCdevkit\VOC2007\Annotations\%s.xml'%i)  #打开xml文档
    root = dom.documentElement  #得到文档元素对象
    ob = root.getElementsByTagName('name')    #获取需要的标签
    while j < len(ob):
        dir_name = ob[j].firstChild.data
        if os.path.exists('D:\yolo\classification\%s'%(dir_name)):  #判断该类别的文件夹是否存在
            shutil.copy('VOCdevkit\VOC2007\Annotations\%s.xml'%(i),'D:\yolo\classification\%s'%(dir_name))
            shutil.copy('VOCdevkit\VOC2007\JPEGImages\%s.jpg'%(i), 'D:\yolo\classification\%s'%(dir_name))
        else:
            os.mkdir('D:\yolo\classification\%s'%(dir_name))    #若不存在，创建该文件夹
            shutil.copy('VOCdevkit\VOC2007\Annotations\%s.xml'%(i), 'D:\yolo\classification\%s'%(dir_name))
            shutil.copy('VOCdevkit\VOC2007\JPEGImages\%s.jpg'%(i), 'D:\yolo\classification\%s'%(dir_name))
        j = j+1
    a = a+1
    i = '{:0>6}'.format(a)
    j = 1