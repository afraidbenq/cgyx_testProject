from appium import webdriver
import yaml
import logging
import logging.config
from os import path
from config import Config

log_file_path = path.join(Config.CONFIG_DIR, 'log.conf')
logging.config.fileConfig(log_file_path)
logging = logging.getLogger()


def appium_desired():
    with open(Config.CONFIG_DIR + '\cgyx_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']

    base_dir = path.dirname(path.dirname(__file__))
    app_path = path.join(base_dir, 'app', data['appname'])
    desired_caps['app'] = app_path

    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']
    desired_caps['ANDROID_UIAUTOMATOR'] = data['ANDROID_UIAUTOMATOR']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['chromedriverUseSystemExecutable'] = data['chromedriverUseSystemExecutable']

    logging.info('start app...')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(3)
    return driver


if __name__ == '__main__':
    appium_desired()
