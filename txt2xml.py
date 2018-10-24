#!/usr/bin/env python  
# -*- coding: UTF-8 -*-  
# txt_to_xml.py  
# 根据一个给定的XML Schema，使用DOM树的形式从空白文件生成一个XML  
from xml.dom.minidom import Document  
import cv2  
import os  
  
def generate_xml(name,split_lines,img_size,class_ind):  
    doc = Document()  # 创建DOM文档对象  
  
    annotation = doc.createElement('annotation')  
    doc.appendChild(annotation)  
  
    title = doc.createElement('folder')  
    title_text = doc.createTextNode('VOC2007')#这里修改了文件夹名  
    title.appendChild(title_text)  
    annotation.appendChild(title)  
  
    img_name=name+'.png'#要用png格式  
  
    title = doc.createElement('filename')  
    title_text = doc.createTextNode(img_name)  
    title.appendChild(title_text)  
    annotation.appendChild(title)  
  
    source = doc.createElement('source')  
    annotation.appendChild(source)  
  
    title = doc.createElement('database')  
    title_text = doc.createTextNode('The VOC2007 Database')#修改为VOC  
    title.appendChild(title_text)  
    source.appendChild(title)  
  
    title = doc.createElement('annotation')  
    title_text = doc.createTextNode('PASCAL VOC2007')#修改为VOC  
    title.appendChild(title_text)  
    source.appendChild(title)  
  
    size = doc.createElement('size')  
    annotation.appendChild(size)  
  
    title = doc.createElement('width')  
    title_text = doc.createTextNode(str(img_size[1]))  
    title.appendChild(title_text)  
    size.appendChild(title)  
  
    title = doc.createElement('height')  
    title_text = doc.createTextNode(str(img_size[0]))  
    title.appendChild(title_text)  
    size.appendChild(title)  
  
    title = doc.createElement('depth')  
    title_text = doc.createTextNode(str(img_size[2]))  
    title.appendChild(title_text)  
    size.appendChild(title)  
  
    for split_line in split_lines:  
        line=split_line.strip().split()  
        #if line[0] in class_ind:  
        object = doc.createElement('object')  
        annotation.appendChild(object)  
  
        title = doc.createElement('name')  
        title_text = doc.createTextNode(line[0])  
        title.appendChild(title_text)  
        object.appendChild(title)  
          
        title = doc.createElement('difficult')  
        title_text = doc.createTextNode('0')  
        title.appendChild(title_text)  
        object.appendChild(title)  
  
        bndbox = doc.createElement('bndbox')  
        object.appendChild(bndbox)  
        title = doc.createElement('xmin')  
        title_text = doc.createTextNode(str(int(float(line[1]))))  
        title.appendChild(title_text)  
        bndbox.appendChild(title)  
        title = doc.createElement('ymin')  
        title_text = doc.createTextNode(str(int(float(line[2]))))  
        title.appendChild(title_text)  
        bndbox.appendChild(title)  
        title = doc.createElement('xmax')  
        title_text = doc.createTextNode(str(int(float(line[3]))))  
        title.appendChild(title_text)  
        bndbox.appendChild(title)  
        title = doc.createElement('ymax')  
        title_text = doc.createTextNode(str(int(float(line[4]))))  
        title.appendChild(title_text)  
        bndbox.appendChild(title)  
  
    # 将DOM对象doc写入文件  
    f = open('Annotations/'+name+'.xml','w')  
    f.write(doc.toprettyxml(indent = ''))  
    f.close()  
  
if __name__ == '__main__':  
    class_ind=('pedestrian', 'car')#修改为了两类  
    cur_dir=os.getcwd()  
    labels_dir=os.path.join(cur_dir,'Labels')  
    for parent, dirnames, filenames in os.walk(labels_dir): # 分别得到根目录，子目录和根目录下文件     
        for file_name in filenames:  
            full_path=os.path.join(parent, file_name) # 获取文件全路径  
            #print full_path  
            f=open(full_path)  
            split_lines = f.readlines()  
            name= file_name[:-4] # 后四位是扩展名.txt，只取前面的文件名  
            #print name  
            img_name=name+'.jpg'   
            img_path=os.path.join('E:\FishEye_out\image_2',img_name) # 路径需要自行修改              
            #print img_path  
            img_size=cv2.imread(img_path).shape  
            generate_xml(name,split_lines,img_size,class_ind)  
print('all txts has converted into xmls')  
