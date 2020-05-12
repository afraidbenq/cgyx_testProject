import unittest
from common.desired_caps import appium_desired
import logging
import os
import time


class StartEnd(unittest.TestCase):
    def save_img(self, img_name):  # 错误截图方法，这个必须先定义好
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"C:\cgyx_testProject\img"),
                                                              img_name))

    def GetScreen(self, action='结果截图', devices='CLB0218615004786'):
        """
        用例成功保存结果截图
        :param action: 用例结果注释
        :param devices: 手机UDID
        :return:
        """
        startTime = time.time()
        # 定义截图存放目录的路径
        screenpath = os.path.abspath(r"C:\cgyx_testProject\img")
        # 生成图片，此时图片还为空。action是字符串类型，存图片的说明信息
        png = screenpath + "\\" + time.strftime('%Y-%m-%d__%H-%M-%S',
                                                time.localtime(startTime)) + "_" + "_" + action + ".png"
        # 调用adb shell screencap方法截图，并存在手机的本地
        os.system("adb -s " + devices + " shell screencap -p /sdcard/screencap.png")
        fp = open(png, "a+", encoding="utf-8")
        fp.close()
        # 将手机上的图片，转存到截图目录里。
        os.system("adb -s " + devices + " pull /sdcard/screencap.png " + png)
        # 将图片发送到Html报告里，这里借用了BR生成报告的一个特性，它会将所有的print都带进报告里，这样使用预先写好的<img>标签，可以将png嵌入Html。
        print("<img src='" + png + "' width=600 />")
        return png

    def setUp(self):
        """
        预处理
        :return:
        """
        logging.info('=====setUp====')
        self.driver = appium_desired()

    def tearDown(self):
        """
        后处理
        :return:
        """
        logging.info('====tearDown====')
        self.driver.close_app()
