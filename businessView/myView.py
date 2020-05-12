import logging, random
from businessView.loginView import LoginView, NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#from interface.testAPI import Order
from time import sleep


class MyView(LoginView):
    my = (By.XPATH, '//*[@text="我的"]')
    allorder = (By.ID, 'com.xiniao.cgmarket:id/tv_order_all')
    dfkorder = (
        By.XPATH, "//android.widget.TextView[@resource-id='com.xiniao.cgmarket:id/tv_tab_title' and @text='待付款']")
    payBtn = (By.XPATH, "//android.widget.TextView[@resource-id='com.xiniao.cgmarket:id/tv_pay' and @text='付款']")
    cancelBtn = (
    By.XPATH, "//android.widget.TextView[@resource-id='com.xiniao.cgmarket:id/tv_cancel' and @text='取消订单']")
    qdcancel = (By.XPATH, "//android.widget.TextView[@resource-id='com.xiniao.cgmarket:id/tv_enter' and @text='确定']")
    paynowBtn = (By.ID, "com.xiniao.cgmarket:id/tv_pay")
    paytypesel = (By.ID, "com.xiniao.cgmarket:id/iv_cb_wx")
    mmlan = (By.ID, "com.tencent.mm:id/fw4")
    paycomple = (By.XPATH, "//android.widget.TextView[@text='完成' and @content-desc='完成']")
    backBtn = (By.XPATH, "//android.widget.Button[@text='返回商户 ']")

    def check_head_pic(self):
        pass

    def order_list(self):
        """
        检测待付款订单数量
        :return:
        """
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.my))
        self.driver.find_element(*self.my).click()
        self.driver.find_element(*self.allorder).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.dfkorder))
        self.driver.find_element(*self.dfkorder).click()
        try:
            elements = self.driver.find_elements(*self.payBtn)
            if len(elements) == 0:
                logging.info('没有待付款的订单')
                return False
        except NoSuchElementException:
            logging.warning('没有待付款的订单')
            return False

        else:
            return True

    def pay_action(self, orderlist):
        """
        微信真实支付
        :param orderlist:
        :return:
        """
        for i in range(len(orderlist)):
            try:
                self.driver.find_elements(*self.payBtn)[0].click()
            except IndexError:
                self.driver.find_elements(*self.cancelBtn)[0].click()
                self.driver.find_element(*self.qdcancel).click()
            else:
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.paynowBtn))
                self.driver.find_element(*self.paynowBtn).click()
                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.mmlan))
                self.driver.tap([(527, 1785)])
                self.driver.tap([(888, 1937)])
                self.driver.tap([(537, 2158)])
                self.driver.tap([(888, 2072)])
                self.driver.tap([(192, 1774)])
                self.driver.tap([(538, 2038)])
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.paycomple))
                self.driver.find_element(*self.paycomple).click()
                self.driver.find_element(*self.backBtn).click()


if __name__ == '__main__':
    token = '13823417742.1584512059.66270.c359415be2251f0b63e99015a2dfce51'  # 测试服
    # token= '13823417742.1584515620.93581.327f32e4c8d6a228ccba303b6d268aa1' #预发布
    # token = '13823417742.1584518448.82312.6886bd0e411f46c636a0c510f2fd699f'  # 灰度

    driver = appium_desired()
    m = MyView(driver)
    e = m.order_list()
    if e:
        r = Order.orderList(token, 1)
        orderlist = r['data']['data']
        print(len(orderlist))
        for i in range(len(orderlist)):
            print(orderlist[i]['order_sn'])
        m.pay_action(orderlist)
