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

    system = platform.platform()  # 系统信息

    TIMEOUT = 12  # 元素等待超时时间

    exists = 10  # 元素存在等待时间

    # 路径配置

    ROOT = os.path.dirname(os.path.abspath(__file__))

    report_path = os.path.join(ROOT, "Report")  # 报告路径

    suite_name = "TestSuite"

    suite_dir = os.path.join(ROOT, suite_name)  # 测试套件路径

    LOG_DIR = os.path.join(ROOT, "logs")  # 日志地址

    CONFIG_DIR = os.path.join(ROOT, "config")  # 配置文件路径

    img_dir = os.path.join(ROOT, "img")  # 截图路径

    # mongo数据库配置信息

    MONGO_HOST = "192.168.199.9" if ENV == "dev" else "192.168.1.xx"
    MONGO_PORT = "27017" if ENV == "dev" else "27027"
    MONGO_USER = "yours"
    MONGO_PWD = "yours"

    # mysql配置信息

    # 测试服数据库
    MYSQL_HOST = "gz-cdb-k615g8cv.sql.tencentcdb.com" if ENV == "dev" else "gz-cdb-k615g8cv.sql.tencentcdb.com  "
    MYSQL_PORT = "60620"
    MYSQL_USER = "developer"
    MYSQL_PWD = "XADADF**##@@@20101"
    # 预发布数据库
    # MYSQL_HOST = "gz-cdb-h2ub8r9n.sql.tencentcdb.com" if ENV == "dev" else "gz-cdb-h2ub8r9n.sql.tencentcdb.com"
    # MYSQL_PORT = "60581"
    # MYSQL_USER = "hyl"
    # MYSQL_PWD = "Hyl12345600"

    # API主机域名

    API_HOST = "https://test-lives-api.chungoulife.com"  # 测试服
    # API_HOST = "https://ready-lives-api.chungoulife.com"  # 预发布
    # API_HOST = "https://gray-lives-api.chungoulife.com"  # 灰度


class TiebaConf(BaseConf):
    url = "http://tieba.baidu.com"  # 测试百度贴吧配置
    pass


def set_config():
    # 使用CMD运行此脚本时，在run_case.py 后面加上SearchConf ，运行时会调用TiebaConf的配置替换BaseConf
    name = sys.argv[1] if len(sys.argv) >= 2 else "BaseConf"
    cls_config = {"BaseConf": BaseConf, "SearchConf": TiebaConf}
    return cls_config.get(name, BaseConf)


class Config(set_config()):
    pass
