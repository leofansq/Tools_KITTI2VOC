# TOOLS Dataset 2 VOC

## About VOC2007 ##
* JPEGImages：存放所有训练图片
* ImageSets：包含3个子文件夹Main，Layout，Segmentation，检测任务只关注Main文件夹，其中的txt文件用来标明训练所需的train和val训练集
* Annotation：存放xml文件，每个XML文件包含训练数据每张图片的各类信息

## Implementation ##

### Label数据处理 ###
* 检测类别归并与调整（对label的txt原文件修改）：在label所在文件夹的同级目录运行[LabelTrans.py](/LabelTrans.py)文件，文件中注意更改txt文件地址，需合并或忽略的类别
* txt转xml并创建Annotation文件夹：在label所在文件夹的同级目录运行[txt2xml.py](/txt2xml.py)文件，需修改训练图片源地址，另需注意代码中的bbox四个参数对应数组位置是否对应实际位置，根据实际情况修改

### ImageSets文件内容创建 ###
* 创建Imagesets文件夹，在文件夹中创建Main，Layout，Segmentation子文件夹。在Labels文件夹同级目录下执行[ImagesetsCreate.py](/ImagesetsCreate.py)，生成Main中的txt文件。

最后，将Annotations，JPEGImages，ImageSets文件夹放到规定目录下
