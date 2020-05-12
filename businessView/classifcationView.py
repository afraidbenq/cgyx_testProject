import logging, random
from businessView.indexView import IndexView, NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class ClassifcationView(IndexView):
    classifcationBtn = (By.XPATH, "//android.widget.TextView[@text='分类']")
    goodsclassifcation = (By.ID, "com.xiniao.cgmarket:id/tv")
    buyBtn = (By.ID, "com.xiniao.cgmarket:id/iv_gou")

    def classifcation_check(self):
        """
        分类页面商品检测
        :return:
        """
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.classifcationBtn))
        self.driver.find_element(*self.classifcationBtn).click()
        goodsclass = self.driver.find_elements(*self.goodsclassifcation)
        goods = self.driver.find_elements(*self.buyBtn)
        if len(goodsclass) == 0 or len(goods) == 0:
            return False
        else:
            return True

    def classifcation_detail(self):
        """
        进入分类商品详情提交订单
        :return:
        """
        name = self.driver.find_element(*self.goodsname).text
        self.driver.find_elements(*self.buyBtn)[0].click()
        self.driver.find_element(*self.addBtn).click()
        # 选择规格
        if self.spe_check():
            self.spe_sel()
            self.driver.find_element(*self.addcartBtn).click()
        self.driver.find_element(*self.selfbuyBtn).click()
        # 选择规格
        if self.spe_check():
            self.spe_sel()
        self.driver.find_element(*self.numjia).click()
        self.driver.find_element(*self.buynowBtn).click()
        self.driver.find_element(*self.submitorderBtn).click()
        return name


if __name__ == '__main__':
    driver = appium_desired()
    c = ClassifcationView(driver)
    if c.classifcation_check():
        name = c.classifcation_detail()
        print(name)
        print(c.paystatus_check())
        print(c.orderstatus_check(name))
