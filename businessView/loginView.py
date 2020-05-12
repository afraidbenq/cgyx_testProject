import logging
from common.common_fun import Common, NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from DataBase.mysqldb import MysqlDb
from time import sleep


class LoginView(Common):
    indicator = (By.ID, "com.xiniao.cgmarket:id/vp_indicator")
    go_app = (By.ID, "com.xiniao.cgmarket:id/tv_go_app")
    my = (By.XPATH, '//*[@text="我的"]')
    mmloginBtn = (By.ID, "com.xiniao.cgmarket:id/tv_account")
    wxloginBtn = (By.ID, "com.xiniao.cgmarket:id/tv_wx")
    quickloginBtn = (By.ID, "com.xiniao.cgmarket:id/tv_code")
    regBtn = (By.ID, "com.xiniao.cgmarket:id/tv_register")

    phone_input = (By.ID, "com.xiniao.cgmarket:id/et_phone")
    passwd_input = (By.ID, "com.xiniao.cgmarket:id/et_password")
    code_input = (By.ID, "com.xiniao.cgmarket:id/et_code")
    loginBtn = (By.ID, "com.xiniao.cgmarket:id/tv_login")

    wx = (By.ID, "com.huawei.android.internal.app:id/icon")

    getcode = (By.ID, "com.xiniao.cgmarket:id/tv_count_down")

    setBtn = (By.ID, "com.xiniao.cgmarket:id/tv_settings")
    logoutBtn = (By.ID, "com.xiniao.cgmarket:id/tv_log_out")
    logoutqr =(By.ID,"android:id/button1")

    def enterindex(self):
        """
        进入欢迎页面
        :return:
        """
        try:
            i = self.driver.find_element(*self.indicator)
        except NoSuchElementException:
            pass
        else:
            self.swipeLeft()
            self.swipeLeft()
            self.driver.find_element(*self.go_app).click()

    def check_logined(self):
        """
        检查登录状态
        :return:
        """
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.my))
        self.driver.find_element(*self.my).click()
        try:
            element = self.driver.find_element(*self.mmloginBtn)
        except NoSuchElementException:
            logging.info('===========logined in========== !')
            return True
        else:
            return False

    def mmlogin_action(self, phone, passwd):
        """
        密码登录步骤
        :param phone: 手机号码
        :param passwd: 密码
        :return:
        """
        logging.info('mmlogin !')
        self.driver.find_element(*self.mmloginBtn).click()
        self.driver.find_element(*self.phone_input).send_keys(phone)
        self.driver.find_element(*self.passwd_input).send_keys(passwd)
        self.driver.find_element(*self.loginBtn).click()

    def wxlogin_action(self):
        """
        微信登录步骤
        :return:
        """
        self.driver.find_element(*self.wxloginBtn).click()
        self.driver.find_element(*self.wx).click()
        pass

    def reg_action(self):
        """
        注册步骤
        :return:
        """
        self.driver.find_element(*self.regBtn).click()
        pass

    def quicklogin_action(self, phone):
        """
        快捷登录步骤
        :param phone:
        :return:
        """
        logging.info('quicklogin !')
        self.driver.find_element(*self.quickloginBtn).click()
        self.driver.find_element(*self.phone_input).send_keys(phone)
        self.driver.find_element(*self.getcode).click()
        sleep(2)
        with MysqlDb() as db:
            sql = "SELECT code FROM `chungou6`.`cg_sms_log` WHERE `mobile` = '%s' ORDER BY `id` DESC LIMIT 0,1" % \
                  phone
            rt = db.query(sql)
            code = rt[0]['code']
        self.driver.find_element(*self.code_input).send_keys(code)
        self.driver.find_element(*self.loginBtn).click()

    def logout_action(self):
        """
        退出登录步骤
        :return:
        """
        self.driver.find_element(*self.my).click()
        self.driver.find_element(*self.setBtn).click()
        self.driver.find_element(*self.logoutBtn).click()
        self.driver.find_element(*self.logoutqr).click()


if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.enterindex()
    e = l.check_logined()
    if not e:
        # l.mmlogin_action(13823417742, 123456)
        l.quicklogin_action(13823417742)
        print(l.check_logined())
        l.logout_action()
