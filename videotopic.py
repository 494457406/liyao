import cv2
import os
import easygui as g


msg = '请选择视频路径'
title = '视频路径选择'
path_1 = g.fileopenbox(msg, title, default='*', filetypes='.avi', multiple=False)
path_2=g.diropenbox(msg='请选择图片保存路径', title='图片保存路径选择', default='*')
vc = cv2.VideoCapture(path_1) #读入视频文件
c=0
rval=vc.isOpened()

#timeF = 1  #视频帧计数间隔频率
while rval:   #循环读取视频帧
    c = c + 1
    rval, frame = vc.read()

    if rval:
#img为当前目录下新建的文件夹


        # cv2.imwrite('E:/Recorder_2019-04-08_17-32-42/image/'+'ME630_408_Recorder_2019-04-08_17-32-42_'+str(c) + '.jpg', frame) #存储为图像
        cv2.imwrite(path_2+'/'+path_1[-42:-4]+'_'+str(c) + '.jpg', frame)

        cv2.waitKey(1)
    else:
        break

vc.release()


