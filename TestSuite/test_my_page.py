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
class TestMyPage(StartEnd):

    # @unittest.skip('test_user_head_pic')
    @BeautifulReport.add_test_img('test_user_head_pic')
    @ddt.data((13823417742, 123456))
    @ddt.unpack
    def test_user_head_pic(self, phone, passwd):
        """
        测试密码登录验证用户头像变化用例
        :param phone:
        :param passwd:
        :return:
        """
        logging.info('开始测试用户头像')
        m = MyView(self.driver)
        l = LoginView(self.driver)
        l.enterindex()
        e = l.check_logined()
        if not e:
            l.mmlogin_action(phone, passwd)
        r = l.check_logined()
        self.assertTrue(r)
        # 保存最新我的页面截图
        self.GetScreen('我的页面截图')
        pass


if __name__ == '__main__':
    unittest.main()
