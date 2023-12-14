import pytest
from airtest.core.api import auto_setup
from airtest.report.report import LogToHtml
from airtest_selenium import WebChrome



@pytest.fixture(scope='session')
def kuke():
    auto_setup(__file__, logdir=r'D:\\pycharm\\aike\\webkuke\\report')   # 指定生成log日志的路径，和下面生成报告配合使用

    driver = WebChrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get('https://www.kuke99.com')
    yield driver
    h1 = LogToHtml(script_root=__file__, log_root=r'D:\\pycharm\\aike\\webkuke\\report', lang='zh',
                   plugins=["airtest_selenium.report"])
    h1.report(output_file=r'D:\\pycharm\\aike\\webkuke\\report\\log.html')
    driver.quit()