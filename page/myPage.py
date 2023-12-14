from time import sleep

from base.base_thromd import BaseThromd

base = BaseThromd()
class MyPage():

    def click_address(self, driver):        # 我的--->收货地址
        base.click_link_text(driver, '我的地址')

    def add_address(self, driver, address, people, phone):          # 收货地址--->添加新的收货地址
        base.click_class(driver, 'add-btn')
        base.click_css(driver, '[placeholder="请选择省/市"]')      # 选择省会
        sleep(2)
        base.click_css(driver, '[placeholder="请选择省/市"]')      # 选择省会
        sleep(2)
        base.click_css(driver, '[placeholder="请选择省/市"]')      # 选择省会
        sleep(2)
        base.click_xpath(driver, '/html/body/div[6]/div[1]/div[1]/ul/li[16]/span')        # 选择河南省
        base.click_css(driver, '[placeholder="市"]')      # 选择市区
        sleep(2)
        base.click_xpath(driver, '/html/body/div[7]/div[1]/div[1]/ul/li[1]')        # 选择郑州市
        base.click_css(driver, '[placeholder="区/县"]')      # 选择县
        sleep(2)
        base.click_xpath(driver, '/html/body/div[8]/div[1]/div[1]/ul/li[12]')      # 选择
        base.send_key_css(driver, '[class="el-textarea__inner"]', address)
        base.send_key_css(driver, '[class="el-input__inner"][maxlength="10"]', people)
        base.send_key_css(driver, '[class="el-input__inner"][maxlength="11"]', phone)
        base.click_css(driver, '[class="confirm btn"]')

    def delete_address(self, driver):               # 删除收货地址
        base.click_xpath(driver, '//*[@id="address-app"]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]')
        base.click_xpath(driver, '//*[@id="address-app"]/div[2]/div/div[2]/div[1]')