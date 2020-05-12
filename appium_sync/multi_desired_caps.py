from appium import webdriver
import yaml
from time import ctime
import logging


with open('C:\\cgyx_testProject\\appium_sync\\desired_caps.yaml', 'r', encoding='utf-8') as file:
    data = yaml.load(file)

devices_list = ['7N2RDQ149T026117', 'A1CEBND232MB', 'YS55VOYDS88SDQ9T']


def appium_desired(udid, port):
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['udid'] = udid

    desired_caps['app'] = data['app']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']

    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    logging.info('appium port:%s start run %s at %s' % (port, udid, ctime()))
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) + '/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    return driver


if __name__ == '__main__':
    appium_desired(devices_list[2], 4727)
