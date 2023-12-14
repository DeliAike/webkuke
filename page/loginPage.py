from base.base_thromd import BaseThromd

base = BaseThromd()
class LoginPage():      # 登录页面

    def phone_number_login(self, driver):       # 选择账号密码登录方式
        base.click_css(driver, '[class="login-type-controller login-type-password fl"]')

    def input_user_password(self, driver, username, password):      # 输入账号密码--->登录
        base.send_key_id(driver, 'tel-input-password', username)  # 账号
        base.send_key_id(driver, 'password', password)  # 密码
        base.click_css(driver, '[class="login-btn login-pw-btn"]')