import pytest

from page.indexPage import IndexPage
from page.loginPage import LoginPage
from page.myPage import MyPage

indexpage = IndexPage()
mypage = MyPage()
loginpage = LoginPage()

class TestLogin:

    @pytest.mark.parametrize('username, password, address, people, phone', [('18348443861', 'xh123456' ,'测试数据11111111', '测试001', '18348443861')])
    def test_login(self, kuke, username, password, address, people, phone):

        indexpage.remove_alter(kuke)
        indexpage.click_login(kuke)
        loginpage.phone_number_login(kuke)
        loginpage.input_user_password(kuke, username, password)
        indexpage.into_my(kuke)
        mypage.click_address(kuke)
        mypage.add_address(kuke, address, people, phone)
        mypage.delete_address(kuke)
