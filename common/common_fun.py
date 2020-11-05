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

    def test(self):
        print(self.driver)
        # print(self.driver.activate_app)
        # print(self.driver.activate_ime_engine())
        # print(self.driver.active_ime_engine)
        # print(self.driver.add_cookie)
        # print(self.driver.all_sessions)
        # print(self.driver.app_strings)
        # print(self.driver.application_cache)
        # print(dir(self.driver))
        # print(dir(self))
        # self.find_element()
        # self.get_window_size()
        # self.driver.get_window_size()
        # self.get_window_size()
        # self.get()
        # self.driver.get_clipboard()
        # self.driver.find_element()
        app=['activate_app',
             'activate_ime_engine',
             'active_ime_engine',
             'add_cookie',
             'all_sessions',
             'app_strings',
             'application_cache',
             'available_ime_engines',
             'back',
             'background_app',
             'battery_info',
             'capabilities',
             'close',
             'close_app',
             'command_executor',
             'context',
             'contexts',
             'create_web_element',
             'current_activity',
             'current_context',
             'current_package',
             'current_url',
             'current_window_handle',
             'deactivate_ime_engine',
             'delete_all_cookies',
             'delete_cookie', 'desired_capabilities',
             'device_time', 'drag_and_drop',
             'end_test_coverage', 'error_handler',
             'events', 'execute',
             'execute_async_script', 'execute_driver',
             'execute_script', 'file_detector',
             'file_detector_context',
             'find_element',
             'find_element_by_accessibility_id',
             'find_element_by_android_data_matcher',
             'find_element_by_android_uiautomator',
             'find_element_by_android_view_matcher',
             'find_element_by_android_viewtag',
             'find_element_by_class_name',
             'find_element_by_css_selector',
             'find_element_by_custom',
             'find_element_by_id',
             'find_element_by_image',
             'find_element_by_ios_class_chain',
             'find_element_by_ios_predicate',
             'find_element_by_ios_uiautomation',
             'find_element_by_link_text',
             'find_element_by_name',
             'find_element_by_partial_link_text',
             'find_element_by_tag_name',
             'find_element_by_windows_uiautomation',
             'find_element_by_xpath',
             'find_elements',
             'find_elements_by_accessibility_id',
             'find_elements_by_android_data_matcher',
             'find_elements_by_android_uiautomator',
             'find_elements_by_android_viewtag',
             'find_elements_by_class_name',
             'find_elements_by_css_selector',
             'find_elements_by_custom',
             'find_elements_by_id',
             'find_elements_by_image',
             'find_elements_by_ios_class_chain',
             'find_elements_by_ios_predicate',
             'find_elements_by_ios_uiautomation',
             'find_elements_by_link_text',
             'find_elements_by_name',
             'find_elements_by_partial_link_text',
             'find_elements_by_tag_name',
             'find_elements_by_windows_uiautomation',
             'find_elements_by_xpath',
             'find_image_occurrence',
             'finger_print', 'flick',
             'forward', 'fullscreen_window',
             'get', 'get_clipboard',
             'get_clipboard_text', 'get_cookie',
             'get_cookies', 'get_device_time',
             'get_display_density', 'get_events',
             'get_images_similarity', 'get_log',
             'get_performance_data', 'get_performance_data_types',
             'get_screenshot_as_base64', 'get_screenshot_as_file',
             'get_screenshot_as_png', 'get_settings',
             'get_system_bars', 'get_window_position',
             'get_window_rect', 'get_window_size',
             'hide_keyboard', 'implicitly_wait',
             'install_app', 'is_app_installed',
             'is_ime_active', 'is_keyboard_shown',
             'is_locked', 'keyevent', 'launch_app',
             'location', 'lock', 'log_event', 'log_types',
             'long_press_keycode', 'make_gsm_call',
             'match_images_features', 'maximize_window',
             'minimize_window', 'mobile', 'name',
             'network_connection', 'open_notifications',
             'orientation', 'page_source', 'press_button',
             'press_keycode', 'pull_file', 'pull_folder',
             'push_file', 'query_app_state', 'quit',
             'refresh', 'remove_app', 'reset',
             'save_screenshot', 'scroll', 'send_sms',
             'session', 'session_id', 'set_clipboard',
             'set_clipboard_text', 'set_gsm_signal',
             'set_gsm_voice', 'set_location', 'set_network_connection',
             'set_network_speed', 'set_page_load_timeout',
             'set_power_ac', 'set_power_capacity', 'set_script_timeout',
             'set_value', 'set_window_position', 'set_window_rect',
             'set_window_size', 'shake', 'start_activity', 'start_client',
             'start_recording_screen', 'start_session', 'stop_client',
             'stop_recording_screen', 'swipe', 'switch_to', 'switch_to_active_element',
             'switch_to_alert', 'switch_to_default_content', 'switch_to_frame', 'switch_to_window',
             'tap', 'terminate_app', 'title', 'toggle_location_services', 'toggle_touch_id_enrollment', 'toggle_wifi',
             'touch_id', 'unlock', 'update_settings', 'w3c', 'wait_activity', 'window_handles']


if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    com.test()
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
