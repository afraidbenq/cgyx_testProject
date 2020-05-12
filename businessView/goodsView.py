import logging, random
from businessView.loginView import LoginView, NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class GoodsView(LoginView):
    goodBtn = (By.ID, "com.xiniao.cgmarket:id/tv_upgrade_rights")
    content = (By.ID, "com.xiniao.cgmarket:id/cl_content")
    tv_title = (By.ID, "com.xiniao.cgmarket:id/tv_title")
    bot = (By.ID, "com.xiniao.cgmarket:id/tv_bot")
    submitorderBtn = (By.ID, "com.xiniao.cgmarket:id/tv_submit")
    paynowBtn = (By.ID, "com.xiniao.cgmarket:id/tv_pay")
    payclose = (By.XPATH, "//android.widget.ImageView[@resource-id='com.xiniao.cgmarket:id/iv_close']")
    ordername = (By.ID, "com.xiniao.cgmarket:id/tv_name")

    def goods_check(self):
        """
        严选专区商品检测
        :return:
        """
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.goodBtn))
        self.driver.find_element(*self.goodBtn).click()
        c = self.driver.find_elements(*self.content)
        if len(c) == 0:
            return False
        else:
            return True

    def content_detail(self):
        """
        严选商品详情提交订单
        :return: 商品名称
        """
        name = self.driver.find_element(*self.tv_title).text
        self.driver.find_elements(*self.content)[0].click()
        self.driver.find_element(*self.bot).click()
        self.driver.find_element(*self.submitorderBtn).click()
        return name

    def paystatus_check(self):
        """
        订单提交成功检测
        :return:
        """
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.paynowBtn))
            p = self.driver.find_element(*self.paynowBtn)
        except NoSuchElementException:
            return False
        else:
            return True

    def orderstatus_check(self, name):
        """
        订单变为待付款状态检测
        :param name: 商品名称
        :return:
        """
        try:
            self.driver.find_element(*self.payclose).click()
            o = self.driver.find_element(*self.ordername)
            ordername = self.driver.find_elements(*self.ordername)[0].text
            if ordername == name:
                pass
            else:
                return False

        except NoSuchElementException:
            return False
        else:
            return True


if __name__ == '__main__':
    driver = appium_desired()
    g = GoodsView(driver)
    if g.goods_check():
        name = g.content_detail()
        print(name)
        print(g.paystatus_check())
        print(g.orderstatus_check(name))
