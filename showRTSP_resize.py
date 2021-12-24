"""
Discription: open rtsp stream and display
"""

import cv2
import numpy as np

rtspAddr = "rtsp://administrator:asr123@10.1.166.253:8554/streaming/channel/101/unicast"


class rtspCap(object):

    """ 打开视频流 """

    def __init__(self):

        self.cap = cv2.VideoCapture(rtspAddr)
        #self.cap.set(cv2.CAP_PROP_FPS, 120)
        #self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
        #self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
        #self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

    """ 帧信息打印 """

    def calc_rgb_mean(img):
        b_mean = round(np.mean(img[:, :, 0]), 2)
        g_mean = round(np.mean(img[:, :, 1]), 2)
        r_mean = round(np.mean(img[:, :, 2]), 2)
        print('r_mean = ', r_mean, 'g_mean = ', g_mean, 'b_mean = ', b_mean)
        return r_mean, g_mean, b_mean

    def get_image_info(self, image):
        print(type(image))
        print(image.shape)
        print(image.size)
        print(image.dtype)
        pixel_data = np.array(image)
        # print(pixel_data)

    """ 逐帧显示 """

    def rtspImg(self):
        ret, frame = self.cap.read()
        self.get_image_info(frame)
        ori_width = frame.shape[1]
        ori_height = frame.shape[0]
        while ret:
            ret, frame = self.cap.read()
            cv2.namedWindow(rtspAddr, cv2.WINDOW_NORMAL |
                            cv2.WINDOW_KEEPRATIO)  # 等比例显示图像

            # 获取调整后的窗口大小
            (x, y, width_rect, height_rect) = cv2.getWindowImageRect(rtspAddr)

            if ori_width / ori_height >= width_rect / height_rect:
                width_display = width_rect
                height_display = int(ori_height * width_rect / ori_width)
            else:
                width_display = int(ori_width * height_rect / ori_height)
                height_display = height_rect

            resize_frame = cv2.resize(frame, (width_display, height_display))
            cv2.imshow(rtspAddr, resize_frame)
            cv2.resizeWindow(rtspAddr, width_display, height_display)

            if 0:
                roi = cv2.selectROI(frame, False, False)
                cropImg = frame[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]
                print('type cropimg:', type(cropImg))
                cv2.imshow('roi_img', cropImg)
                self.calc_rgb_mean(cropImg)

            key = cv2.waitKey(10) & 0xFF
            if key == ord('q') or key == 27:
                cv2.destroyAllWindows()
                break


if __name__ == '__main__':

    outmasages = rtspCap()

    outmasages.rtspImg()  # 调用摄像头

    outmasages.cap.release()  # 释放对象和销毁窗口
