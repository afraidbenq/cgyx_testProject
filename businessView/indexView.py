import logging, random
from businessView.loginView import LoginView, NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class IndexView(LoginView):
    index = (By.XPATH, "//android.widget.TextView[@text='首页']")
    search_goods = (By.XPATH, "//android.widget.TextView[@text='搜索商品']")
    search_input = (By.ID, "com.xiniao.cgmarket:id/et_search")
    searchBtn = (By.ID, "com.xiniao.cgmarket:id/tv_search")
    emptyimg = (By.ID, "com.xiniao.cgmarket:id/iv_empty")
    goods = (By.ID, "com.xiniao.cgmarket:id/cl_jp")
    goodsname = (By.ID, "com.xiniao.cgmarket:id/tv_title")
    addBtn = (By.ID, "com.xiniao.cgmarket:id/tv_add")
    addcartBtn = (By.ID, "com.xiniao.cgmarket:id/tv_add_car")
    selfbuyBtn = (By.ID, "com.xiniao.cgmarket:id/fl_buy")
    buynowBtn = (By.ID, "com.xiniao.cgmarket:id/tv_buy_now")
    numjian = (By.ID, "com.xiniao.cgmarket:id/iv_jian")
    numjia = (By.ID, "com.xiniao.cgmarket:id/iv_jia")
    submitorderBtn = (By.ID, "com.xiniao.cgmarket:id/tv_submit")
    spe = (By.ID, "com.xiniao.cgmarket:id/tv_spe")
    spename = (By.ID, "com.xiniao.cgmarket:id/tv_name")
    spetv = (By.ID, "com.xiniao.cgmarket:id/tv")
    tvstore = (By.ID, "com.xiniao.cgmarket:id/tv_store")
    paynowBtn = (By.ID, "com.xiniao.cgmarket:id/tv_pay")
    payclose = (By.XPATH, "//android.widget.ImageView[@resource-id='com.xiniao.cgmarket:id/iv_close']")
    ordername = (By.ID, "com.xiniao.cgmarket:id/tv_name")

    def enter_searchindex(self):
        """
        进入首页
        :return:
        """
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.index))
        self.driver.find_element(*self.index).click()

    def search_action(self, goodsname):
        """
        首页搜索商品步骤
        :param goodsname:商品名称
        :return:
        """
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.search_goods))
        self.driver.find_element(*self.search_goods).click()
        self.driver.find_element(*self.search_input).send_keys(goodsname)
        self.driver.find_element(*self.searchBtn).click()

    def check_search(self):
        """
        检测搜索结果
        :return:
        """
        try:
            element = self.driver.find_element(*self.emptyimg)
        except NoSuchElementException:
            element = self.driver.find_elements(*self.goods)
            logging.info('搜到%s件商品' % len(element))
            return True
        else:
            logging.warning('没搜到任何商品')
            return False

    def nine_nine_area(self):
        """
        9.9元优惠专区下单
        :return:
        """
        pass

    def spe_check(self):
        """
        是否有规格属性检测
        :return:
        """
        try:
            s = self.driver.find_element(*self.spe)
            # t = self.driver.find_element(*self.tvstore) #正式服去掉库存
            spenum = self.driver.find_elements(*self.spename)
            if len(spenum) == 0:
                return False
        except NoSuchElementException:
            return False
        else:
            return True

    def spe_sel(self):
        """
        规格自动选择
        :return:
        """
        spenum = self.driver.find_elements(*self.spename)
        tvnum = self.driver.find_elements(*self.spetv)
        if len(spenum) == 1:
            for i in range(len(tvnum)):
                self.driver.find_elements(*self.spetv)[i].click()
                # store = int(self.driver.find_element(*self.tvstore).text[5:]) #正式服去掉库存显示
                # if store > 0:
                #     break

        elif len(spenum) > 1:
            for i in range(len(tvnum)):
                self.driver.find_elements(*self.spetv)[i].click()
                # store = int(self.driver.find_element(*self.tvstore).text[5:]) #正式服去掉库存显示
                # if store > 0:
                #     break

    def goods_detail(self):
        """
        搜索后进入商品详情提交订单
        :return:
        """
        name = self.driver.find_element(*self.goodsname).text
        self.driver.find_elements(*self.goods)[0].click()
        self.driver.find_element(*self.addBtn).click()
        # 选择规格
        if self.spe_check():
            self.spe_sel()
            self.driver.find_element(*self.addcartBtn).click()
        else:
            logging.info('没有找到商品规格')
        self.driver.find_element(*self.selfbuyBtn).click()
        # 选择规格
        if self.spe_check():
            self.spe_sel()
        else:
            logging.info('没有找到商品规格')
        self.driver.find_element(*self.numjia).click()
        self.driver.find_element(*self.buynowBtn).click()
        self.driver.find_element(*self.submitorderBtn).click()
        return name

    def paystatus_check(self):
        """
        提交订单成功检测
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
        :param name:
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
    i = IndexView(driver)
    i.search_action('刀')
    if i.check_search():
        name = i.goods_detail()
        print(name)
        print(i.paystatus_check())
        print(i.orderstatus_check(name))
