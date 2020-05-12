from baseView.baseView import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
from PIL import Image  # pip install Pillow  PIL 的py3版本
import time, os
import csv


class Common(BaseView):
    # 实名认证按钮
    btn_verify_dialog = (By.ID, 'com.xiniao.cgmarket:id/btn_verify_dialog')
    # 关闭实名认证
    iv_close = (By.ID, 'com.xiniao.cgmarket:id/iv_close')

    allowlocaBtn = (By.ID, 'com.huawei.systemmanager:id/btn_allow')
    allowAddressBtn = (By.ID, 'com.huawei.systemmanager:id/btn_allow')

    # 红米note4x
    nextBtn = (By.ID, 'com.goockr.intelligentizeobc:id/goto_settings')
    allowBtn = (By.ID, 'android:id/button1')

    def check_verify_btn(self):
        logging.info('======= check verify btn =======')
        try:
            btn_verify_dialog = self.driver.find_element(*self.btn_verify_dialog)
            iv_close = self.driver.find_element(*self.iv_close)
        except NoSuchElementException:
            logging.info('no verify btn')
        else:
            iv_close.click()

    def check_allowLocaBtn(self):
        logging.info('=========check allowLocaBtn==========')

        try:
            allowlocaBtn = self.driver.find_element(*self.allowBtn)
        except NoSuchElementException:
            logging.info('no allowLoca')
        else:
            allowlocaBtn.click()

    def check_allowAddressBtn(self):
        logging.info('========check allowAddressBtn========')

        try:
            allowAddressBtn = self.driver.find_element(*self.allowBtn)
        except NoSuchElementException:
            logging.info('no allowAddress')
        else:
            allowAddressBtn.click()

    def check_nextBtn(self):
        logging.info('=======check nextBtn=========')

        try:
            nextBtn = self.driver.find_element(*self.nextBtn)
        except NoSuchElementException:
            logging.info('no next')
        else:
            nextBtn.click()

    def check_allowStoreBtn(self):
        logging.info('=========check allowStore=========')

        try:
            allowStoreBtn = self.driver.find_element(*self.allowBtn)
        except NoSuchElementException:
            logging.info('no allowStore')
        else:
            allowStoreBtn.click()

    def check_allowCameraBtn(self):
        logging.info('=========check allowCamera=========')

        try:
            allowCameraBtn = self.driver.find_element(*self.allowBtn)
        except NoSuchElementException:
            logging.info('no allowCamera')
        else:
            allowCameraBtn.click()

    def check_allowPhoneBtn(self):
        logging.info('==========check allowPhone==========')

        try:
            allowPhoneBtn = self.driver.find_element(*self.allowBtn)
        except NoSuchElementException:
            logging.info('no allowPhone')
        else:
            allowPhoneBtn.click()

    def check_allowAddressBtn2(self):
        logging.info('=========check allowAddressBtn2=========')

        try:
            allowAddressBtn2 = self.driver.find_element(*self.allowBtn)
        except NoSuchElementException:
            logging.info('no allowAddress2')
        else:
            allowAddressBtn2.click()

    def check_cancelBtn(self):
        logging.info('==========check_cancelBtn=========')
        try:
            cancelBtn = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('no cancelBtn')
        else:
            cancelBtn.click()

    def check_skipBtn(self):
        logging.info('=========check skipBtn=============')

        try:
            skipBtn = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('no skipBtn')
        else:
            skipBtn.click()

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x1, y1, x2, y1, 1000)

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/img/%s_%s.png' % (module, time)

        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)
        return image_file

    def get_screenshot_by_custom_size(self, module, bounds):
        # 自定义截取范围
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/img/%s_%s.png' % (module, time)
        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)
        image = Image.open(image_file)
        newImage = image.crop(bounds)
        newImage.save(image_file)
        return self

    def get_csv_data(self, csv_file, line):
        logging.info('=====get_csv_data======')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row


if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
# com.check_allowLocaBtn()
# com.check_allowAddressBtn()
#  com.check_nextBtn()
#  com.check_allowStoreBtn()
#  com.check_allowPhoneBtn()
#  com.check_allowAddressBtn2()
#  com.check_cancelBtn()
#  com.check_skipBtn()
#  com.swipeLeft()
#  com.getScreenShot('startApp')
