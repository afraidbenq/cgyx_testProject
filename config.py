import os
import platform
import sys


class BaseConf(object):
    # 测试环境
    ENV = "dev"

    # 系统类型
    if platform.system().lower() == "darwin":
        SYS = "mac"
    elif platform.system().lower() == "windows":
        SYS = "win"
    else:
        SYS = "linux"

    # MAC os
    chrome_app = "/Applications/Google\ Chrome.app/Contents/MacOS/"  # mac os chrome安装地址

    # Win
    chrome_reg = r"SOFTWARE\Google\Chrome\BLBeacon"  # win chrome注册表地址

    # 用例配置
    soft_name = "GOOCKR CHARGING"

    BROWSER = "Chrome"  # 启动浏览器

    url = "http://activate.navicat.com/zzcdbV2/#/login"  # 首页

    USER = "admin"

    PWD = "Goockr.8686"

    system = platform.platform()  # 系统信息

    driver_url = "https://npm.taobao.org/mirrors/chromedriver/"

    TIMEOUT = 12  # 元素等待超时时间

    exists = 10  # 元素存在等待时间

    report_title = "果壳租电后台自动化测试报告"  # 报告名字

    # 不执行的测试集
    skip_suite = []

    # 路径配置

    # CASE_NUM = None

    ROOT = os.path.dirname(os.path.abspath(__file__))

    report_path = os.path.join(ROOT, "Report")  # 报告路径

    driver_dir = os.path.join(ROOT, "chromedriver")  # 驱动路径

    pic_dir = os.path.join(ROOT, "ErrorPic")  # 截图路径

    suite_name = "TestSuite"

    suite_dir = os.path.join(ROOT, suite_name)  # 测试套件路径

    report_mod = os.path.join(ROOT, "templates", "report_template.html")

    xmind = os.path.join(ROOT, "Xmind")

    LOG_DIR = os.path.join(ROOT, "Log")  # 日志地址

    LOGGER = "webdriver_test"  # 日志名

    # 失败重跑次数
    RETRY = 0

    # 定位方法映射
    location = dict(css="CSS_SELECTOR", id="ID", name="NAME", xpath="XPATH",
                    link_text="LINK_TEXT", partial_link_text="PARTIAL_LINK_TEXT",
                    tag_name="TAG_NAME", class_name="CLASS_NAME")

    # mongo数据库配置信息
    MONGO_HOST = "192.168.199.9" if ENV == "dev" else "192.168.1.xx"
    MONGO_PORT = "27017" if ENV == "dev" else "27027"
    MONGO_USER = "yours"
    MONGO_PWD = "yours"

    # mysql配置信息

    # 测试服数据库
    # MYSQL_HOST = "gz-cdb-k615g8cv.sql.tencentcdb.com" if ENV == "dev" else "gz-cdb-k615g8cv.sql.tencentcdb.com  "
    # MYSQL_PORT = "60620"
    # MYSQL_USER = "developer"
    # MYSQL_PWD = "XADADF**##@@@20101"
    # 预发布数据库
    MYSQL_HOST = "gz-cdb-h2ub8r9n.sql.tencentcdb.com" if ENV == "dev" else "gz-cdb-h2ub8r9n.sql.tencentcdb.com"
    MYSQL_PORT = "60581"
    MYSQL_USER = "test"
    MYSQL_PWD = "Test123456"



    # API主机域名
    # API_HOST = "http://testnewapi.chungoulife.com"  # 测试服
    API_HOST = "http://readynewmall.chungoulife.com"  # 预发布
    # API_HOST = "http://graynewmall.chungoulife.com"  # 灰度

    # xmind头文件配置
    xmind_head = ["from TestSuite.base_case import BaseCase",
                  "from Tools.decorator import screenshot"]


class TiebaConf(BaseConf):
    url = "http://tieba.baidu.com"  # 测试百度贴吧配置


def set_config():
    # 使用CMD运行此脚本时，在run_case.py 后面加上SearchConf ，运行时会调用TiebaConf的配置替换BaseConf
    name = sys.argv[1] if len(sys.argv) >= 2 else "BaseConf"
    cls_config = {"BaseConf": BaseConf, "SearchConf": TiebaConf}
    return cls_config.get(name, BaseConf)


class Config(set_config()):
    pass