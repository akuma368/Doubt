import pytest
from Tests.test_basic import Basic_test
from Pages.LoginPage import LoginPage
from Config.config import TestData


class TestLogin(Basic_test):

    def test_page_title(self):
        self.loginpage = LoginPage(self.driver)
        title_driver_gettitle = self.loginpage.get_title_of_page(TestData.TITLE_PROJECT) # here we are reciveing title via driver.title and sending actual title to LoginPage get_title_of_page
        assert  title_driver_gettitle  == TestData.TITLE_PROJECT

    def test_text_on_page(self):
        self.loginpage = LoginPage(self.driver)
        assert TestData.TEXT in self.loginpage.is_text_visible().text

    def test_name_text_box(self):
        self.loginpage = LoginPage(self.driver)
        flag = self.loginpage.is_name_visible()
        assert flag


    def test_email_text_box(self):
        self.loginpage = LoginPage(self.driver)
        flag = self.loginpage.is_email_visible()
        assert flag

    def test_check_box_display(self):
        self.loginpage = LoginPage(self.driver)
        flag = self.loginpage.is_checkbox_visble()
        assert flag

    def test_submit_button(self):
        self.loginpage = LoginPage(self.driver)
        flag = self.loginpage.is_submit_visible()
        assert flag

    def test_successfull_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(TestData.USER_NAME,TestData.EMAIL)
