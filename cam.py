
"""
# -*- coding: cp936 -*-
Author:zhangbo
Date:2019-11-07
Discription:Read Camaro picture and save
"""

import sys
import cv2
import os
import time
import datetime
import numpy as np


class CamaroCap(object):

    """ 打开视频流 """

    def __init__(self):

        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        # self.cap.set(cv2.CAP_PROP_FPS, 120) 这个有时候生效，有时候不生效不知道是什么原因
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
        self.cap.set(cv2.CAP_PROP_FOURCC,
                     cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

    """ 图片信息打印 """

    def get_image_info(self, image):
        print(type(image))
        print(image.shape)
        print(image.size)
        print(image.dtype)
        pixel_data = np.array(image)
        print(pixel_data)

    """ 逐帧读取数据并保存图片到本地制定位置 """

    def Camaro_image(self, savejpg):
        print("savejpg = ", savejpg)
        if savejpg == 1:
            file_path = "tmp"
            file_exist = os.path.exists(file_path)
            print("file_exist = ", file_exist)
            if file_exist == False:
                os.mkdir(file_path)
        i = 0
        while(True):
            ret, frame = self.cap.read()  # ret：True或者False，代表有没有读取到图片;frame：表示截取到一帧的图片
            if ret == False:
                break

            # self.get_image_info(frame)  # print("打印图片信息") 注意：调试的时候可以打开，如果是一直运行程序，建议把这行代码注释掉，避免影响内存占用

            cv2.namedWindow('cam0', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('cam0', frame)  # 展示图片

            if savejpg == True:
                mtime = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
                # print(mtime)
                cv2.imwrite(file_path + str("\\") + str(i) + str("-") +
                            mtime + ".jpg", frame)  # 保存图片
                i = i + 1

            if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == 27:
                cv2.destroyAllWindows()
                break


if __name__ == '__main__':
    savejpg = int(sys.argv[1])

    outmasages = CamaroCap()

    outmasages.Camaro_image(savejpg)  # 调用摄像头

    outmasages.cap.release()  # 释放对象和销毁窗口
