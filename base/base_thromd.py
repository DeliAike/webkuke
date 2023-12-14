from selenium.webdriver.common.by import By


class BaseThromd():

    def click_xpath(self, driver, xpath):
        driver.find_element_by_xpath(xpath).click()

    def click_link_text(self, driver, link_text):
        driver.find_element_by_link_text(link_text).click()

    def click_css(self, driver, css):
        driver.find_element_by_css_selector(css).click()

    def click_class(self, driver, cla):
        driver.find_element_by_class_name(cla).click()

    def send_key_xpath(self, driver, xpath, keys):
        driver.find_element_by_xpath(xpath).send_keys(keys)

    def send_key_id(self, driver, id, keys):
        driver.find_element_by_id(id).send_keys(keys)

    def send_key_css(self, driver, css, keys):
        driver.find_element_by_css_selector(css).send_keys(keys)

    # 存放元素的方法
    def save_element(self, driver, element):
        ele = driver.find_element_by_xpath(element)
        return ele