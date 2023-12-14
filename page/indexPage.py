from base.base_thromd import BaseThromd

base = BaseThromd()

class IndexPage():

    def remove_alter(self, driver):     # 关闭首页广告
        base.click_css(driver, '[class="close abs"]')

    def click_login(self, driver):      # 首页--->点击登录
        base.click_xpath(driver, '//span[text()="登录"]')

    def into_my(self, driver):      # 首页 ----> 个人中心
        base.click_class(driver, 'user-text')