import json
import os
import shutil

text_json = open('F:\coco\\annotations_trainval2014\instances_train2014.json') #打开标签文件
text_load = json.load(text_json) #读取标签文件

a = text_load['annotations'] #a是列表，将json文件中"annotations"所对应的值（一个列表）赋值给a
b = text_load['categories'] #b是列表
c = text_load['images'] #c是列表
i = 0
j = 0
k = 0
c_name = 'a' #定义类别名称字符串
f_name = 'b' #定义图像名称字符串
while i<len(a): #循环注释列表
    while j<len(b): #循环类别列表
        if b[j]['id']==a[i]['category_id']: #a[i]，b[j]均为字典
            c_name = b[j]['name'] #若当前注释中的类别id与当前类别的子类别id相同，则将该类别名称赋值给c_name
            break
        else:
            j = j+1
    while k<len(c): #循环图像列表
        if c[k]['id']==a[i]['image_id']:
            f_name = c[k]['file_name'] #若当前注释中的图像id与当前图像中的id相同，则将该图像名称赋值给f_name
            break
        else:
            k = k+1
    if os.path.exists('F:\classification\%s'%(c_name)):  # 判断该类别的文件夹是否存在
        shutil.copy('coco\\train2014\%s'%(f_name),'F:\classification\%s'%(c_name))
    else:
        os.mkdir('F:\classification\%s'%(c_name))  # 若不存在，创建该文件夹
        shutil.copy('coco\\train2014\%s'%(f_name),'F:\classification\%s'%(c_name))
    i = i+1
    j = 0
    k = 0