import logging, random
from businessView.indexView import IndexView, NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class CartView(IndexView):
    cart = (By.XPATH, "//android.widget.TextView[@text='购物车']")
    cartgoods = (By.ID, "com.xiniao.cgmarket:id/iv_cb")
    goodsname = (By.ID, "com.xiniao.cgmarket:id/tv_name")
    empty = (By.ID, "com.xiniao.cgmarket:id/iv_cart_empty")
    enter = (By.ID, "com.xiniao.cgmarket:id/tv_enter")
    selall = (By.ID, "com.xiniao.cgmarket:id/cb_all")

    def cart_check(self):
        """
        检查购物车状态
        :return:
        """
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.cart))
        self.driver.find_element(*self.cart).click()
        try:
            e = self.driver.find_element(*self.empty)
        except NoSuchElementException:
            goods = self.driver.find_elements(*self.cartgoods)
            logging.info('购物车有%s件商品' % len(goods))
            return True
        else:
            logging.info('购物车为空！')
            return False

    def cart_settlement(self):
        """
        购物车结算订单提交
        :return:
        """
        name = self.driver.find_element(*self.goodsname).text
        self.driver.find_elements(*self.cartgoods)[0].click()
        self.driver.find_element(*self.enter).click()
        self.driver.find_element(*self.submitorderBtn).click()
        return name


if __name__ == '__main__':
    driver = appium_desired()
    c = CartView(driver)
    if c.cart_check():
        name = c.cart_settlement()
        print(name)
        print(c.paystatus_check())
        print(c.orderstatus_check(name))
