import unittest
from BeautifulReport import BeautifulReport
import time
import webbrowser
from os import path

now = time.strftime('%Y-%m-%d %H-%M-%S')
report_name = 'Test_Report ' + now
scene_name = '纯购APP UI自动化'

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('./TestSuite', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename=report_name, description=scene_name, report_dir='Report', theme='theme_cyan')
    filename = 'file:///{}/Report/{}.html'.format(path.dirname(__file__), report_name)
    webbrowser.open_new_tab(filename)
