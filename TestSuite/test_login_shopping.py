from common.myunit import StartEnd
from businessView.loginView import LoginView
from businessView.cartView import CartView
from businessView.classifcationView import ClassifcationView
from businessView.goodsView import GoodsView
from businessView.indexView import IndexView
from businessView.myView import MyView
import unittest
import logging
import ddt
from BeautifulReport import BeautifulReport


@ddt.ddt
class TestLoginShpping(StartEnd):
    phone = [13823417742]

    @unittest.skip('test_quicklogin_classifcashopping')
    @BeautifulReport.add_test_img('test_quicklogin_classifcashopping')
    @ddt.data(*phone)
    def test_quicklogin_classifcashopping(self, phone):
        """
        测试快捷登录分类页面下单用例
        :param phone: 手机号码
        :return:
        """
        logging.info('开始测试快捷登录分类页面下单')
        l = LoginView(self.driver)
        c = ClassifcationView(self.driver)
        l.enterindex()
        e = l.check_logined()
        if not e:
            l.quicklogin_action(phone)
        r = l.check_logined()
        self.assertTrue(r)
        if c.classifcation_check():
            name = c.classifcation_detail()
            logging.info('goodname:%s' % name)
        self.assertTrue(c.paystatus_check())
        self.assertTrue(c.orderstatus_check(name))
        # 不报错截图保存结果
        self.GetScreen('分类页面下单结果')

    # @unittest.skip('test_mmlogin_goodsshopping')
    @BeautifulReport.add_test_img('test_mmlogin_goodsshopping')
    @ddt.data((13823417742, 'a12345678'))
    @ddt.unpack
    def test_mmlogin_goodsshopping(self, phone, passwd):
        """
        测试密码登录严选专区页面下单用例
        :param phone: 手机号码
        :param passwd: 密码
        :return:
        """
        logging.info('开始测试密码登录严选专区页面下单')
        l = LoginView(self.driver)
        g = GoodsView(self.driver)
        l.enterindex()
        e = l.check_logined()
        if not e:
            l.mmlogin_action(phone, passwd)
        r = l.check_logined()
        self.assertTrue(r)
        r = g.goods_check()
        self.assertTrue(r)
        if r:
            name = g.content_detail()
            logging.info('goodname:%s' % name)
        self.assertTrue(g.paystatus_check())
        self.assertTrue(g.orderstatus_check(name))
        # 不报错截图保存结果
        self.GetScreen('严选专区下单结果')

    # @unittest.skip('test_mmlogin_cartshopping')
    @BeautifulReport.add_test_img('test_mmlogin_cartshopping')
    @ddt.data((13823417742, 'a12345678'))
    @ddt.unpack
    def test_mmlogin_cartshopping(self, phone, passwd):
        """
        测试密码登录购物车页面结算下单用例
        :param phone: 手机号码
        :param passwd: 密码
        :return:
        """
        logging.info('开始测试密码登录购物车页面结算下单')
        l = LoginView(self.driver)
        c = CartView(self.driver)
        l.enterindex()
        e = l.check_logined()
        if not e:
            l.mmlogin_action(phone, passwd)
        r = l.check_logined()
        self.assertTrue(r)
        if c.cart_check():
            name = c.cart_settlement()
            logging.info('goodname:%s' % name)
        self.assertTrue(c.paystatus_check())
        self.assertTrue(c.orderstatus_check(name))
        # 不报错截图保存结果
        self.GetScreen('购物车页面下单结果')

    @unittest.skip('test_mmlogin_indexshopping')
    @BeautifulReport.add_test_img('test_mmlogin_indexshopping')
    @ddt.data((13823417742, 'a12345678', '绒'))
    @ddt.unpack
    def test_mmlogin_indexshopping(self, phone, passwd, goodname):
        """
        测试密码登录主页搜索下单用例
        :param phone:手机号码
        :param passwd: 密码
        :param goodname:商品名称
        :return:
        """
        logging.info('开始测试密码登录主页搜索下单')
        l = LoginView(self.driver)
        i = IndexView(self.driver)
        l.enterindex()
        e = l.check_logined()
        if not e:
            l.mmlogin_action(phone, passwd)
        r = l.check_logined()
        self.assertTrue(r)
        i.enter_searchindex()
        i.search_action(goodname)
        r = i.check_search()
        self.assertTrue(r)
        if r:
            name = i.goods_detail()
            logging.info('goodname:%s' % name)
        self.assertTrue(i.paystatus_check())
        self.assertTrue(i.orderstatus_check(name))
        # 不报错截图保存结果
        self.GetScreen('主页搜索下单结果')

    # # @unittest.skip('test_quicklogin_classifcashopping')
    # @BeautifulReport.add_test_img('test_quicklogin_classifcashopping')
    # @ddt.data(*phone)
    # def test_quicklogin_classifcashopping(self, phone):


if __name__ == '__main__':
    unittest.main()
